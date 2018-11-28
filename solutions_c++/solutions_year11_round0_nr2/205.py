#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <cctype>
#include <cstring>
#include <string>
#include <sstream>
#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <functional> 
#include <numeric>
using namespace std;
#define foreach(i,v) for(__typeof((v).end()) i=(v).begin();i!=(v).end();++i)
#define rforeach(i,v) for(__typeof((v).rend()) i=(v).rbegin();i!=(v).rend();++i)
#define FOR(i,b,e) for(int i=(b);i<(e);++i)
#define FORE(i,b,e) for(int i=(b);i<=(e);++i)
#define debug(x) cerr << #x << " = " << (x) << "\n"
typedef long long LL;

int main(){
	int t;
	cin >> t;
	FORE(z,1,t){
		int c, d, n;
		cin >> c;
		char to[200][200];
		memset(to,0,sizeof(to));
		FOR(i,0,c){
			string s;
			cin >> s;
			to[s[0]][s[1]]=s[2];
			to[s[1]][s[0]]=s[2];
		}
		cin >> d;
		bool opp[200][200];
		memset(opp,false,sizeof(opp));
		FOR(i,0,d){
			string s;
			cin >> s;
			opp[s[0]][s[1]]=true;
			opp[s[1]][s[0]]=true;
		}
		cin >> n;
		string s;
		cin >> s;
		char a[n], m=0;
		FOR(i,0,n){
			a[m++] = s[i];
			if (m>1 && to[a[m-2]][a[m-1]])
				a[m-2] = to[a[m-2]][a[m-1]], m--;
			FOR(i,0,m-1)
				if (opp[a[i]][a[m-1]]) m=0;
		}
		printf("Case #%d: [",z);
		if (m>0) putchar(a[0]);
		FOR(i,1,m)
			printf(", %c",a[i]);
		puts("]");

	}
	return 0;
}
