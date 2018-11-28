#include <cstdio>
#include <iostream>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <cstring>
#include <string>
#include <vector>
#include <set>
#include <map>
using namespace std;

int main()
{
#ifndef ONLINE_JUDGE
	freopen("input1.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif
	int n,i,k,t;
	scanf("%d",&t);
	for (i=0; i<t; ++i)
	{
		scanf("%d%d",&n,&k);
		printf("Case #%d: ",i+1);
		if ((k+1)%(1<<n)==0) printf("ON\n");
		else printf("OFF\n");
	}
	return 0;
}