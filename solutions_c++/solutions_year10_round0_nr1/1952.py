#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
using namespace std;

const int two[32]={1,2,4,8,16,32,64,128,256,512,1024,2048,4096,8192, 16384, 32768,65536, 
131072,262144,524288,1048576, 2097152, 4194304,8388608,16777216, 33554432, 67108864, 
134217728, 268435456, 536870912, 1073741824,2147483648};

int n,t,k;

int main()
{
	freopen("input.txt","r", stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&t);
	for (int q=1; q<=t; q++)
	{
		scanf("%d %d",&n, &k);
		if ((k%two[n])==two[n]-1) printf("Case #%d: ON\n", q);
		else printf("Case #%d: OFF\n", q);
	}
	return 0;
}