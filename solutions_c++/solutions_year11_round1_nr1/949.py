#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <algorithm>
#include <memory.h>

using namespace std;
#define MAXN 1100
long long int N, pd, pg;

int main()
{
	int cases;
	int casenum = 1;
	freopen("test", "r", stdin);
	freopen("output", "w", stdout);
	scanf("%d", &cases);
	while(cases--)
	{
		scanf("%lld%lld%lld", &N, &pd, &pg);
		if(pg == 100 && pd != 100){
			printf("Case #%d: Broken\n", casenum++);
			continue;
		}
		if(pg == 0 && pd != 0){
			printf("Case #%d: Broken\n", casenum++);
			continue;
		}

		bool isok = false;
		if(N < 100){
			for(int i = 1;i <= N; i++){
			//	cout<<i<<" = "<<(i * pd) % 100<<endl;
				if((i * pd) % 100 != 0)continue;
				isok = true;
			}
		}else{
			isok = true;
		}

		if(isok)
			printf("Case #%d: Possible\n", casenum++);
		else
			printf("Case #%d: Broken\n", casenum++);
	}
	return 0;
}

