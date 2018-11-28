#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <queue>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <fstream>
#include <stdio.h>
#include <complex>

using namespace std;

//conversion
//------------------------------------------
inline int toInt(string s) {int v; istringstream sin(s);sin>>v;return v;}
template<class T> inline string toString(T x) {ostringstream sout;sout<<x;return sout.str();}

//typedef
//------------------------------------------
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int, int> PII;
typedef pair<int, PII> TIII;
typedef long long LL;
typedef vector<LL> VLL;

//container util

//------------------------------------------
#define ALL(a)  (a).begin(),(a).end()
#define RALL(a) (a).rbegin(), (a).rend()
#define PB push_back
#define MP make_pair
#define SZ(a) int((a).size())
#define EACH(i,c) for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); ++i)
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define SORT(c) sort((c).begin(),(c).end())
#define MT(a,b,c) MP(a, MP(b, c))
#define T1 first
#define T2 second.first
#define T3 second.second

//repetition
//------------------------------------------
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n)  FOR(i,0,n)

int judge(int t,int cx, int co){
	if(cx==4){
		printf("Case #%d: X won\n", t+1);
		return 1;
	}else if(co==4){
		printf("Case #%d: O won\n", t+1);
		return 1;
	}
	return 0;
}

void main(){
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T;
	cin>>T;
	REP(t,T){
		VS board(4);
		int flag = 0;
		int cnt = 0;
		REP(i,4)cin>>board[i];
		REP(i,4)REP(j,4)if(board[i][j]=='.')cnt++;
		//1‚È‚È‚ß
		int co = 0, cx = 0;
		REP(i,4){
			if(board[i][i]=='X')cx++;
			else if(board[i][i]=='O')co++;
			else if(board[i][i]=='T'){
				cx++;
				co++;
			}
		}
		if(judge(t,cx,co))continue;
		//1‚È‚È‚ß
		co = 0, cx = 0;
		REP(i,4){
			if(board[i][3-i]=='X')cx++;
			else if(board[i][3-i]=='O')co++;
			else if(board[i][3-i]=='T'){
				cx++;
				co++;
			}
		}
		if(judge(t,cx,co))continue;
		//2‚æ‚±
		REP(j,4){
			co = 0, cx = 0;
			REP(i,4){
				if(board[j][i]=='X')cx++;
				else if(board[j][i]=='O')co++;
				else if(board[j][i] == 'T'){
					cx++;
					co++;
				}
			}
			if(flag = judge(t,cx,co))break;
		}
		if(flag)continue;
		//3‚½‚Ä
		REP(j,4){
			co = 0, cx = 0;
			REP(i,4){
				if(board[i][j]=='X')cx++;
				else if(board[i][j]=='O')co++;
				else if(board[i][j] == 'T'){
					cx++;
					co++;
				}
			}
			if(flag = judge(t,cx,co))break;
		}
		if(flag)continue;
		if(cnt == 0)printf("Case #%d: Draw\n", t+1);
		else printf("Case #%d: Game has not completed\n", t+1);
	}
}