#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("a.in");
ofstream fout("b.txt");
int n,v[1001];

void citire()
{int i;fin>>n;
for(i=1;i<=n;i++)
	fin>>v[i];}

int suma()
{int s=0;
for(int i=1;i<=n;i++)
	s+=v[i];return s;}

int min()
{int min=1000000;
for(int i=1;i<=n;i++)
if(min>v[i]) min=v[i];
return min;}
	
void rez()
{int a=0,i;
for(i=1;i<=n;i++)
a=a^v[i];
if(a) fout<<"NO";
else fout<<suma()-min();}

int main()
{int m,i;
fin>>m;
	for(i=1;i<=m;i++)
	{citire();
	fout<<"Case #"<<i<<": ";rez();fout<<"\n";}
	fin.close();
	fout.close();
	return 0;
}
