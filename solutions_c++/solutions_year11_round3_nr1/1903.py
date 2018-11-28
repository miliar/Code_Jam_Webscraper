#include<iostream>
#include<fstream>
using namespace std;
int main()
{
char ar[100][100];
int p,p1,i,j,n,c;
ofstream fout("output.txt");
ifstream fin("input.txt");
fin>>p;
for(p1=1;p1<=p;p1++)
{
fin>>n>>c;
fout<<"Case #"<<p1<<":\n";
for(i=0;i<n;i++)
{
for(j=0;j<c;j++)
{
fin>>ar[i][j];
ar[i+1][j]='.';
ar[i][j+1]='.';
ar[i+1][j+1]='.';
}
}
for(i=0;i<n;i++)
{
for(j=0;j<c;j++)
{
if(ar[i][j]=='#')
{
if(ar[i+1][j+1]=='#' && ar[i][j+1]=='#' && ar[i+1][j]=='#')
{
ar[i+1][j+1]='/' ;
ar[i][j]='/' ;
ar[i+1][j]='\\' ;
ar[i][j+1]='\\' ;
j+=1;
}
else
{
fout<<"Impossible\n";
goto p;
}
}
}
}
for(i=0;i<n;i++)
{
for(j=0;j<c;j++)
{
fout<<ar[i][j];
}
fout<<'\n';
}
p:;

}
return(0);
}
