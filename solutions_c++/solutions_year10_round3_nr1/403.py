#include <cstdio>
#include <cstdlib>
#include <string>
#include <cmath>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <stack>
using namespace std;

int frm [1020];
int too [1020];

int main()
{
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int tt;
	scanf("%d",&tt);
	for ( int t = 1; t<=tt ; t++)
	{
		int n;
		scanf("%d",&n);
		for ( int i = 0 ; i < n ; i ++ )
			scanf("%d %d", &frm[i] , &too[i]);
		int cnt = 0;
		for ( int i = 0 ; i < n ; i ++ )
			for ( int j = 0 ; j < n ; j ++ )
				if ( frm[i] > frm [j] && too [i] < too[j] )
					cnt++;
		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}
