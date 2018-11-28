#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

char a[110][110];
int nr[110],dr[110];
double wp[110],owp[110],oowp[110];

int main()
{
	int cases,n;
	double rpi;
	scanf("%d",&cases);
	FILE* pFile=fopen("11.out","w");
	for(int c=1;c<=cases;c++)
	{
		scanf("%d",&n);
		for(int i=0;i<n;i++) scanf("%s",a[i]);
		for(int i=0;i<n;i++)
		{
			nr[i]=dr[i]=0;
			for(int j=0;j<n;j++)
				if(a[i][j]=='1') {nr[i]++;dr[i]++;}
				else if(a[i][j]=='0') dr[i]++;
			wp[i]=(double)nr[i]/(double)dr[i];
		}
		for(int i=0;i<n;i++)
		{
			double avg=0.00;
			int m=n-1;
			for(int j=0;j<n;j++)
				if(j==i) continue;
				else
				{
					if(a[j][i]=='.') {m--;continue;}
					else if(a[j][i]=='0') avg+=(double)nr[j]/(double)(dr[j]-1);
					else avg+=(double)(nr[j]-1)/(double)(dr[j]-1);
				}
			if(m==0) owp[i]=0;
			else owp[i]=(double)avg/(double)(m);
		}
		for(int i=0;i<n;i++)
		{
			double avg=0.00;
			int m=n-1;
			for(int j=0;j<n;j++)
				if(i==j) continue;
				else if(a[i][j]=='.') {m--;continue;} 
				else avg+=owp[j];
			if(m==0) oowp[i]=0;
			else oowp[i]=avg/(double)m;
		}
		fprintf(pFile,"Case #%d:\n",c);
		for(int i=0;i<n;i++)
		{
			rpi=0.25*wp[i]+0.50*owp[i]+0.25*oowp[i];
			fprintf(pFile,"%.12lf\n",rpi);
		}
	}
	return 0;
}