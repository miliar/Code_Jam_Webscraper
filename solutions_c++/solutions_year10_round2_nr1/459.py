#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>
 
using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

typedef pair < int, int > pii;
typedef long long LL;

int N,M;
map<string,int> m;

int cont(string s){
	
	string path="";
	int sol = 0;
	s+="/";
	REPSZ(i,s){
		if(i>0){
			if(s[i]=='/'){
				if(m.find(path)==m.end()){
					sol++;
					m[path] = 1;
				}
			}
		}
		path+=s[i];
	}
return sol;
}
void run1(int caso){
	cin >> N>>M;
	m.clear();
	m["/"]=1;
	REP(i,N) {
		string path;
		cin >> path;
		m[path]=1;
	}
	int sol=0;
	REP(i,M){
		string path;
		cin >> path;
		if(m.find(path)==m.end()){
			sol+=cont(path);
			m[path] = 1;
		}//else se encuentra
	}

	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}