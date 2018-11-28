#include<stdio.h>
#include<conio.h>
#include<iostream>
#include<string.h>
#include<fstream>
using namespace std;
int a[105][105];
int dir(int i,int j){
    int n,e,w,s,p;
    p=a[i][j];
    s=a[i+1][j];
    e=a[i][j+1];
    w=a[i][j-1];
    n=a[i-1][j];
    if(p<=n && p<=e && p<=w && p<=s) return 0;
    if(n<=p && n<=e && n<=w && n<=s) return 1;
    if(w<=n && w<=e && w<=p && w<=s) return 4;
    if(e<=n && e<=p && e<=w && e<=s) return 2;
    if(s<=n && s<=e && s<=w && s<=p) return 3;
}

int main(){
    int h,w,n,i,b[105][105],c=97,j,k;
    char r[109][109];
    fstream fin ,fout;
    fin.open("in.in");
    fout.open("out.txt");
    fin>>n;
    for(k=1;k<=n;k++){
               fin>>h>>w;
               int c=97;
               for(i=1;i<=h;i++)
                  for(j=1;j<=w;j++)
                     fin>>a[i][j];

               for(i=0;i<=h;i++) a[i][0]=10001,b[i][0]=0,a[i][w+1]=10001;
               for(i=0;i<=w;i++) a[0][i]=10001,b[0][i]=0,a[h+1][i]=10001;
               
               for(i=0;i<=h+1;i++)
                       for(j=0;j<=w+1;j++) b[i][j]=0,r[i][j]= 0;
                       
               for(i=1;i<=h;i++){
                   for(j=1;j<=w;j++){
                         b[i][j]=dir(i,j);
               }}
               
               for(i=1;i<=h;i++)
                   for(j=1;j<=w;j++) r[i][j]=0;
               for (int x=1;x<=5;x++)    {
                   for(i=1;i<=h;i++)
                       for(j=1;j<=w;j++){
                           if(!r[i][j]){
                               if(b[i][j]==0) r[i][j]=c,c++;
                               
                               if(b[i][j]==1) if(r[i-1][j]) r[i][j]=r[i-1][j];
                               if(b[i][j]==2) if(r[i][j+1]) r[i][j]=r[i][j+1];
                               if(b[i][j]==3) if(r[i+1][j]) r[i][j]=r[i+1][j];
                               if(b[i][j]==4) if(r[i][j-1]) r[i][j]=r[i][j-1];
                               
                               if(b[i][j-1]==2) r[i][j-1]=r[i][j];
                               if(b[i+1][j]==1) r[i+1][j]=r[i][j];
                               if(b[i][j+1]==4) r[i][j+1]=r[i][j];
                               if(b[i-1][j]==3) r[i-1][j]=r[i][j];
                           }
                   }
               }
               if (r[1][1]!=97) {
                   int q=r[1][1];
                   for(i=1;i<=h;i++)
                     for(j=1;j<=w;j++){
                        if(r[i][j]==q) r[i][j]=97;
                        else
                            if(r[i][j]==97) r[i][j]=q;
                     }
               }
               fout<<"Case #"<<k<<":"<<endl;
                for(i=1;i<=h;i++){
                   for(j=1;j<=w;j++)
                     fout<<r[i][j]<<" ";
                     fout<<endl;
                }
    }
    fin.close();
    fout.close();
    getch();
    return 0;
}
