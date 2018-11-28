#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <cstdio>
using namespace std;
typedef long long int64;

int main(void){
	freopen("1.txt", "rt", stdin);
	freopen("2.txt", "wt", stdout);
	vector<int> tm;
	int cases;
	int a, b, c;
	int time;
	int counter = 0;
	scanf("%d", &cases);
	for(int i = 0; i < cases; i++){
		vector<int> tm;
		scanf("%d%d%d", &a,&b,&c);
		for(int j=0; j < c; j++){
			scanf("%d", &time);
			tm.push_back(time);
		}
		sort(tm.begin(), tm.end());
		reverse(tm.begin(), tm.end());
		int index = 1;
		counter = 0;
		for (int k = 0; k < c; k++) {
			if ( k == 0) {
			counter += tm[k];
			continue;
			}
			if (k % b == 0) {
				index ++;
				}
			counter += (index * tm[k]);

		}
		
		printf("Case #%d: %d\n", i + 1, counter);
		
	}
	return 0;
}
