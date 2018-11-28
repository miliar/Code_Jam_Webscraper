#include <algorithm>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
//#include <cmath>
//#include "lcgrand.c"

using namespace std;

const int nmax=501;
const int MOD=100003;

int ans[nmax][nmax];
long long C[nmax][nmax];

int main()
{

	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);

	int T,n,i,j;

	C[0][0]=1;
	for(i=1;i<nmax;i++)
	{
		C[i][0]=1;
		for(j=1;j<=i;j++) C[i][j]=(C[i-1][j-1]+C[i-1][j])%MOD;
	}

	ans[1][0]=1;
	for(n=2;n<nmax;n++)
	{
		for(i=1;i<n;i++)
			for(j=0;j<i;j++) ans[n][i]=(ans[n][i]+C[n-i-1][i-j-1]*ans[i][j])%MOD;
	}
	
	cin>>T;
	for(int t=1;t<=T;t++)
	{
		cin>>n;
		int ret=0;
		for(i=0;i<n;i++) ret=(ret+ans[n][i])%MOD;
		printf("Case #%d: %d\n",t,ret);
	}
	

	return 0;
}