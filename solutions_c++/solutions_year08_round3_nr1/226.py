#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define max(a,b) (((a)>(b))?(a):(b))
#define min(a,b) (((a)<(b))?(a):(b))

int val[2000];

bool minCmp(int a,int b)
{
	return a < b;
}
bool maxCmp(int a,int b)
{
	return a > b;
}
int main()
{
	int C;
	int n,i;
	int P,K,L;
	int j;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	while (scanf("%d",&C) != EOF) {
		for (int p = 1; p <= C; p ++) {

			scanf("%d%d%d",&P,&K,&L);

			for (i = 0; i < L; i ++) {
				scanf("%d",&val[i]);
			}

			sort(val,val+L,maxCmp);

			int base = 1;

			__int64 ans = 0;

			for (i = 0; i < L; i += K) {

				for (j = i; j < i + K && j < L; j ++) {

					ans += base * val[j];
				}

				//printf("%d\n",ans);

				base ++;
			}

			printf("Case #%d: %I64d\n",p,ans);


		}
	}

	return 0;
}

