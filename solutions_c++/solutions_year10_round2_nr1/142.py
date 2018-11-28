#include <cstdio>
#include <map>
#include <vector>
#include <string>
#include <algorithm>
using namespace std;

#define REP(i,n) for(int (i)=0,_n=(n);(i)<_n;(i)++)
#define FOR(i,a,b) for(int (i)=(a),_n=(b);(i)<=_n;(i)++)
#define FORD(i,a,b) for(int (i)=(a),_n=(b);(i)>=_n;(i)--)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)
vector<string> split( const string& s, const string& delim =" " ) {
	vector<string> res;
	string t;
	REP(i,s.size()) {
		if ( delim.find(s[i]) == string::npos ) t += s[i];
		else if ( !t.empty() ) { res.push_back(t); t = ""; }
	}
	if ( !t.empty() ) res.push_back(t);
	return res;
}

struct tdata {
	string name;
	map <string,tdata*> dir;
};

void f(tdata *curr, int d) {
	if ( curr == 0 ) return;
	REP(i,d*5) putchar( ' ' );
	puts( curr->name.c_str() );
	FOREACH(it,curr->dir) f(it->second,d+1);
}

int main()
{
	char line[1000];
	int ncase;
	scanf( "%d", &ncase );
	FOR(tcase,1,ncase) {
		int n, m;
		tdata *root = new tdata;
		root->name = "root";
		scanf( "%d %d", &n, &m );
		REP(i,n) {
			scanf( "%s", line );
			vector <string> path = split(line,"/");
			tdata *curr = root;
			REP(j,path.size()) {
				if ( curr->dir[path[j]] == 0 ) {
					tdata *node = new tdata;
					node->name = path[j];
					curr->dir[path[j]] = node;
				}
				curr = curr->dir[path[j]];
			}
		}
		int ans = 0;
		REP(i,m) {
			scanf( "%s", line );
			vector <string> path = split(line,"/");
			tdata *curr = root;
			REP(j,path.size()) {
				if ( curr->dir[path[j]] == 0 ) {
					tdata *node = new tdata;
					node->name = path[j];
					curr->dir[path[j]] = node;
					ans++;
				}
				curr = curr->dir[path[j]];
			}
		}
		
		printf( "Case #%d: %d\n", tcase, ans );

	}
	return 0;
}
