#include <string.h>
#include <sstream>
#include <string>
#include <map>
#include <queue>
#include <vector>
#include <set>
#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;
#define ll long long

int a[100000];

int main()
{
	int T;
	scanf("%d",&T);
	for(int c =0;c<T;)
	{
		int n;
		scanf("%d",&n);
		double cnt = 0;
		for(int i=0;i<n;++i)
		{
			scanf("%d",&a[i]);
			if( a[i] != i+1 )
				cnt += 1.0;
		}
		printf("Case #%d: %.9lf\n",++c,cnt);
	}
}

