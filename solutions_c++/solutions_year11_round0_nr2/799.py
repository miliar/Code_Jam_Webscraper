#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <queue>
#include <cmath>
#include <algorithm>
#include <vector>
#include <stack>
#include <map>
#include <ctime>
#include <list>
#include <set>
using namespace std;
typedef pair<int,int> PII;
typedef vector<int> VI;
typedef long long LL;
#define PATH(x) "c:\\Users\\Topsky\\Desktop\\ACM\\"#x
#define CLR(x,a) memset(x,a,sizeof(x))
#define out(x) cerr<<#x<<" "<<x
#define FOR(i,n) for(int i=0;i<(n);i++)
#define REP(i,a,b) for(int i=(a);i<=(b);i++)
#define DEP(i,a,b) for(int i=(a);i>=(b);i--)
#define FORIT(it,c) for(__typeof((c).begin())it=(c).begin();it!=(c).end();it++)
#define ALL(a) a.begin(),a.end()
#define MP make_pair
#define PB push_back
#define LB(x) (x&(-x))
#define L(x) (x<<1)
#define R(x) ((x<<1)+1)
#define oo 0x3f3f3f3f
#define X first
#define Y second

const int MAXN = 1000 + 10;
int n, m, r;
string str;
vector<PII> gp;
int opp[MAXN][MAXN];
int com[MAXN][MAXN];

int main(int argc, char *argv[]){
	freopen("data.in", "r", stdin);
	freopen("data.out", "w", stdout);
	int cas; cin >> cas;
	FOR(tc, cas){
		cin >> m;
		CLR(com, -1);
		FOR(i, m){
			cin >> str;
			com[str[0]][str[1]] = str[2];
			com[str[1]][str[0]] = str[2];
		}
		cin >> r;
		CLR(opp, 0);
		FOR(i, r){
			cin >> str;
			opp[str[0]][str[1]] = 1;
			opp[str[1]][str[0]] = 1;
		}
		cin >> n;
		cin >> str;
		list<char> st;
		FOR(i, n){
			if(st.size() < 1){
				st.PB(str[i]);
			}else{
				char c, t1 = st.back(); st.pop_back();
				if((c = com[t1][str[i]]) != -1){
					st.PB(c);
				}else {
					st.PB(t1);
					FORIT(it, st){
						if(opp[*it][str[i]] != 0){
							st.clear();
							break;
						}
					}
					if(!st.empty())st.PB(str[i]);
				}
			}
		}
		printf("Case #%d: ", tc + 1);
		printf("[");
		int p = 0;
		FORIT(it, st){
			printf("%c", *it);
			if(p++ != st.size() - 1)cout << ", ";
		}
		puts("]");
	}
}
