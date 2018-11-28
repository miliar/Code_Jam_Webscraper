#include <iostream>
#include <string>
#include <fstream>
#include <stdlib.h>
using namespace std;
long long i,j,k,x,y,z,n,m,mx,mn,p,d,t;
char a[10][10];
void ghnc(int h)
{
p=0;
for (i=1; i<=4; i++)
for (j=1; j<=4; j++)
if (a[i][j]=='.')  {p=3; break;}
if (p==0) p=4;
}
void owon(int h)
{
p=0;
x=0;
t=0;
for (i=1; i<=4; i++)
{
for (j=1; j<=4; j++)
if (a[i][j]=='O') x++; else 
if (a[i][j]=='T') t++;
if ((x+t==4) && (t<=1)) {p=2; break;}
x=0;
t=0;
}
if (p==0)
{
x=0;
t=0;
for (i=1; i<=4; i++)
{
for (j=1; j<=4; j++)
if (a[j][i]=='O') x++; else 
if (a[j][i]=='T') t++;
if ((x+t==4) && (t<=1)) {p=2; break;}
x=0; t=0;
}}
if (p==0)
{
for (i=1; i<=4; i++)
if (a[i][i]=='O') x++; else 
if (a[i][i]=='T') t++;
if ((x+t==4) && (t<=1)) {p=2; }
x=0; t=0;        
}
if (p==0)
{
for (i=1; i<=4; i++)
if (a[i][4-i+1]=='O') x++; else 
if (a[i][4-i+1]=='T') t++;
if ((x+t==4) && (t<=1)) {p=2; }
x=0; t=0;
}
if (p==0) ghnc(1);     
}
void xwon(int h)
{
p=0;
x=0;
t=0;
for (i=1; i<=4; i++)
{
for (j=1; j<=4; j++)
if (a[i][j]=='X') x++; else 
if (a[i][j]=='T') t++;
if ((x+t==4) && (t<=1)) {p=1; break;}
x=0;
t=0;
}
if (p==0)
{
x=0;
t=0;
for (i=1; i<=4; i++)
{
for (j=1; j<=4; j++)
if (a[j][i]=='X') x++; else 
if (a[j][i]=='T') t++;
if ((x+t==4) && (t<=1)) {p=1; break;}
x=0; t=0;
}}
if (p==0)
{
for (i=1; i<=4; i++)
if (a[i][i]=='X') x++; else 
if (a[i][i]=='T') t++;
if ((x+t==4) && (t<=1)) {p=1;}
x=0; t=0;        
}
if (p==0)
{
for (i=1; i<=4; i++)
if (a[i][4-i+1]=='X') x++; else 
if (a[i][4-i+1]=='T') t++;
if ((x+t==4) && (t<=1)) {p=1; }
x=0; t=0;
}
if (p==0) owon(1);
}
main()
{
freopen ("A-large.in","r",stdin);
freopen ("output.txt","w",stdout);
cin>>n;
for (k=1; k<=n; k++)
{
for (i=1; i<=4; i++)
for (j=1; j<=4; j++)
cin>>a[i][j];
cout<<"Case #"<<k<<": ";    
p=0;
xwon(1);
if (p==1) cout<<"X won"<<endl; else
if (p==2) cout<<"O won"<<endl; else
if (p==3) cout<<"Game has not completed"<<endl; else
cout<<"Draw"<<endl;
}
}
