#include <algorithm>
#include <valarray>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
using namespace std;

int main(){
	int Tests;
	scanf("%d ", &Tests);
	for(int Test = 1; Test <= Tests; ++Test){
		int n;
		scanf("%d", &n);
		vector<pair<int,int> >vec;
		while(n--){
			int a, b;
			scanf("%d %d", &a, &b);
			vec.push_back(make_pair(a, b));
		}
		int result = 0;
		for(int i = 0; i < vec.size(); ++i){
			for(int j = 0; j < vec.size(); ++j){
				if(i == j) continue;
				if(vec[i].first > vec[j].first && vec[i].second > vec[j].second) continue;
				++result;
			}
		}
		result >>= 1;
		printf("Case #%d: %d\n", Test, result);
	}
}
