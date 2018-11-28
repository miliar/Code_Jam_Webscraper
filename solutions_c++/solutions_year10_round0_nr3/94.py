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

#define MAX 1000

void run1(int caso){
	LL R,K,N;

	cin >> R>>K>>N;

	int g[MAX]={0};
	REP(i,N){
		cin >> g[i];
	}

	LL val[MAX]={0};
	int next[MAX]={0};
	REP(i,N){
		LL sum = 0;
		int j =0;
		while(sum+g[(i+j)%N] <=K && j!=N){
			sum+=g[(i+j)%N];
			j++;
		}
		val[i]=sum;
		next[i]=(i+j)%N;
	}
	
	int ind = 0;
	LL sol = 0;

	REP(i,R){
		sol+=val[ind];
		ind = next[ind];
	}
	
	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}