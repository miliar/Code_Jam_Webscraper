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
const int INF = 1000000000;
int test, a1, a2, b1, b2;
map<PII, bool> m;
bool win(int a, int b){
	if(a <= 0 || b <= 0 ) return false;
	int k = (int) floor(a/b);
	if(k* b == a) k--;
	while(k > 0 && k*b < a){
		if(!win(a - k*b, b)) return true;
		k--;
	}
	k = (int) floor(b/a);
	if(k* a == b) k--;
	while(k > 0 && k*a < b){
		if(!win(a, b - k*a)) return true;
		k--;
	}
	return false;
}
int main() {
	ifstream fin("C-small-attempt2.in");
	ofstream fout("c-small.out");
	fin>>test;
	for(int t = 1; t <= test; t ++ ){
		fin>>a1>>a2>>b1>>b2;
		fout<<"Case #"<<t<<": ";
		int ret = 0;
		FOR(i, a1, a2){
			FOR(j, b1, b2){
				if(win(i,j)) ret++;
			}
		}
		fout<<ret<<endl;
	}
    return 0;
}
