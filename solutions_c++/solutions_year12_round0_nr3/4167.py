#include<iostream>
#include<conio.h>
#include<fstream>
using namespace std;

int t;
int x=1;
int a,b;
int m,n,o,y;
main(){
       ifstream nobj("c-small-attempt0.in");
       ofstream robj("op3.in");
       nobj>>t;
       while(nobj>>a>>b){
       y=0;
       if(a<=99&&b>=10){
       for(int i=a;i<=b;i++){                 
       m=i/10;
       n=i%10;                 
       if((10*n+m<=b)&&(10 * n + m > i))
       y++;}}
       else if(b>=100&&a<=999){
for(int i=a;i<=b;i++){
        m=i/100;
        n=(i/10)-10*m;            
       o=i%10;
        if ((100 * o + 10 * m + n > i) && (100 * o + 10 * m + n <= b))
        y++;
        if ((100 * n + 10 * o + m > i) && (100 * n + 10 * o + m <= b))
        y++;}}
        robj<<"Case #"<<x<<": "<<y<<endl;
        x++;
        }         
                     
getch();
}
