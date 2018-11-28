#include <cstdio>
#include <iostream>
#include <cstdlib>
#include <ctime>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <deque>
#include <list>
#include <vector>
#include <cstring>
using namespace std;
typedef unsigned U;
typedef long long LL;
typedef unsigned long long UL;
typedef long double LD;

const int K = 16;
const int N = 100*1000;

int n,k;
int p[K];
char s[N],w[N];

void single_case(int cas)
{
	int best = N;
	scanf("%d",&k);
	scanf("%s",s);
	n = strlen(s);
	
	for (int i=0; i<k; i++) p[i]=i;
	do
	{
		for (int i=0; i<n/k; i++)
		{
			for (int j=0; j<k; j++)
				w[i*k+j]=s[i*k+p[j]];
		}
		int c=1;
		for(int i=1; i<n; i++)
			c+=(w[i]!=w[i-1]);
		best = min(best,c);
	}while(next_permutation(p,p+k));

	printf("Case #%d: %d\n",cas,best);
}


int main()
{
	int j;
	scanf("%d",&j);
	for (int i=0; i<j; i++)
		single_case(i+1);
	return 0;
}

