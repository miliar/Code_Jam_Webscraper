#include <cstdio>
#include <cstring>
#include <algorithm>
#include <vector>
#include <string>
#include <map>

#define REP(AA,BB) for(AA=0; AA<(BB); ++AA)
#define FOR(AA,BB,CC) for(AA=(BB); AA<(CC); ++AA)
#define FC(AA,BB) for(typeof(AA.begin()) BB=AA.begin(); BB!=AA.end(); ++BB)
#define SZ(AA) ((int)(AA.size()))
#define ALL(AA) (AA).begin(), (AA).end()
#define PB push_back
#define MP(AA,BB) make_pair((AA), (BB))

using namespace std;

typedef vector<int> VI;
typedef pair<int, int> PII;

struct drzewo {
	map<string, drzewo*> c;
};

vector<string> split(string s, string delim) {
    int i; vector<string> res;
    while((i=s.find(delim))!=string::npos) {
        res.push_back(s.substr(0,i));
        s=s.substr(i+delim.size());
    }
    if(s.size()>0)
        res.push_back(s);
    return res;
}

drzewo *root;

int ins(vector<string> &a) {
	drzewo *cur=root; int i, res=0;
	REP(i,SZ(a)) {
		if(!cur->c.count(a[i])) {
			++res;
			cur->c[a[i]]=new drzewo;
		}
		cur=cur->c[a[i]];
	}
	return res;
}

char buf[1000010];

int main(void) {
	int T, n, m, i, j, k, t, res;
	scanf("%d", &T); 
	FOR(t,1,T+1) {
		scanf("%d%d", &n, &m);
		root = new drzewo; res=0;
		REP(i,n) {
			scanf("%s", buf);
			vector<string> z=split(string(buf+1), "/");
			ins(z);
		}
		REP(i,m) {
			scanf("%s", buf);
			vector<string> z=split(string(buf+1), "/");
			res+=ins(z);
		}
		printf("Case #%d: %d\n", t, res);
	}
	return 0;
}
		


