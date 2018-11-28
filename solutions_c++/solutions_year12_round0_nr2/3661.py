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
		
		// init
		int N, S, p;
		int t[101];
		
		// read
		scanf("%d %d %d ", &N, &S, &p);
		for(int i=0;i<N;i++)
			scanf("%d", &t[i]);
		
		int result = 0;
		
		// check them
		for(int i=0;i<N;i++){
			int x = t[i];
			int y = x/3;
			
			//printf("%d %d %d\n", x, y, z);
			
			// Easy
			if(y >= p){
				result++;
				continue;
			}
			
			// Bruteforce
			bool withoutSurprise = false;
			bool solution = false;
			for(int a=y-2;a<=y+2;a++){
			for(int b=y-2;b<=y+2;b++){
			for(int c=y-2;c<=y+2;c++){	
			
				// range check
				if(a<0 || b<0 || c<0 || a>10 || b>10 || c>10)
					continue;
				
				// must fit to the sum
				if(a+b+c != x)
					continue;
				
				// no too surprised stuff
				if(abs(a-b) > 2 || abs(a-c) > 2 || abs(b-c) > 2)
					continue;
				
				// does it fulfill our requierements?
				if(! (a>=p||b>=p||c>=p))
					continue;
					
				// YEAH! There can be a solution
				solution = true;				
				//printf(" ->  %d %d %d\n", a, b, c);
				
				// Is this solution reachable without using any suprise token?
				if(abs(a-b) <= 1 && abs(a-c) <= 1 && abs(b-c) <= 1)
					withoutSurprise = true;
			}
			}
			}
			
			if(solution){
				if(withoutSurprise){
					result++;
				}else{
					if(S>0){
						S--;
						result++;
					}
				}
			}
			
		}
			
		printf("%d\n", result);
		
		
		fflush(stdout);
	}
	
	return 0;
}
