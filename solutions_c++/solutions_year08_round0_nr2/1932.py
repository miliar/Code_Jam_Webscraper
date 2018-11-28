#include<iostream>
#include<fstream>
#include<string.h>
using namespace std;
struct train{
       int mins;
       int type;
};

void swap(train *a, train *b){
	train temp;
	temp=*a;
	*b=*a;
	*a=temp;
}


void sort(train *t1,int n){
     for(int i=0;i<n-1;i++){
             for(int j=i+1;j<n;j++){
                     if(t1[i].mins>t1[j].mins)
                           swap(t1[i],t1[j]);
                     else if(t1[i].mins==t1[j].mins)
                           if((t1[i].type==1||t1[i].type==3)&&(t1[j].type==2||t1[j].type==4))
                                  swap(t1[i],t1[j]);
              }
     }
}             
     
int main(){
    ifstream in("B-large.in");
    ofstream out("B-large.out");
    //ofstream out2("B.in");
    int n;
    in>>n;
    for(int i=1;i<=n;i++){
            int na,nb,turn,h,m;
            char ch;
            train *t1;
            in>>turn;
            in>>na>>nb;
            int z=(na+nb)*2,k=0,tra=0,trb=0,ansa=0,ansb=0;
            t1=new train[z];
            for(int j=0;j<na;j++){
                    in>>h>>ch>>m;
                    t1[k].mins=((h*60)+m);
                    t1[k++].type=1;//train leaves from A
                    in>>h>>ch>>m;
                    t1[k].mins=((h*60)+m+turn);
                    t1[k++].type=2;//train arrives at B +turnaround
            }
            for(int j=0;j<nb;j++){
                    in>>h>>ch>>m;
                    t1[k].mins=((h*60)+m);
                    t1[k++].type=3;//train leaves from B
                    in>>h>>ch>>m;
                    t1[k].mins=((h*60)+m+turn);
                    t1[k++].type=4;//train arrives at A +turnarond
            }
           sort(t1,z);
          // for(int m=0;m<z;m++)
            //        out2<<t1[m].mins<<" "<<t1[m].type<<'\n';
             for(int m=0;m<z;m++){
                   switch(t1[m].type){
                         case 1:
                              if(tra==0)
                                   ansa++;
                              else
                                   tra--;
                              break;
                         case 2:
                              trb++;
                              break;
                         case 3:
                              if(trb==0)
                                   ansb++;
                               else
                                   trb--;
                               break;
                         case 4:
                              tra++;
                              break;
                         default:
                              return -1;
                   }
           }
           out<<"Case #"<<i<<": "<<ansa<<" "<<ansb<<endl;
           delete [] t1;
    }             
    in.close();
    out.close();
}
