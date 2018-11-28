#include "stdafx.h"
#include <set>
#include <string>
#include <vector>
#include <iostream>
using namespace std;

const int modulo=10000;

int N;
string T,S="*welcome to code jam";
int d[550][25],calced[550][25];

int calc(int i,int j)
{
	if (i<j)
		return 0;
	if ( (i<0) || (j<0) )
		return 0;
	if (calced[i][j])
		return d[i][j];
	d[i][j]=calc(i-1,j)%modulo;
	if (T[i]==S[j])
		d[i][j]=(d[i][j]+calc(i-1,j-1))%modulo;
	calced[i][j]=1;
	return d[i][j];
}

int main()
{

	freopen("A-small.in","rt",stdin);
	freopen("A-small.out","wt",stdout);

	scanf("%d\n",&N);
	for(int i=0;i<N;i++)
	{
		getline(cin,T);
		T="*"+T;
		memset(calced,0,sizeof(calced));
		memset(d,0,sizeof(d));
		d[0][0]=1;
		calced[0][0]=1;
		int ans=calc(T.length()-1,S.length()-1);
		printf("Case #%d: %04d\n",i+1,ans);
	}
	
	return 0;
}