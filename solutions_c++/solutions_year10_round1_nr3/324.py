#include <list>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <cfloat>


 
using namespace std;
 
const int oo = 0x3f3f3f3f;
const double eps = 1e-9;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
 
#define sz(c) int((c).size())
#define all(c) (c).begin(), (c).end()
#define FOR(i,a,b) for (int i = (a); i < (b); i++)
#define FORD(i,a,b) for (int i = int(b)-1; i >= (a); i--)
#define FORIT(i,c) for (__typeof__((c).begin()) i = (c).begin(); i != (c).end(); i++)

map<pii, bool> mm;
bool isWin(int a, int b){
	if(a==b)return false;
	if(a>b){
		int tmp = a;
		a = b;
		b = tmp;
	}
	if(b%a==0){
		return true;
	}
	int d = (b/a);
	if(!isWin(b%a,a))return true;
	return (d>1);
}
int main(){
	mm.clear();
	int tc;
	cin >> tc;
	FOR(tcc,1,tc+1){
		int a1, a2, b1, b2;
		cin >> a1 >> a2 >> b1 >> b2;
		int ret = 0;
		FOR(i,a1,a2+1)FOR(j,b1,b2+1){
			if(isWin(i,j))++ret;
		}
		cout << "Case #" << tcc << ": " << ret << endl;
	}
	return 0;
}
