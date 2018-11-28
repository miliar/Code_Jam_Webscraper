/*Written by Vladimir Ignatiev aka Neacher (neacher@gmail.com)*/
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <iostream>

using namespace std;

int N;
int a[200][200];

double wp(int cur)
{	
	int nTotal=0;
	int nWin=0;
	double WP=0;
	

	for(int j=0;j<N;j++)
		if(a[cur][j]!=-1)
		{
			nTotal++;
			if(a[cur][j]) nWin++;
		}

	if(nTotal) WP=(double)nWin/nTotal;
	return WP;
}

double owp(int cur)
{	
	int nTotal=0;
	int nTotal2=0;
	int nWin=0;
	double OWP=0;

	for(int i=0;i<N;i++)
	{
		if(i==cur) continue;
		nTotal=0;
		nWin=0;
		if(a[cur][i]!=-1)
		{
			nTotal2++;
			for(int j=0;j<N;j++)
			{
				if(j==cur) continue;
				if(a[i][j]!=-1)
				{
					nTotal++;
					if(a[i][j]) nWin++;
				}
			}
			if(nTotal) OWP+=(double)nWin/nTotal;
		}
	}
	OWP/=(double)nTotal2;
	return OWP;
}

int main()
{
	FILE* In=fopen("A.in","r");if(!In) return 1;
	FILE* Out=fopen("A.res","w");if(!Out) return 2;

	int nCount;
	char c;
	vector<double> WP;
	vector<double> OWP;

	fscanf(In,"%d",&nCount);

	for(int n=0;n<nCount;n++)
	{
		fprintf(Out,"Case #%d:\n",n+1);
		printf("%d\n",n);
		fscanf(In,"%d%*[ \n\t]",&N);
		for(int i=0;i<N;i++)
		{
			for(int j=0;j<N;j++)
			{
				fscanf(In,"%c%*[ \n\t]",&c);
				if(c=='1') a[i][j]=1;
				else
					if(c=='0') a[i][j]=0;
					else a[i][j]=-1;
			}
		}

		WP.clear();
		OWP.clear();
		for(int i=0;i<N;i++)
		{
			WP.push_back(wp(i));
			OWP.push_back(owp(i));
		}

		
		for(int i=0;i<N;i++)
		{
			double SumOWP=0;
			int nTotal=0;
			for(int j=0;j<N;j++)
			{
				if(j==i) continue;
				if(a[i][j]!=-1) {SumOWP+=OWP[j];nTotal++;}
			}
			double RPI=0.25*WP[i]+0.5*OWP[i]+0.25*SumOWP/(double)nTotal;
			fprintf(Out,"%.6f\n",RPI);
		}
	};

	fclose(In);
	fclose(Out);
	return 0;
}