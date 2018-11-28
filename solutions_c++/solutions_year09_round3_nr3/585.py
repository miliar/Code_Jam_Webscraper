#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <cstring>
#include <iomanip>
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
const int MAX = 10000000;
ifstream fin("C-small-attempt0.in");
ofstream fout("C-small.out");
int noCase;
int p,q;
int solve(vector<int> list,int n){
	vector<int> l;
	int ret = 0;
	REP(i,n)l.push_back(i);
	REP(i,SIZE(list)){
		
		int idx = list[i]-1;
		l[idx]=-1;
		int st = idx-1;
		while(st >= 0 && l[st]!= -1){
			ret++;st--;
		}
		st = idx+1;
		while(st < n && l[st]!= -1){
			ret++;st++;
		}
	}
	return ret;
}
int main() {
	fin>>noCase;
	for(int k=1;k<=noCase;k++){
		fin>>p>>q;
		vector<int> list;
		REP(i,q){
			int a;fin>>a;
			list.push_back(a);
		}
		sort(ALL(list));
		int ret = INF;
		do{
			ret = min(ret,solve(list,p));
		}while(next_permutation(ALL(list)));
		fout<<"Case #"<<k<<": "<<ret<<endl;
		
	}
    return 0;
}
