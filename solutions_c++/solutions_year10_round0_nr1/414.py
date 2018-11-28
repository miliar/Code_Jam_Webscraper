//We believe ourselves
#include "cstdlib"
#include "cctype"
#include "cstring"
#include "cstdio"
#include "cmath"
#include "algorithm"
#include "vector"
#include "string"
#include "set"
#include "map"
#include "iostream"
#include "sstream"
#include "queue"
using namespace std;
__int64 p[32];

int main()
{

	freopen("D:\\A-large.in","r",stdin);
	freopen("D:\\A-large.out","w",stdout);

	__int64 n,k;
	__int64 t;
	int ca=0;
	n=1;
	p[0]=1;
	for(t=1;t<32;t++)
	{
		p[t]=n*2;
		n=n*2;
	}

	scanf("%I64d",&t);
	while(t--)
	{
		ca++;
		scanf("%I64d%I64d",&n,&k);
		printf("Case #%d: ",ca);
		k=k%(p[n]);
		
		if(k==p[n]-1)
			printf("ON\n");
		else
			printf("OFF\n");
	}
	return 0;
}