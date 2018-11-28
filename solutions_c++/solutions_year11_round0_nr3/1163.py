#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;

int main(){
	int n; scanf("%d\n", &n);
	for(int i = 0; i < n; i++){
		int inps; scanf("%d\n", &inps);
		int first, cumulative, sum = 0;
		vector<int> inp;
		for(int j = 0; j < inps; j++){
			scanf("%d\n", &first);
			inp.push_back(first);
		}
		sort(inp.begin(), inp.end());
		sum = cumulative = inp[0];
		for(int j = 1; j < inps; j++) {
			sum += inp[j];
			cumulative ^= inp[j];
		}
		printf("Case #%d: ", i+1);
		if(cumulative == 0)
			printf("%d\n", sum - inp[0]);
		else printf("NO\n");
	}
	return 0;
}
