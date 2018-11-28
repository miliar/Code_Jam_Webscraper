#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <fstream>


using namespace std;
double nums[100000];
double certo = 1;
double melhor;
ofstream myfile;

double keepTyping(int escrevi, int total){
  
    return certo * (total-escrevi+1) + (1-certo)*(total-escrevi+2+total);
    
}


double pressEnter(int total){
    return  (total + 2);
}

double backspace(int escrevi, int total, int times){
    double lcerto=1;
    for(int i = 0 ; i < escrevi-times ; i++) lcerto*=nums[i];
    
    return lcerto * (total-escrevi+1+times*2) + (1-lcerto)*(total-escrevi+2+total+times*2);
}

int main(){
    int n,a,b;
    myfile.open ("testeJamA1.txt");
       
    scanf("%d",&n);
    
    for(int t=1;t<=n;t++)
    {
               certo=1;
               scanf("%d%d",&a,&b);
               for(int i = 0 ; i < a ; i++){
                       scanf("%lf",&nums[i]);
                       certo*=nums[i];
               }
               melhor=keepTyping(a,b);
               double temp;
               temp = pressEnter(b);
               if(temp<melhor) melhor = temp;
               for(int i = 1 ; i <= a ; i++){
                       temp=backspace(a,b,i);
                       if(temp<melhor) melhor = temp;
               }
               
               int pos = (int)((melhor-((int)melhor))*1000000);
               int pos2=pos;
               int nzero=0;
               
               myfile << "Case #" << t << ": " << (int) melhor << "."  ;     
               while((pos/=10)>0) nzero++;
               
               for(int i = 0 ; i < 5-nzero ; i++) myfile << "0";

                myfile << pos2 << "\n"; 
               
    }
    return 0;
}
