#include <stdlib.h>
#include <stdio.h>
#include <algorithm>
#include <iostream>
#include <queue>
#include <list>
#include <map>
#include <numeric>
#include <set>
#include <sstream>
#include <string>
#include <vector>

using namespace std;
#define VAR(a,b) __typeof(b) a=(b)
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define REP(i,n) FOR(i,0,n)
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define REVERSE(c) reverse(ALL(c))
#define UNIQUE(c) SORT(c),(c).resize(unique(ALL(c))-(c).begin())
#define INF 1000000000
#define X first
#define Y second
#define pb push_back
#define SZ(c) (c).size()

int case_num=0;
#define gout cout<<"Case #"<<++case_num<<": "

typedef pair<int, int> PII;
typedef vector<int> VI;
typedef vector<PII> VPII;
typedef vector<VI> VVI;


void function();

int main() {
	int num_cases;
	cin>>num_cases;
	REP(i,num_cases)
		function();

	return 0;
}
int R,C;
bool check(VVI&,int,int);
void function(){
	VVI v;
	char c;
	cin>>R; cin>>C;
	for(int i=0;i<R;i++){
		v.push_back(VI());
		for(int j=0;j<C;j++){
			cin>>c;
			v[i].push_back((c == '#')?1:0);
		}
	}
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			if(v[i][j] == 1){
				if(check(v,i,j) == false){
				   	gout<<endl<<"Impossible"<<endl;
					return;
				}
			}
		}
	}
	char ca[] = ".#\\/";
	gout<<endl;
	for(int i=0;i<R;i++){
		for(int j=0;j<C;j++){
			cout<<ca[v[i][j]];
		}
		cout<<endl;
	}

}
bool check(VVI &v,int a,int b){
	if(a >= R-1 || b >= C-1) return false;
	if(v[a][b] == 1 && v[a][b+1] == 1 && v[a+1][b] == 1 && v[a][b+1] == 1){
		v[a][b] = 3;
		v[a][b+1] = 2;
		v[a+1][b] = 2;
		v[a+1][b+1] = 3;
		return true;
	}
	return false;
}

