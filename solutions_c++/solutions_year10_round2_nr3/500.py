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
#define CLEAR(t,v) memset((t),v,sizeof(t))

typedef pair < int, int > pii;
typedef long long LL;
#define MOD 100003
#define MAX 28

long long comb[50][50];

long long getComb(LL i,LL j){

  if( i < j) return 0;
  if( j == 0) return 1;

  if( comb[i][j]!=-1) return comb[i][j];
  
  return comb[i][j] = getComb(i-1,j-1) + getComb(i-1,j);
}

int N;
LL memo[MAX][MAX];
LL go(int tam, int last){//cumple
	if(memo[tam][last] > -1) return memo[tam][last];
	if(N==last) return 0;
	LL esp = last-tam-1;
	LL disp = N-last-1;
	LL sol = 0;

	if(disp>=esp)
		sol = getComb(disp, esp)% MOD;

		FORE(i,last+esp+1,N-1) {
			sol  = (sol + go(tam+esp+1,i)% MOD)% MOD;
		
		}
	

	memo[tam][last] = sol% MOD;
	return sol% MOD;
}

void run1(int caso){
	cin >> N;
	CLEAR(memo,-1);
	CLEAR(comb,-1);

	LL sol=1; // N solo
	FORE(i,2,N-1){
		
		sol  = (sol + go(1,i)% MOD)% MOD;
	}
	cout << "Case #"<<caso<<": "<< sol<<endl;
}
void run2(int caso){
	cin >> N;
	CLEAR(memo,-1);
	CLEAR(comb,-1);

	int a[26]={0,0,1,2,3,5,8,14,24,43,77,140,256,472,874,
		1628,3045,5719,10780,20388,38674,73562,40265,68060,13335,84884};
	cout << "Case #"<<caso<<": "<< a[N]<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run2(i);
	return 0;
}