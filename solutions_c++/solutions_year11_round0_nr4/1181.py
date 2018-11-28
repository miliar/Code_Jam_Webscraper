// 2011_1.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int chainlen(vector<int> & v, int s)
{
	int res = 0;
	while(v[s])
	{
		res++;
		int save = s;
		s = v[s]-1;
		v[save] = 0;
	}
	if(res == 1) res = 0;
	return res;
}

double fac(int n)
{
	double res = 1;
	for(int i = 1; i<=n; i++)
		res *= i;
	return res;
}

vector<vector<double>> circlecount(2000);

vector<double> getCircleCount(int n)
{
	vector<double> res(n+1);
	vector<double> src = circlecount[n-1];
	for(int i = 1; i<= n-1; i++)
		res[i] = src[i]+src[i-1]*(i-1);
	res[n] = fac(n-1);
	res[1] = fac(n);
	return res;
}




double mid_chain[2000];

double getChainMoveCount(int n)
{
	double res = 0;
	double numTest = fac(n);
	double numself = fac(n-1);
	for(int i = 1; i<n; i++)
		res += mid_chain[i]*circlecount[n][i];

	res += fac(n)-numself;
	res = (numself+res)/(numTest-numself);
	return res;
}


int _tmain(int argc, _TCHAR* argv[])
{
	
	/*circlecount.resize(2000);
	circlecount[1].resize(2);
	circlecount[1][1] = 1;

	for(int i = 2; i<1002; i++)
		circlecount[i] = getCircleCount(i);

	mid_chain[0] = 0;
	mid_chain[1] = 0;
	
	for(int i = 2; i<2000; i++)
	{
		mid_chain[i] = getChainMoveCount(i);
		printf("%f\n",mid_chain[i]);
	}*/

	FILE * in	= fopen("D-large.in","rt");
	FILE * out	= fopen("out_large.txt","wt");

	int n;
	fscanf(in,"%d\n",&n);
	for(int i = 0; i<n; i++)
	{
		int k;
		fscanf(in,"%d\n",&k);
		vector<int> candies;
		for(int i = 0; i<k; i++)
		{
			int c;
			fscanf(in,"%d ",&c);
			candies.push_back(c);
		}
		double res = 0;
		for(int i = 0; i<k; i++)
			res += chainlen(candies,i);
		fprintf(out,"Case #%d: %.6f\n",i+1,res);
	}
	fclose(in);
	fclose(out);
	return 0;
}

