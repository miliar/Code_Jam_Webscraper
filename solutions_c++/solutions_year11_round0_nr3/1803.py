#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>

using namespace std;

typedef pair<int, int> PII;

typedef vector<int> VI;
typedef vector<vector<int> > VII;
typedef vector<PII> VPII;

typedef vector<double> VD;
typedef vector<string> VS;

typedef long long LL;

int main(){ 	
	int cases;
	scanf("%d\n", &cases);
	
	for(int caseNr = 1; caseNr <= cases; caseNr++){
		// go for it!	
		printf("Case #%d: ", caseNr);
		
		
		// READ
		int N;
		scanf("%d", &N);
		
		int candies[N];
		bool seans[N];
		memset(seans, false, sizeof(seans));
		for(int i=0;i<N;i++){
			scanf("%d", &candies[i]);
		}
		
		sort(candies, candies+N);
		
		// does he cry?
		int temp = 0;
		for(int j=0;j<N;j++)
			temp ^= candies[j];
		if (temp != 0){
			printf("NO\n");
			continue; // we're finished
		}
		
		// do it greedy
		for(int i=N-1;i>=0;i--){
			// try to steal the i-th candy
			
			int pileSean = 0, pilePatrick = 0;
			
			// is only one left?
			if(i==0){
				LL sum = 0;
				for(int k=0;k<N;k++)
					if(!seans[k] && k!=i)
						sum += candies[i];
				if(sum <= 0)
					break;
			}
			
			// does patrick cry?
			for(int j=0;j<N;j++){			
				if(j == i || seans[i])
					pileSean ^= candies[j];
				
				else
					pilePatrick ^= candies[j];
			}
			
			// no? then be bad and steal
			if(pileSean == pilePatrick)
				seans[i] = true;
		}
		
		// count all my candies *muahahaha*
		LL sum = 0;
		for(int i=0;i<N;i++)
			if(seans[i])
				sum += candies[i];
			
		printf("%Ld\n", sum);
		
		fflush(stdout);
	}
	
	return 0;
}
