#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <set>

#define REP(AA,BB) for(AA=0; AA<BB; ++AA)
#define FOR(AA,BB,CC) for(AA=BB; AA<CC; ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)

using namespace std;

char c[10010], d[20];

struct tree {
	double p; string s;
	vector<int> ch;
	void clear() { ch.clear(); }
};

tree P[10010]; int st[10010];

int main(void) {
	int t, n, m, M, T, L, i, j, k, x, h; double tmp, res;
	scanf("%d", &T);
	REP(t,T) {
		memset(c, 0, sizeof c);
		scanf("%d", &L); fgets(c+M, 100, stdin); M=0;
		REP(i,L) {
			fgets(c+M, 100, stdin); x=strlen(c+M);
			c[M+x-1]=' '; M+=x;
		}
		k=-1; h=0;
		for(i=0; i<M; ) {
			if(c[i]=='(') {
				if(h!=0)
					P[st[k]].ch.push_back(h);
				sscanf(c+i+1, "%lf", &tmp);
				P[h].p=tmp;
				st[++k]=h++;
				++i;
			}
			else if(c[i]==')') {
				--k;
				++i;
			}
			else if(isalpha(c[i])) {
				sscanf(c+i, "%s", d);
				for(; i<M && isalpha(c[i]); ++i);
				P[st[k]].s=string(d);
			}
			else
				++i;
		}
		printf("Case #%d:\n", t+1);
		scanf("%d", &n); 
		REP(i,n) {
			scanf("%*s%d", &m); set<string> S;
			REP(j,m) {
				scanf("%s", d);
				S.insert(string(d));
			}
			res=1.0;
			for(k=0; !P[k].ch.empty(); ) {
				res*=P[k].p;
				if(S.find(P[k].s)!=S.end())
					k=P[k].ch[0];
				else
					k=P[k].ch[1];
			}
			res*=P[k].p;
			printf("%lf\n", res);
		}
		REP(i,h)
			P[i].clear();
	}
	return 0;
}

