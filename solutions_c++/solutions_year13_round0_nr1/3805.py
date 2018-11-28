#include <cstdio>
#include <cmath>
#include <cctype>
#include <string>
#include <algorithm>
#include <vector>
#include <iostream>
#include <stack>
#include <cstring>
#include <cstdlib>
#include <queue>
#include <map>
using namespace std;
typedef long long ll;

int main()
{
          freopen("A-large.in","r",stdin);
          freopen("G13out.txt","w",stdout);
          long i,j,T,res,c,hang[5],cot[5],b[101][101],dg1,dg2,ok;
          char a[101][101];
          
          cin>>T;
          for (c=1; c<=T; c++){
                    res=0; ok=0; dg1=0; dg2=0;
          for (i=1; i<=4; i++)
          {
                    hang[i]=0;
                    cot[i]=0;
                    for (j=1; j<=4; j++)
                    {
                              cin>>a[i][j];
                              if (a[i][j]=='O') {b[i][j]=-100;}
                              else if (a[i][j]=='X') {b[i][j]=100;}
                              else if (a[i][j]=='T') {b[i][j]=1;}
                              else if (a[i][j]=='.') {b[i][j]=10000;ok=20;}
                    }
                    
          }
          for (i=1; i<=4; i++)
          {
                    for (j=1; j<=4; j++)
                    {
                              hang[i]+=b[i][j];
                              cot[j]+=b[i][j];
                    }
          }
           dg1=b[1][1]+b[2][2]+b[3][3]+b[4][4];
           dg2=b[4][1]+b[3][2]+b[2][3]+b[1][4];
          for (i=1; i<=4; i++)
          {
                    if ((hang[i]>300) && (hang[i]<9000)) {res=1; }
                    else if (hang[i]<-298) {res=-1;}
                    if ((cot[i]>300) && (cot[i]<9000)) {res=1; }
                    else if (cot[i]<-298) {res=-1;};
          }
          if ((dg1>300) && (dg1<9000)) res=1; else if (dg1<-298) res=-1;
             if ((dg2>300) && (dg2<9000)) res=1; else if (dg2<-298) res=-1;
          cout<<"Case #"<<c<<": ";
          if (res==1) {cout<<"X won";}
          else if (res==-1) {cout<<"O won";}
          else if (ok!=20) cout<<"Draw"; else cout<<"Game has not completed";
          cout<<endl;
          }
          //system("pause");     
          return 0;
}
