#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>

using namespace std;

long long candies[1010],preSum[1010], preXor[1010];
long long SeanXor=0, PatXor=0, totXor=0, totSum=0, SeanSum=0, PatSum=0, tmp=0, maxsum = -111;

int main() { 

	int tc, n;

	scanf("%d",&tc);

	for(int k=0; k<tc; k++) {

		totXor = 0;	totSum = 0;
		maxsum = -111;

		scanf("%d",&n);

		for(int i=0; i<n; i++) { 
			scanf("%lld",&candies[i]);
		}
	
		vector<long long> can(candies,candies+n);
		sort(can.rbegin(),can.rend());

		int len = can.size();
		for(int i=0;i<len;i++) { 
			totXor ^= can[i];
			totSum += can[i];
		}

		preSum[0] = can[0]; preXor[0] = can[0];
		for(int i=1;i<len;i++) { 
			preXor[i] = preXor[i-1] ^ can[i];
			preSum[i] = preSum[i-1] + can[i];
		}

		for(int i=0;i<len-1;i++) { 
			if(preXor[i] == ( preXor[len-1] ^ preXor[i] )){ 
				tmp = max(preSum[i],preSum[len-1]-preSum[i]);
				if(tmp > maxsum) maxsum = tmp;
			}
		}
		printf("Case #%d: ",k+1);
		maxsum == -111 ? puts("NO") : printf("%lld\n",maxsum);

	}//tc
		
	return 0;	
}
