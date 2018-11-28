#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <math.h>
#pragma comment (linker,"/STACK:16000000")
using namespace std;
bool func(int n, int k)
{
	int i;
	if (k==0)
		return false;
	int st = (1 << n) - 1;
	if ( (st & k) == st )
		return true;
	else return false;
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int i,j,n,t,k;
	scanf("%d",&t);
	for (int q=1;q<=t;++q)
	{
		scanf("%d %d",&n,&k);
		printf("Case #%d: ",q);
		if (func(n,k))
			printf("ON\n");
		else printf("OFF\n");
	}

	return 0;
}