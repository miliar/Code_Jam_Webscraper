/*
  Developed by: kamalesh
  Compiler : Dev-C++ 4.9.9.2
  OS: Windows Vista Home
*/
#include<iostream>
#include<conio.h>
#include<fstream.h>

using namespace std;

fstream finput,foutput;

int main(){
    int t=1,n=0;
    double k=0; //n: snapper in which the bulb is connected k: number of times snapped
    char state[][5]={"OFF","ON"};
    int findbulbstate(int,double);
 
 
     finput.open("input.in",ios::in);
      finput>>t;
    
    int temp=2;
    int lim=1; 
    
    while(lim<=t){
    finput>>n>>k;                   
    temp=findbulbstate(n,k);
    cout<<"Case #"<<lim<<": "<<state[temp]<<endl;
    lim++;
    }

    finput.close();
    getch();
    return 0;
}



int findbulbstate(int n,double k=0){
    int snapper=n-1;
    double snaps=k;
    int toggle(int);
    //n: snapper in which the bulb is connected, k: number of times snapped
    int snapper_status[30],power[30]; 

    for(int i=0;i<30;i++){
            snapper_status[i]=power[i]=0;
    }

    //power[0]= 1 ; this means, first snapper is recieving power
    power[0]=1;
    for(int j=0; j<snaps ;j++){
            for(int l=0;l<=snapper;l++){
               if(power[l]==1){
                    snapper_status[l]=toggle(snapper_status[l]);
               }
               if(l>0){
                 if(power[l-1]==1 && snapper_status[l-1]==1){
                                  power[l]=1;
                 }
                 else
                     power[l]=0;
               }
            }//End of loop l
    }//End of loop j
    if(power[snapper]==1 && snapper_status[snapper]==1)
      return 1;
    else
      return 0;
}



int toggle(int status){
    if(status==0)
     return 1;
    else 
     return 0;
}
