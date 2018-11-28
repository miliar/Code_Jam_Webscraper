#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <map>
#include <set> 
#include <sstream>
#include <fstream>
#include <utility>
#include <string>
#include <vector>
#include <stack>
#include <queue>
using namespace std;
#define REP(i,a) for(int i=0;i<a;i++)
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define SIZE(c) (int)c.size()
#define ALL(c) (c).begin(),(c).end() 
typedef pair<int, int> PII;
typedef pair<char, char> PCC;
const int INF = 1000000000;
const int MAXN = 30, MAXX = 105;
int T, C, D, N;
string str;
char form[MAXN][MAXN], ret[MAXX * MAXX];
bool opp[MAXN][MAXN];
char s[MAXX];
string solve(){
	int M = 0;
	for(int i = 0; i < N; i ++){
		if(M == 0){
		 ret[M ++] = s[i];
		 continue;
		}
		char c = form[s[i] - 'A'][ret[M-1] - 'A'];
		if(c != ' '){
			ret[M - 1] = c;
		}
		else{
			bool cl = false;
			for(int j = 0; j < M; j ++){
				if(opp[s[i] - 'A'][ret[j] - 'A']){
					cl = true;
				}
			}
			if(cl){
				M = 0;
			}
			else{
				ret[M ++] = s[i];
			}
		}
	}
	string r = "[";
	for(int i = 0; i < M - 1; i ++)
		r += ret[i], r += ", ";
	if(M != 0)
		r += ret[M-1];
	r += "]";
	return r;
}
int main() {
	freopen("B-large.in", "r", stdin);
	freopen("b-large.out", "w", stdout);
	cin>>T;
	REP(t, T){
		
		memset(opp, false, sizeof opp);
		REP(i, MAXN) REP(j, MAXN) form[i][j] = ' ';
		cin>>C;
		REP(i, C){
			cin>>str;
			form[str[0] - 'A'][str[1] - 'A'] = str[2];
			form[str[1] - 'A'][str[0] - 'A'] = str[2];
		}
		cin>>D;
		REP(i, D){
			cin>>str;
			opp[str[0] - 'A'][str[1] - 'A'] = true;
			opp[str[1] - 'A'][str[0] - 'A'] = true;
		}
		cin>>N;
		REP(i, N){
			cin>>s[i];
		}
		cout<<"Case #"<<(t+1)<<": ";
		cout<<solve()<<endl;
	}
	return 0;
}
