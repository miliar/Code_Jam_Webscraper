#include<iostream>
#include<fstream>

using namespace std;

struct cord{
       int x;
       int y;
};      

int main(){
    std::ifstream infile("C:/Users/aman/Desktop/input1.txt");
    std::ofstream output("C:/Users/aman/Desktop/output1.txt");
    //input.open("C:\Users\aman\Desktop\input.txt");
    //output.open("C:\Users\aman\Desktop\output.txt");
    int T;
    infile>>T;
    
    int i;
    char A,B,C,D;
    struct cord x[4];
    struct cord y[4];
    struct cord l;
    struct cord r;
    
    for(i=1;i<=T;i++){
                      string ans = "None";
                      int m=0;
                      
                      for(m=0;m<4;m++){
                                       x[m].x=0;
                                       x[m].y=0;
                                       y[m].x=0;
                                       y[m].y=0;
                                       l.x=0;
                                       r.x=0;
                                       l.y=0;
                                       r.y=0;
                      }
                      
                      
                      int j;
                      
                      for(j=0;j<4;j++){
                                       
                                       infile>>A>>B>>C>>D;
                                       if(A=='X' || A == 'T'){
                                                 
                                                 x[0].x+=1;
                                                 
                                                 y[j].x+=1;
                                                 
                                                 if(j==0){
                                                 l.x+=1;
                                                 }
                                                 
                                                 
                                                 if(j==3){
                                                 r.x+=1;
                                                 }
                                                 
                                       }

                                       if(B=='X' || B == 'T'){
                                                
                                                 x[1].x+=1;
                                                 
                                                 y[j].x+=1;
                                                 
                                                 if(j==1){
                                                 l.x+=1;
                                                 }
                                                 
                                                 if(j==2){
                                                 r.x+=1;
                                                 }
                                                 
                                       }
                                       if(C=='X' || C == 'T'){
                                                
                                                 x[2].x+=1;
                                                 
                                                 y[j].x+=1;
                                                 if(j==2){
                                                 l.x+=1;
                                                 }
                                                 
                                                 if(j==1){
                                                 r.x+=1;
                                                 }
                                                 
                                       }
                                       if(D=='X' || D == 'T'){
                                               
                                                 x[3].x+=1;
                                                 
                                                 y[j].x+=1;
                                                 
                                                 if(j==3){
                                                 l.x+=1;
                                                 }
                                                 
                                                 if(j==0){
                                                 r.x+=1;
                                                 }
                                       }
                                       
                                       
                                       
                                       
                                       
                                       
                                       if(A=='O' || A == 'T'){
                                                 x[0].y+=1;
                                                 
                                                 y[j].y+=1;
                                                 
                                                 if(j==0){
                                                 l.y+=1;
                                                 }
                                                 
                                                 if(j==3){
                                                 r.y+=1;
                                                 }
                                                 
                                       }

                                       if(B=='O' || B == 'T'){
                                                 x[1].y+=1;
                                                 
                                                 y[j].y+=1;
                                                 
                                                 if(j==1){
                                                 l.y+=1;
                                                 }
                                                 if(j==2){
                                                 r.y+=1;
                                                 }
                                                 
                                       }
                                       if(C=='O' || C == 'T'){
                                                 x[2].y+=1;
                                                 
                                                 y[j].y+=1;
                                                 if(j==2){
                                                 l.y+=1;
                                                 }
                                                 if(j==1){
                                                 r.y+=1;
                                                 }
                                                 
                                       }
                                       if(D=='O' || D == 'T'){
                                                 x[3].y+=1;
                                                 y[j].y+=1;
                                                 if(j==3){
                                                 l.y+=1;
                                                 }
                                                 if(j==0){
                                                 r.y+=1;
                                                 }
                                       }
                            }
                                       
                                       int k=0;
                                       
                                       
                                       for(k=0;k<4;k++){
                                                        
                                                        if(x[k].x==4 || y[k].x==4 || r.x==4||l.x==4) 
                                                        {             
                                                                      
                                                                      ans = "X won";
                                                                     break;
                                                        }
                                                        
                                                        if(x[k].y==4 || y[k].y==4 || r.y==4||l.y==4) 
                                                        {             ans = "O won";
                                                                     break;
                                                        }
                                                                                                                
                                                        
                                       }
                                       
                                       if(ans == "None"){
                                              
                                              if(  ((x[0].x + x[0].y) >= 4) &&  ((x[1].x + x[1].y) >= 4) && ((x[2].x + x[2].y) >= 4) && ((x[3].x + x[3].y) >= 4) && ((y[0].x + y[0].y) >= 4) &&  ((y[1].x + y[1].y) >= 4) && ((y[2].x + y[2].y) >= 4) && ((y[3].x + y[3].y) >= 4) && ((l.x + l.y) >=4) && ((r.x + r.y) >=4) ){
                                              ans = "Draw";
                                              }
                                              else
                                              ans = "Game has not completed";
                                       }
                      
                                                                      
                      
                      output<<"Case #"<<i<<": "<<ans<<endl;
                      
    }
    
    
    //system("pause");
    return 0;
}
