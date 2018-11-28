#include<iostream>
#include <fstream>
using namespace std;
    ofstream fout ("file.out");
    ifstream fin ("file.in");
    int d[4][2]={{-1,0},{0,-1},{0,1},{1,0}};
    int a[100][100],b[100][100],h,w,num=1,tt;
    void pri(int i){
         fout<<"Case #"<<i+1<<":"<<endl;
         for(int j1=0;j1<h;j1++){
           for(int j2=0;j2<w-1;j2++)
             fout<<char('a'+b[j1][j2]-1)<<" ";
           fout<<char('a'+b[j1][w-1]-1)<<endl;
         }
    }
    void aa(int i,int j){
         b[i][j]=tt;
         int minn=10001,x,y;
         bool mark=false;
         for(int k=0;k<4;k++)
           if(i+d[k][0]>=0&&i+d[k][0]<h&&j+d[k][1]>=0&&j+d[k][1]<w&&a[i+d[k][0]][j+d[k][1]]<minn){
             x=i+d[k][0];
             y=j+d[k][1];
             minn=a[x][y];
             mark=true;
           }
         if(mark)
         if(a[i][j]>a[x][y])
          if(b[x][y]==0)
           aa(x,y);
          else tt=b[x][y];
         b[i][j]=tt;
    }
int main(){
    int t;
    fin>>t;
    for(int i=0;i<t;i++){
      fin>>h>>w;
      num=1;
      for(int j1=0;j1<h;j1++)
        for(int j2=0;j2<w;j2++){
          fin>>a[j1][j2];
          b[j1][j2]=0;
        }
      for(int j1=0;j1<h;j1++)
        for(int j2=0;j2<w;j2++)
          if(b[j1][j2]==0){
            tt=num;
            aa(j1,j2);
            if(tt==num)
              num++;
          }
      pri(i);
    }
    return 0;
}
