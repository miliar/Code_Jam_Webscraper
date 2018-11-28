#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;

int main(){
    int i,n,j,x,k;
    char test[501],s[20]="welcome to code jam";
    fstream fout;
   // fin.open("in.txt");
    fout.open("out1.txt");
    cin>>n;
    for(i=1;i<=n+1;i++){
               int a[20][9501],f[20][9501];
               
               gets(test);
               int l= strlen(test);
               
               for (j=0;j<strlen(s);j++)
                   for(x=0;x<l;x++)
                       a[j][x]=0,f[j][x]=0;
                       
               for(j=l-1;j>=0;j--){
                     for(x=0;x<strlen(s);x++) a[x][j]=a[x][j+1];
                     for (k=0;k<strlen(s);k++)
                         if (test[j]==s[k]) a[k][j]=a[k][j]+1;
               }
             
               for(x=0;x<l;x++) f[18][x]=a[18][x];
               
               int flag=0;
               
               for(j=strlen(s)-2;j>=0;j--){ 
                   for(x=l-1;x>0;x--){
                       if(a[j][x]<a[j][x-1]) {
                          f[j][x-1]=f[j+1][x-1]+f[j][x];
                          if(f[j][x-1]>=10000) f[j][x-1]-=10000;
                       }
                       else f[j][x-1]=f[j][x];
                   }
               }
               if(i>1){
                   if  (f[0][0]>=1000)
                   fout<<"Case #"<<i-1<<": "<<f[0][0]<<endl;
                   else {
                       if  (f[0][0]>=100)
                       fout<<"Case #"<<i-1<<": 0"<<f[0][0]<<endl;
                       else{ 
                           if  (f[0][0]>=10)
                           fout<<"Case #"<<i-1<<": 00"<<f[0][0]<<endl;
                           else{
                               if (f[0][0]>=0)
                               fout<<"Case #"<<i-1<<": 000"<<f[0][0]<<endl;
                               else
                               fout<<"Case #"<<i-1<<": 0000"<<endl;
                           }
                       }
                   }
               }
    }
    //fin.close();
    fout.close();
    getch();
    return 0;
}
