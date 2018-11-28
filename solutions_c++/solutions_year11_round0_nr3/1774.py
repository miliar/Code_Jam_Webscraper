#include <stdio.h>
#include <algorithm>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
    int nCases;
    scanf("%d", &nCases);

    for(int i = 0; i < nCases; i++) {
	vector<int> candies;
        printf("Case #%d: ", i+1);
	int N = 0;
	scanf("%d", &N);

	for(int j = 0; j < N; j++) {

	    int x = 0;
	    scanf("%d ", &x);
	    candies.push_back(x);

	}

	std::sort(candies.begin(), candies.end());

	int size = candies.size();

	int res = 0;
	for(int z = 0; z < size; z++) {
	    res ^= candies[z];
	}

        if(res == 0) {
            int sum = 0;
            for(int y = 1; y < size; y++)
                sum += candies[y];
            printf("%d\n",sum);
	}
	else {
                printf("NO\n");
	}
    }
    return 0;
}
