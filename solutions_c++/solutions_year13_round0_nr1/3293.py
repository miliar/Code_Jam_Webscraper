#include <vector>
#include <string>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <fstream>
#include <map>
#include <deque>
#include <queue>
#include <bitset>
#include <stack>
#include <set>
#include <cstring>
#include <cstdlib>
#include <cassert>
#include <iomanip> 
#include <ctime>
using namespace std;

#define sz size()
#define FOR(i,a,b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i,a,b) for(int (i) = (a); (i) >= (b); --(i))
#define rep(i,n) for (int (i) = 0; (i) < (n); ++(i))
#define fe(i,a) for (int (i) = 0; (i) < int((a).size()); ++(i))
#define C(a) memset((a),0,sizeof(a))
#define inf 1000000000
#define pb push_back
#define ppb pop_back
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define pi 2*acos(0.0)
#define sqr(a) (a)*(a)
#define mp(a,b) make_pair((a), (b))
#define X first
#define Y second 

typedef vector<int> vint;
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int, int> pii; 
const int INF=~(1<<31);
const double eps=1e-6;
 
const long double PI = 3.1415926535;
 
int main() {
   freopen("input.txt", "r", stdin);
   freopen("output.txt", "w", stdout);
  int T;
  cin>>T;
  FOR(t,1,T){
	  printf("Case #%d: ",t);
	vector<string> s(4);
	rep(i,4)cin>>s[i];
	int win=0;
	rep(j,4){
		int i=0;
		for(;i<4  && (s[j][i]=='X' || s[j][i]=='T');i++);
		if(i==4){
			win=1;
		}
		i=0;
		for(;i<4  && (s[i][j]=='X' || s[i][j]=='T');i++);
		if(i==4){
			win=1;
		}
	}
	int k=0;
	for(;k<4 && (s[k][k]=='X' || s[k][k]=='T');k++);
	if(k==4){
			win=1;
	}
	k=0;
	for(;k<4 && (s[k][4-k-1]=='X' || s[k][4-k-1]=='T');k++);
	if(k==4){			
			win=1;
	}
	if(win){
		puts("X won");
		continue;
	}
	rep(j,4){
		int i=0;
		for(;i<4  && (s[j][i]=='O' || s[j][i]=='T');i++);
		if(i==4){ 
			win=1; 
		}
		i=0;
		for(;i<4  && (s[i][j]=='O' || s[i][j]=='T');i++);
		if(i==4){ 
			win=1; 
		}
	}
	k=0;
	for(;k<4 && (s[k][k]=='O' || s[k][k]=='T');k++);
	if(k==4){ 
			win=1;
	}
	k=0;
	for(;k<4 && (s[k][4-k-1]=='O' || s[k][4-k-1]=='T');k++);
	if(k==4){ 
			win=1;
	}
	
	if(win){
		puts("O won");
		continue;
	} 
	{
		k=0;
		rep(i,4)rep(j,4)if(s[i][j]=='.')k++;
		if(k)puts("Game has not completed"); else puts("Draw");
	}
  }
  return 0;
}
