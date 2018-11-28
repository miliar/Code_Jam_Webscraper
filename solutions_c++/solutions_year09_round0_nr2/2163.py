#include<iostream>
#include<fstream>
using namespace std;

int n,h,w,num;
int a[105][105];
int ans[105][105];
ofstream fout("B-large.out");
ifstream fin("B-large.in");

int search(int x,int y)
{
     int i,j,k,t;
     if (ans[x][y]==0)
     {
                       i=0;j=0;k=a[x][y];t=0;
                       if (x-1>0 && a[x-1][y]<k) {k=a[x-1][y];t=1;i=x-1;j=y;}
                       if (y-1>0 && a[x][y-1]<k) {k=a[x][y-1];t=1;i=x;j=y-1;}
                       if (y+1<=w && a[x][y+1]<k) {k=a[x][y+1];t=1;i=x;j=y+1;}                       
                       if (x+1<=h && a[x+1][y]<k) {k=a[x+1][y];t=1;i=x+1;j=y;}                       
                       
                       if (t==0) {num++;ans[x][y]=num;}
                       else ans[x][y]=search(i,j);
     }
     return ans[x][y];
}

void calc()
{
     int i,j,k;
     char c;
     
     for (i=1;i<=h;i++)      
     {
         for (j=1;j<=w;j++)
         {
                      if (ans[i][j]==0)  {ans[i][j]=search(i,j);}
                      c='a';c+=ans[i][j]-1;
                      if (j!=1) fout<<" ";
                      fout<<c;
         }
         fout<<endl;
     }
}

int main()
{
    int i,j,k;
    
    fin>>n;
    for (i=1;i<=n;i++)
    {
        fin>>h>>w;
        memset(ans,0,sizeof(ans));memset(a,0,sizeof(a));       
        
        num=0;
        for (j=1;j<=h;j++)        
            for (k=1;k<=w;k++) fin>>a[j][k];
        
        fout<<"Case #"<<i<<":"<<endl;
        calc();
    }    
//    cin>>n;
    return 0;
}
