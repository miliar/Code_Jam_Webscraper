#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <queue>

using namespace std;

int gotit[5005];

int main(void) {
	int T;
	int C = 1;
	scanf("%d", &T);
	vector<int> v;
	vector<int> res;
	int K;
	int cnt;
	int tmp;
	int pos;
	int steps;
	while(T--) {
		memset(gotit, 0, sizeof(int) * 5005);
		v.clear();
		res.clear();
		scanf("%d%d", &K, &cnt);
		for(int i = 0; i < cnt; ++i) {
			scanf("%d", &tmp);
			v.push_back(tmp);
		}
		pos = 0;
		for(int i = 1; i <= K; ++i) {
			steps = 1;
			pos++;
			while(1) {
				if(pos == K+1) pos = 1;
				if(gotit[pos] == 1) {
					pos++;
					continue;
				}
				if(steps == i) {
					gotit[pos] = 1;
					res.push_back(pos);
					break;
				}
				steps++;
				pos++;
			}
		}
		
		printf("Case #%d:", C++);	
		for(int i = 0; i < cnt; ++i) {
			for(int j = 0; j < res.size(); ++j) {
				//printf("doing i=%d (%d)    j=%d (%d)\n", i,v[i], j, res[j]);
				if(res[j] == v[i]) {
					printf(" %d", j+1);
					break;
				}
			}			
		}
		printf("\n");
	}	
	return 0;
}
