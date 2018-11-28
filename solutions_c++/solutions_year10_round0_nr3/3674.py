#include<iostream>
#include<fstream>
using namespace std;
main()
{
ifstream fin;
ofstream fout;
fin.open("C-small-attempt1.in");
fout.open("output1.in");
int t,r,k,n,g[10],profit=0;
fin>>t;
int s;
for(int i=0;i<t;i++)
	{
	profit=0;
	fin>>r>>k>>n;
	for(int j=0;j<n;j++)
		{
		fin>>g[j];
		}
	for(int l=0;l<r;l++)
		{
		int w=k;
		for(int m=0,c=0;c<n;c++)
			{
			if(g[m]>w)
				break;
			s=g[0];
			profit=profit+g[m];
			w=w-g[m];
			int a;
			for(a=0;a<n;a++)
				{
				g[a]=g[a+1];
				}
			g[a-1]=s;
			}
		}
	fout<<"Case #"<<(i+1)<<": "<<profit<<endl;
	}
return 0;
}
