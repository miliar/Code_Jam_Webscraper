#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#include<fstream>
using namespace std;
int main()
{
ifstream fin("test.in");
ofstream fout("test3.out");
int t,i,j,k;
fin>>t;
//char a;
//fin>>a;
for(k=1;k<=t;k++)
{
int flagX=0,flag_X=0,flagO=0,flag_O=0,flag=0,O=0,X=0,dot=0;
vector< vector<char> > a(4,vector<char>(4));
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
fin>>a[i][j];
if(a[i][j]=='X')
flagX+=1;
else
if(a[i][j]=='O')
flagO+=1;
else
if(a[i][j]=='T')
flag=1;
}
if(flagX==4 || (flagX==3 && flag==1))
X=1;
else
if(flagO==4 || (flagO==3 && flag==1))
O=1;
flagX=flagO=flag=0;
}
for(j=0;j<4;j++)
{
for(i=0;i<4;i++)
{
if(a[i][j]=='X')
flagX+=1;
else
if(a[i][j]=='O')
flagO+=1;
else
if(a[i][j]=='T')
flag=1;
else
dot++;
}
if(flagX==4 || (flagX==3 && flag==1))
X=1;
else
if(flagO==4 || (flagO==3 && flag==1))
O=1;
flagX=flagO=flag=0;
}
for(j=0,i=0;j<4;j++,i++)
{
if(a[i][j]=='X')
flagX+=1;
else
if(a[i][j]=='O')
flagO+=1;
else
if(a[i][j]=='T')
flag=1;
}
if(flagX==4 || (flagX==3 && flag==1))
X=1;
else
if(flagO==4 || (flagO==3 && flag==1))
O=1;
flagX=flagO=flag=0;
for(i=0,j=3;i<4;i++,j--)
{
if(a[i][j]=='X')
flagX+=1;
else
if(a[i][j]=='O')
flagO+=1;
else
if(a[i][j]=='T')
flag=1;
}
if(flagX==4 || (flagX==3 && flag==1))
X=1;
else
if(flagO==4 || (flagO==3 && flag==1))
O=1;
flagX=flagO=flag=0;

if(X==1)
fout<<"Case #"<<k<<": "<<"X won"<<endl;
else
if(O==1)
fout<<"Case #"<<k<<": "<<"O won"<<endl;
else
if(dot>0)
fout<<"Case #"<<k<<": "<<"Game has not completed"<<endl;
else
fout<<"Case #"<<k<<": "<<"Draw"<<endl;

}

}
