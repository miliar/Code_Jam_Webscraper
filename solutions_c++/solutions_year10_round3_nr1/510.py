#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

int main(){
	int tc, t, n;
	vector<pair<int, int> >v;
	int a,b,c;
	scanf("%d", &tc);
	for(t=0;t<tc;++t){
		scanf("%d", &n);
		v = vector<pair<int, int> >(n);
		for(int i=0; i<n; ++i){
			scanf("%d %d", &a, &b);
			v[i] = make_pair(a, b);
		}
		c=0;
		for(int i=0; i<n; ++i){
			for(int j=i+1; j<n; ++j){
				if(v[i].first < v[j].first && v[i].second > v[j].second)
					++c;
				if(v[i].first > v[j].first && v[i].second < v[j].second)
					++c;
			}
		}
		printf("Case #%d: %d\n", t+1, c);
	}
}
