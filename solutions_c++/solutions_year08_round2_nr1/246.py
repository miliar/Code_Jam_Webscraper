#include <cstdio>
#include <vector>
using namespace std;
typedef pair<int,int> bod;
typedef long long int lint;

int main() {
	int N;
	scanf("%d", &N);
	for (int ixN=0; ixN<N; ixN++) {
		lint n, A, B, C, D, M, x0, y0;
		vector<bod> v;
		scanf("%lld %lld %lld %lld %lld %lld %lld %lld", &n, &A, &B, &C, &D, &x0, &y0, &M);
		v.push_back(make_pair(x0,y0));
		for (int i=0; i<n-1; i++) {
			x0 = (A*x0+B) % M;
			y0 = (C*y0+D) % M;
			v.push_back(make_pair(x0,y0));
		}
		int result = 0;
		//fprintf(stderr, "%d\n", v.size());
		for (int i=0; i<v.size(); i++) {
			for (int j=i+1; j<v.size(); j++) {
				for (int k=j+1; k<v.size(); k++) {
					if ((v[i].first+v[j].first+v[k].first)%3==0 && (v[i].second+v[j].second+v[k].second)%3==0) {
						bod b = make_pair((v[i].first+v[j].first+v[k].first)/3, (v[i].second+v[j].second+v[k].second)/3);
						//fprintf(stderr, "%d %d, %d %d %d\n", b.first, b.second, i, j, k);
						result++;
					}
				}
			}
		}
		printf("Case #%d: %d\n", ixN+1, result);
	}

	return 0;
}
