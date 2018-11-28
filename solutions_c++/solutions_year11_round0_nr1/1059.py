#include <iostream>
#include <fstream>

using namespace std;

struct point{
       
char c;
int p;

};

struct Bot{

   Bot(char col){
   c=col;         
   x=1;
   n=0;
   done=false;
   p=NULL; 
   }

   void load(point *points, int num){
           p=points;
           x=1;
           n=0;
           done=false;
           tot=num;
           press=false;
           }
       
   void move( Bot &two ){
 
       press=false;

       while(p[n].c != c &&n<tot ){
         n++;
        }

       if(n>=tot){
       done=true;
       return;           
       }

       if(p[n].p>x){
           x++;          
           return;     
          }
       if(p[n].p<x){
           x--;          
           return;     
          }
       if(two.n<n)
         return;

       //PRESS BUTTON
       if(two.press)
          return;
       press=true;
       n++;
        while(p[n].c != c &&n<tot ){
          n++;
         }

       if(n>=tot){
       done=true;
       return;           
       }
       
    }  
          
bool done, press;
char c;
int x;
int n;//number in sequence
point *p;
int tot;

};





int main(){
ifstream inf;
ofstream fout;
int cases=0,n,steps=0;
int *sizes,*results;
point **points;
bool done;
int oPos,bPos;
Bot o('O');
Bot b('B');
char fileName[100];
    
//input data
inf.clear();
cout<<"enter file name: ";
cin>>fileName;
inf.open(fileName);
if(!inf.good()){
                cout<<"ERROR";
                system("pause");
                }
                
                


inf>>cases;

points=new point* [cases];
sizes=new int[cases];
results=new int[cases];

for( int i=0;i<cases;i++){
      inf>>sizes[i];
      
      points[i]=new point[sizes[i]];
      
      for(int j=0;j<sizes[i];j++){
              inf>>points[i][j].c;
              inf>>points[i][j].p;              
              }
     
     }
    



for(int i=0;i<cases;i++){
        results[i]=0;
        b.load(points[i],sizes[i]);
        o.load(points[i],sizes[i]);
                
        while(!b.done || !o.done){



                     results[i]++;
                     b.move(o);
                     o.move(b);
                     o.press=false;
                     b.press=false;


                     }
    
       }
      
  fout.clear();
  fout.open("out.txt");
      
   for(int i=0;i<cases;i++){
           fout<<"Case #"<<i+1<<": "<<results[i]<<endl;
           }   
      
      
 return 0;   
}
