#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
/*
inline bool prime(int n)
{
	if(n<=1)	return false;
	if(n==2||n==3)	return true;
	int k=sqrt(double(n));
	for(int i=2;i<=k;++i)
		if(n%i==0)	return false;
	return true;
}
*/
int main()
{
	int T;
	int n,k;
	scanf("%d",&T);
	for(int t=1;t<=T;++t){
		scanf("%d%d",&n,&k);
		long long p = 0;
		for(int i=0;i<n;++i)	p = p*2+1;
		if((long long )(k+1)%(p+1) == 0)		printf("Case #%d: ON\n",t);
		else		printf("Case #%d: OFF\n",t);
	}
	return 0;
}