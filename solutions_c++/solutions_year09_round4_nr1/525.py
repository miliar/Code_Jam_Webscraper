#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<map>
#include<vector>
#include<list>
#include<set>
#include<queue>
#include<cassert>
#include<sstream>
#include<string>
#include<cmath>
#include<algorithm>
using namespace std;

#define LET(x,a) 	__typeof(a) x(a)
#define IFOR(i,a,b) 	for(LET(i,a);i!=(b);++i)
#define EACH(it,v)  	IFOR(it,v.begin(),v.end())
#define FOR(i,a,b)  	for(int i=(int)(a) ; i < (int)(b);++i)
#define REP(i,n) 	FOR(i,0,n)
#define PB		push_back
#define MP 		make_pair
#define EPS		1e-9
#define INF 2000000000

typedef vector<int>	VI;
typedef long long	LL;
typedef pair<int,int>	PI;
int main() {
	int t;
	scanf("%d",&t);
	for (int kases = 1; kases <= t; ++ kases) { 
		cout << "Case #"<<kases <<": ";
		int N;
		scanf("%d",&N);
		string s[100];
		REP(i,N) {
			cin >> s[i];
		}
		int ans = 0;
		REP(i,N) {
			FOR(j,i,N) {
				int solve = 1;
				FOR(k,i+1,N) {
					if(s[j][k] == '1') {
						solve = false;
						break;
					}
				}
				if(solve) {
					ans += j - i;
					for(int pp = j; pp >i; --pp) {
					string tmp = s[pp - 1];
					s[pp-1] = s[pp];
					s[pp] = tmp;

					}
					break;
				}
			}
		}
		cout << ans << endl;

	}
	return 0;
}

