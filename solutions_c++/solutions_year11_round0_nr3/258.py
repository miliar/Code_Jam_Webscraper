#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

int v[1000];

int main(int argc, char* argv[])
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
#endif
	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		

		int N;
		scanf("%d", &N);

		for (int i = 0; i < N; i++)
			scanf("%d", &v[i]);

		int res = 0;
		for (int i = 0; i < N; i++)
			res ^= v[i];

		printf("Case #%d: ", nTest);

		if (res != 0)
		{
			printf("NO\n");
		}
		else
		{
			res = accumulate(v, v + N, 0) - *min_element(v, v + N);
			printf("%d\n", res);
		}
	}

	return 0;
}


