#include <vector>
#include <string>
#include <map>
#include <cstdio>
#include <sstream>
#include <cmath>
using namespace std;

#define sz(x) ((int)(x.size()))
template<class T> string toString(T& v){ ostringstream os; os << v; return os.str(); }

int cacheCnt[2000000];
int cache[2000000][7];
map<pair<int,int>, bool> cacheChecker;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	for(int i=1;i<=2000000;++i){
		string val = toString(i);
		for(int j=1;j<val.size();++j){
			string next = val.substr(j) + val.substr(0,j);
			int value = stoi(next);
			if(i < value && cacheChecker.find(make_pair(i,value)) == cacheChecker.end()){
				cache[i][cacheCnt[i]] = value;
				cacheChecker[make_pair(i,value)] = true;
				++cacheCnt[i];
			}
		}
	}

	int tests; scanf("%d",&tests);
	for(int test=1;test<=tests;++test){
		int a,b; scanf("%d %d",&a,&b);
		int cnt = 0;
		for(int i=a;i<=b;++i){
			for(int j=0;j<cacheCnt[i];++j){
				if(cache[i][j] <= b){
					++cnt;
				}
			}
		}
		printf("Case #%d: %d\n",test,cnt);
	}
	return 0;
}
