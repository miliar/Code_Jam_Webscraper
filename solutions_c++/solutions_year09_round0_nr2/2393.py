#include<iostream>
#include<fstream>
#include<vector>

using namespace std;



#define DRY  '.'
#define SINK 1

enum MyEnumType { NORTH, WEST, EAST, SOUTH };



struct Latitude{
    int altitude;
    char label;
    
};

class Position{
 public:
 int i,j;
 bool isSink;

 Position(){
 
    isSink=false;
    i=-1;
    j=-1;
    
 }
 void setCoords(int i,int j){
    this->i=i;
    this->j=j;
 }
 
 bool isDisabled(){
    return i==-1&&j==-1;     
 }
     
};



Latitude map[101][101];
int H,W;
char currentLetter='a'-1;

void basinFlow();
Position getNextPosition(int i,int j);
char flowStep(int i,int j);
void printMat();



int main(){
    
    ifstream cin("watersheds.in");
    ofstream cout("watersheds.out");
    
    int T;//number of maps
  
    int i,j,k;
    
    cin>>T;
    
    for(i=0;i<T;i++){
            cin>>H>>W;  
            
            for(j=0;j<H;j++){//reading the matrix
                for(k=0;k<W;k++){
                    cin>>map[j][k].altitude;
                    map[j][k].label=DRY;
                 }
            } 
            
            basinFlow(); 
            //print result
            cout<<"Case #"<<i+1<<": "<<endl;
            for(j=0;j<H;j++){ 
                for(k=0;k<W;k++){
                         
                        cout<<map[j][k].label<<" ";
                }
                cout<<endl;
             } 
           
   }
   
   
    
    

system("pause");
return 0;
}


void printMat(int ci,int cj){
    int i,j;
   for(i=0;i<H;i++){
         for(j=0;j<W;j++){
            if(ci==i&&cj==j)
              cout<<"[";
           
            cout<<"("<<map[i][j].altitude<<","<<map[i][j].label<<")";
            
            if(ci==i&&cj==j)
              cout<<"]";
            
        }
        cout<<endl;
    }  
}
void basinFlow(){
    int i,j;
    currentLetter='a'-1;
    
    for(i=0;i<H;i++){ 
        for(j=0;j<W;j++){
             
              flowStep(i,j);
    } }
     
}



char flowStep(int i,int j){
    
    Position pos=getNextPosition(i,j);
    //cout<<"current: "<<i<<", "<<j<<": "<<map[i][j].altitude<<endl;
    //cout<<"next: "<<pos.i<<", "<<pos.j<<": "<<map[pos.i][pos.j].altitude<<endl<<endl;
  // printMat(i,j);
   //cin.get();
    
    if(map[pos.i][pos.j].label!=DRY){
       
       //cout<<"water!"<<endl;
       map[i][j].label=map[pos.i][pos.j].label;
        return map[pos.i][pos.j].label;
    }else
    if(pos.isSink){//current position is sink and doesnt have wather
        currentLetter++;
        map[i][j].label=currentLetter;
      
      //  cout<<"Sink!"<<endl;
   
    
        return map[i][j].label;
    }
    
    map[i][j].label=flowStep(pos.i,pos.j);
    
    return map[i][j].label;
    
}   

Position getNextPosition(int i,int j){
    
    Position pos[4],menorPos;
    int menorAltitude=0;
    bool isSink=true;
    
    if(i-1>=0) pos[NORTH].setCoords(i-1,j);
    if(j-1>=0) pos[WEST].setCoords(i,j-1);
    if(j+1<W)  pos[EAST].setCoords(i,j+1);
    if(i+1<H)  pos[SOUTH].setCoords(i+1,j);
  
    
    menorAltitude=map[i][j].altitude;
    
    for(int k=0;k<4;k++)
    {
        if(pos[k].isDisabled())
            continue;
            
               
        if(map[pos[k].i][pos[k].j].altitude<menorAltitude){
            
            menorPos.setCoords(pos[k].i,pos[k].j);
            menorAltitude=map[pos[k].i][pos[k].j].altitude;
            isSink=false;
        }
        
    }
    
    if(isSink){
        menorPos.setCoords(i,j);
        menorPos.isSink=true;
        return menorPos;
    }
    
    return menorPos;
    
   
    
}



