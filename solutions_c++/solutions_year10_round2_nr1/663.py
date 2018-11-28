#include<cstdio>
#include<map>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;

char str[10009];
vector<pair< vector<string>, int> > vps;

vector<string> split( char str[]){
	vector<string> ret;
	string ss;
	char *p = strtok(str, "/");
	while(p){
		ss = p;
		ret.push_back(ss);
		p = strtok( NULL, "/");
	}

	return ret;
}
int main(){
	int T, X, i, a, ret,j,k, n, m,mx;
	vector<string> cur;

	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);

	scanf("%d", &T);
	string ss;

	for(X = 1 ;X <=T; ++X){
		scanf("%d%d", &n, &m);
		ret = 0;

		//init( root );
		vps.clear();
		for( i = 0; i<n; ++i) {
			scanf("%s", str);
		

			cur = split( str );
			//build( cur );

			vps.push_back( make_pair( cur, 0));
		}

		for( i = 0; i<m; ++i){
			scanf("%s", str);

			cur = split(str);
			//a = build( cur);
			vps.push_back( make_pair(cur, 1));
			//ret += a;
		}

		sort( vps.begin(), vps.end());

		ret = 0;

		for( i = 0; i< vps.size(); ++i){
			if( vps[i].second == 0) continue;

			mx = 0;
			for( j = 0; j<i; ++j){
				for( k = 0; k<vps[i].first.size() && k<vps[j].first.size(); ++k){
					if( vps[i].first[k] != vps[j].first[k]) break;
				}
				mx = max( mx, k);
			}

			ret += vps[i].first.size() - mx;
		}


		printf("Case #%d: %d\n", X, ret);
	}


	return 0;
}