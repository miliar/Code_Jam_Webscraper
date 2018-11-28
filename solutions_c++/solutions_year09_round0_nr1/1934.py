// Marek Rogala; Code Jam 2009
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <vector>
#include <map>
#include <queue>
#include <set>

using namespace std;
#define VAR(a,b) typeof(b) a=(b)
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;++i)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define ST first
#define ND second
#define MP make_pair
#define SIZE(x) ((int)x.size())
int COND = 1;
#define DB(x) { if (COND > 0) { COND--; REP (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
typedef long long LL;
const int INF = 1000000000;
typedef vector<int> VI; 
typedef pair<int,int> PII;
typedef vector<PII> VPII;

int L,D,N;
int n;

vector<string> dict;
vector<char> possible[17];


bool check(int sl){
	bool ok;
	for(int i=0;i<L;i++){
		ok=false;
		//cout<<"["<<SIZE(possible[i])<<endl;
		REP(j,SIZE(possible[i])){
		//	cout<<"("<<possible[i][j]<<")";
			if(possible[i][j]==dict[sl][i]) {
				ok=true;
				break;
			}
		}
		//cout<<"\tlitera "<<i<<dict[sl]<<" " <<ok<<endl;
		if(!ok) return false;
	}
	return true;
}

int main() {
	scanf("%d%d%d",&L,&D,&N);
	REP(i,D){
		char buff[17];
		scanf("%s", buff);
		string str(buff);
		dict.PB(str);
	}
	FOR(testcase,1,N){
		char buff[600];
		scanf("%s",buff);
		int i=0;
		REP(j,L){
			possible[j].clear();
			if(buff[i]=='('){
				i++;
				while(buff[i]!=')'){
					possible[j].PB(buff[i]);
			//		cout<<"dod"<<buff[i]<<endl;
					i++;
				}
				i++;
			} else {
			//	cout<<"dod"<<buff[i]<<endl;
				possible[j].PB(buff[i++]);
			}
			//cout<<"--"<<endl;
		}
		int cnt=0;
		REP(i,D){
			if(check(i)) {
			//	cout<<"pasuje do "<<i<<endl;
				cnt++;
			}
		}
		printf("Case #%d: %d\n",testcase, cnt);
	}
	return 0;
}


