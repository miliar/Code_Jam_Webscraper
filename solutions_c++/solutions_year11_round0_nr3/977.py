#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <cassert>
#include <string>
#include <cmath>
#include <iostream>
#include <stack>
#include <queue>
#include <ctime>
#include <utility>
#include <bitset>
#include <memory.h>
#include <list>
#include <deque>

using namespace std;

int main()
{
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int z = 0; z < T; z++)
	{
		int N;
		scanf("%d",&N);
		vector<int> A;
		
		int res = 0;
		for(int i = 0; i < N; i++){
			int p;
			scanf("%d",&p);
			res ^= p;
			A.push_back(p);
		}
		sort(A.begin(),A.end());

		if(res==0)
		{
			int sum = 0;
			for(int i = 1; i < N; i++)
				sum += A[i];
			printf("Case #%d: %d\n",z+1,sum);
		}
		else
			printf("Case #%d: NO\n",z+1);
	}
	return 0;
}