#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <utility>
#include <vector>
#define MAX 105

using namespace std;

typedef pair<int, int> pii;

int main(){
	int T;
	scanf ("%d", &T);
	for (int t = 1; t <= T; t++){
		int N;
		scanf ("%d", &N);
		vector <int> seq[2];
		vector <pii> ord;
		ord.clear();
		seq[0].clear();
		seq[1].clear();
		for (int i = 0; i < N; i++){
			char c;
			int x;
			scanf (" %c %d", &c, &x);
			if (c == 'B'){
				seq[0].push_back(x);
				ord.push_back(make_pair(0, x));
			}
			else{
				seq[1].push_back(x);
				ord.push_back(make_pair(1,x));
			}
		}
		int cnt[] = {0, 0};
		int pos[] = {1, 1};
		int tmp = 0;
		for (int i = 0; i < N; i++){
			int deltat = 1 + abs(pos[ord[i].first] - ord[i].second);
			tmp += deltat;
			cnt[ord[i].first]++;
			pos[ord[i].first] = ord[i].second;
			int out = (ord[i].first + 1) % 2;
			if (cnt[out] < seq[out].size()){
				if (abs(pos[out] - seq[out][cnt[out]]) <= deltat)
					pos[out] = seq[out][cnt[out]];
				else{
					int mult = 1;
					if (seq[out][cnt[out]] - pos[out] < 0)
						mult = -1;
					pos[out] += deltat * mult;
				}
			}
		}
		printf ("Case #%d: %d\n", t, tmp);
	}
	return 0;
}
