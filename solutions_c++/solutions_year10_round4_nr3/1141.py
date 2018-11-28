#include <cstdio>
#include <cstring>
#include <set>

using namespace std;

typedef pair<int, int> pii;

int T, N, R;
set<pii, std::greater<pii> > s;
set<pii, std::greater<pii> >::iterator it, it_next;

set<pii, std::greater<pii> >::iterator todel[1000000];
int todelN;

//pii toadd[1000000];
//int toaddN;


int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	//FILE *fout = fopen("C-small-attempt0.out", "w");

	scanf("%d", &T);
	for (int t=0; t<T; ++t) {
		s.clear();

		scanf("%d", &R);
		int x1,x2,y1,y2;
		for (int k=0; k<R; ++k) {
			scanf("%d%d%d%d", &x1, &y1, &x2, &y2);
			for (int i=x1; i<=x2; ++i) {
				for (int j=y1; j<=y2; ++j) {
					s.insert(pii(j, i));
				}
			}
		}

		int ans = 0;
		for (; !s.empty(); ++ans) {
			
			todelN = 0;
			//toaddN = 0;
			for (it=s.begin(); it!=s.end(); it++) {

				if (s.find(pii(it->first, it->second-1)) == s.end() &&
					s.find(pii(it->first-1, it->second)) == s.end()) {
					//printf("del\n");
					//s.erase(it);
					todel[todelN++] = it;
				}
				if (s.find(pii(it->first-1, it->second+1)) != s.end()) {
					//printf("add\n");
					s.insert(pii(it->first, it->second+1));
					//toadd[toaddN].first = it->first;
					//toadd[toaddN++].second = it->second+1;
				}
			}
			
			for (int i=0; i<todelN; ++i) {
				s.erase(todel[i]);
			}
			//for (int i=0; i<toaddN; ++i) {
			//	s.insert(toadd[i]);
			//}
		}

		printf("Case #%d: %d\n", t+1, ans);
	}

	//fclose(fout);

	return 0;
}