#include<fstream>
#include<iostream>
using namespace std;

int main()
{
	int T,C,D,N,nerv;
	int n,m,p,j,prim,i;
	char x[40][7],d[33][5],r[105];
	ifstream fin("problema.in");
	ofstream fout("probleme.out");
	fin>>T;
	nerv=T;
	while(T)
	{
		T--;
		fin>>C;
		prim=1;
		n=0;
		m=0;
		p=0;
		while(C)
		{
			n++;
			fin>>x[n][1]>>x[n][2]>>x[n][3];
			C--;
		}
		fin>>D;
		while(D)
		{
			m++;
			fin>>d[m][1]>>d[m][2];
			D--;
		}
		fin>>N;
		while(N)
		{
			p++;
			fin>>r[p];
			N--;
			if(p>1)
			{
				for(j=1;j<=n;j++)
					if(((r[p-1]==x[j][1]) && (r[p]==x[j][2])) || ((r[p-1]==x[j][2]) && (r[p]==x[j][1])))
				{
					p--;				
					r[p]=x[j][3];
				}
				for(j=1;j<p;j++)
				{	for(i=1;i<=m;i++)
					{
				if(((r[p]==d[i][1]) && (r[j]==d[i][2])) || ((r[j]==d[i][1]) && (r[p]==d[i][2])))
					p=0;
				}}
			}
		}			
		fout<<"Case #"<<nerv-T<<":"<<" [";
		for(j=1;j<=p;j++)
		{
		fout<<r[j];
			if(j<p)
				fout<<", ";
		}
		fout<<"]";
		fout<<endl;
	}
	fin.close();
	fout.close();
	return 0;
}
