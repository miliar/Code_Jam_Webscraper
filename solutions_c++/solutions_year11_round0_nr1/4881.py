#include <cstdlib>
#include <iostream>

#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cctype> 
#include <string> 
#include <cstring> 
#include <ctime> 

using namespace std;

int diff(int &x ,int &y){
if((x-y)<0) return -1*(x-y);
else return (x-y);
    }


int main(){

    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);
    
    char color[1000];
    int value[1100];
    int cases,i,j,k,l,m,nbutton,totalseconds,backseconds,oposition ,bposition,presentcolor,otimepassed,btimepassed,dif,lastotimepassed=0,lastbtimepassed=0;

    scanf("%d" ,&cases);


    for(l=1;l<=cases;l++){
                          scanf("%d" ,&nbutton );
                          for(int m=1;m<=nbutton;m++)scanf(" %c %d" ,&color[m], &value[m] );
                          totalseconds=0,oposition=1 ,bposition=1,otimepassed=0,btimepassed=0,lastotimepassed=0,lastbtimepassed=0;

//for(int m=1;m<=nbutton;m++){
        
//        if(color[m]=='O')present=1;
//        if(color[m]=='B')present=2;
//        if(color[m+1]=='O')present=1;
//        if(color[m]=='B')present=2;        
        
  //       }

                          for(int m=1;m<=nbutton;m++){
                                  
                                  if(color[m]=='O'){

                                                    dif=(diff(value[m],oposition)+1);
                                                    if( (dif-btimepassed)<=0 ){
                                                         totalseconds=totalseconds+1;otimepassed++;//cout<<otimepassed<<"o ,";
                                                         lastotimepassed=otimepassed;
                                                         }
                                                    else if( (otimepassed=(dif-btimepassed) )>0 ){
                                                             totalseconds=totalseconds+otimepassed;
                                                             otimepassed=lastotimepassed+otimepassed;//cout<<otimepassed<<"o ,";
                                                             lastotimepassed=otimepassed;
                                                             }
                                                    btimepassed=0;lastbtimepassed=0;oposition=value[m];//cout<<totalseconds<<"o ,";
                                                    }
                                  else if(color[m]=='B'){
                                                    dif=(diff(value[m],bposition)+1);
                                                    if( (dif-otimepassed)<=0 ){
                                                         totalseconds=totalseconds+1;btimepassed++;//cout<<btimepassed<<"b ,";
                                                             lastbtimepassed=btimepassed;
                                                         }
                                                    else if( (btimepassed=(dif-otimepassed))>0 ){
                                                             totalseconds=totalseconds+btimepassed;
                                                             btimepassed=lastbtimepassed+btimepassed;//cout<<btimepassed<<"b ,";
                                                             lastbtimepassed=btimepassed;
                                                             }
                                                    otimepassed=0;lastotimepassed=0;bposition=value[m];//cout<<totalseconds<<"b ,";

                                                    }
                                  }
cout<<"Case #"<<l<<": "<<totalseconds<<"\n";                          
                          
                          }

return 0;
    }
