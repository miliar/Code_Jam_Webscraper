#include<iostream>
#include<cstdio>
#include<string>
#include<fstream>
using namespace std;
int arr[1001][1001]={0};
void pre()
{
     int i,t,small,rem,ct,j;
     for(i=10;i<100;i++){
                         t=i;
                                     rem=t%10;
                                     t/=10;
                                     t+=rem*10;
                                     arr[i][t]=1;
     }
     for(i=100;i<1000;i++){
                         t=i;
                             for(j=0;j<2;j++){
                                     rem=t%10;
                                     t/=10;
                                     t+=rem*100;           
                                     arr[i][t]=1;
                             }
     }
}
int main()
{
    pre();
    int i,t,a,b,j,k,ct;
    ofstream istr;
    istr.open("demo.txt");
    scanf("%d",&t);
    for(i=1;i<=t;i++){
                      ct=0;
                     scanf("%d%d",&a,&b);
                     for(j=a;j<b;j++)
                                     for(k=j+1;k<=b;k++){
                                                         if(arr[j][k]==1){
                                                                         ct++;
                                                         }
                                     }
                     istr<<"Case #"<<i<<": "<<ct<<"\n";
    }
    istr.close();
    return 0;
}
