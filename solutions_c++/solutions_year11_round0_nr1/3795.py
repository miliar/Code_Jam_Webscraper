#include <fstream>
#include <iostream>
#include <cstdio>
#include <cmath>
using namespace std;

int main()
{
	int vcount[2];
	int vcur[2];
	int vdst[2];
	ifstream fin("B-small-attempt0.in");
	ofstream fout("A-samll-attmept0.out");
	int T;
	fin>>T;
	for(int i=1;i<=T;i++)
	{
		for(int k=0;k<2;k++)
		{
			vcount[k]=0;
			vdst[k]=0;
			vcur[k]=1;
		}
		int total=0;
		int idst;
		char ccolor;
		int icolor;
		
		int size;
		fin>>size;
		int pre=2;
		for(int j=1;j<=size;j++)
		{
			fin>>ccolor>>idst;
			if(ccolor=='O')icolor=0;
			if(ccolor=='B')icolor=1;
			vdst[icolor]=idst;
			int dist=abs(vdst[icolor]-vcur[icolor]);

			if(pre!=icolor)
			{	
				if(dist<=vcount[1-icolor])
					vcount[icolor]=1;
				else
					vcount[icolor]=dist-vcount[1-icolor]+1;
				total+=vcount[icolor];
				vcur[icolor]=idst;
			}
			else
			{
				vcount[icolor]+=dist+1;
				total+=dist+1;
				vcur[icolor]=idst;
			}
			pre=icolor;
		}
		fout<<"Case"<<' '<<'#'<<i<<':'<<' '<<total<<endl;
	}
	return 0;
}