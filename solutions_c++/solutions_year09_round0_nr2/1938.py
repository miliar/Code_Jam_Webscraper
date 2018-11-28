#include <iostream>
#include <fstream>

using namespace std;

ifstream ci("in");
ofstream co("out");

int N,map[100][100],e[100][100],ch[100][100];
int x,y;

int search(int a,int b)
{
	int n,w,ea,s;
	n=(a>0)?map[a-1][b]:100000;
	w=(b>0)?map[a][b-1]:100000;
	s=(a<x-1)?map[a+1][b]:100000;
	ea=(b<y-1)?map[a][b+1]:100000;
	if ((n<=w)&&(n<=ea)&&(n<=s)&&(n<map[a][b]))
		e[a][b]=(e[a-1][b]==-1)?search(a-1,b):e[a-1][b];
	if ((w<n)&&(w<=ea)&&(w<=s)&&(w<map[a][b]))
		e[a][b]=(e[a][b-1]==-1)?search(a,b-1):e[a][b-1];
	if ((ea<n)&&(ea<w)&&(ea<=s)&&(ea<map[a][b]))
		e[a][b]=(e[a][b+1]==-1)?search(a,b+1):e[a][b+1];
	if ((s<n)&&(s<w)&&(s<ea)&&(s<map[a][b]))
		e[a][b]=(e[a+1][b]==-1)?search(a+1,b):e[a+1][b];
	if (e[a][b]==-1)
		e[a][b]=a*y+b;
	return e[a][b];
}

int main()
{
	ci>>N;
	for (int i=0;i<N;++i)
	{
		ci>>x>>y;
		int m=0;
		for (int j=0;j<x;++j)
			for (int k=0;k<y;++k)
			{
				ci>>map[j][k];
				e[j][k]=-1;
				ch[j][k]=-1;
			}
		for (int j=0;j<x;++j)
			for (int k=0;k<y;++k)
			if (e[j][k]==-1)
		      search(j,k);
		co<<"Case #"<<i+1<<":"<<endl;
		for (int j=0;j<x;++j)
		{
			for (int k=0;k<y;++k)
				if (ch[int(e[j][k]/y)][e[j][k]%y]==-1)
				{
					ch[int(e[j][k]/y)][e[j][k]%y]=m;
					co<<char(m+97)<<" ";
					++m;
				}
				else
					co<<char(ch[int(e[j][k]/y)][e[j][k]%y]+97)<<" ";
			co<<endl;
		}
	};
}