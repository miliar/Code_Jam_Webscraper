//Author : Nitin Gangahar
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <iostream>
#include <cstring>
#include <set>
#define F first
#define S second
#define mp make_pair
#define pb push_back
#define isok(x,y) (x>=0 && x<R && y>=0 && y<C)
#define MAX 16

using namespace std;

typedef pair<int,int> PII;
typedef vector<int> VI;
typedef vector< VI > VII;
vector<int> A;
int main()
{
	int T;
	scanf("%d",&T);
	int cases = 1;
	while(T--)
	{
		int N;
		int ans = 0;
		scanf("%d",&N);
		int xorval = 0;
		A.resize(0);A.resize(N);
		for(int i=0;i<N;i++)
		{
			scanf("%d",&A[i]);
			xorval = xorval ^ A[i];
		}
		if(xorval != 0)
		{
			printf("Case #%d: NO\n",cases++);
			continue;
		}
		sort(A.begin(),A.end());
		for(int i=1;i<N;i++)
			ans += A[i];
		printf("Case #%d: %d\n",cases++,ans);
	}
	return 0;
}
