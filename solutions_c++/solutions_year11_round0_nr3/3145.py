#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <set>

using namespace std;

#define forn(i, n) for (int i = 0; i < (int)(n); i++)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define sz(a) (int)(a).size()
#define all(a) (a).begin(), (a).end()
#define zero(a) memset(a, 0, sizeof(a))
#define pb push_back
#define mp make_pair

int N = 0;
vector<int> candy;

int go(int i, int emptyXor, int fullXor, int emptySum, int fullSum){
    
	if(i == N){
		if(emptySum == 0 || fullSum == 0) return 0;
		if(emptyXor == fullXor) return max(emptySum,fullSum);
		return 0;
	}

	int tmp = 0;
	tmp = max(tmp, go(i+1,emptyXor^candy[i],fullXor^candy[i],emptySum+candy[i],fullSum-candy[i]));
	tmp = max(tmp, go(i+1,emptyXor,fullXor,emptySum,fullSum));
	return tmp;

}

int main(){

	FILE* input = fopen("input.txt", "r");
	FILE* output = fopen("output.txt", "w");
	
	int nTestCases = 0;
	
	fscanf(input,"%d", &nTestCases);

	for(int tt=0; tt<nTestCases; tt++){

		fscanf(input, "%d ", &N);
		
		candy.clear();
		int tmp = 0, fullXor = 0, fullSum = 0;
		for(int i=0; i<N; i++){
			fscanf(input, "%d ", &tmp);
			candy.pb(tmp);
			fullXor ^= tmp;
			fullSum += tmp;
		}

		int ret = go(0,0,fullXor,0,fullSum);

		if(ret) fprintf(output, "Case #%d: %d\n", tt+1, ret);
		else fprintf(output, "Case #%d: NO\n", tt+1);

	}
}