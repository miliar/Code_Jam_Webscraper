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

//### MAXIMO COMUN DIVISOR ############################################################
long long GCD(long long a, long long b)
{
	if(b==0) return a;
	return GCD(b, a%b);
}

void run1(int caso){
	long long N, Pd,Pg;
	cin >> N >> Pd>>Pg;

	if(Pg==100 && Pd<100) cout << "Case #"<<caso<<": "<< "Broken"<<endl;
	else if(Pg==0 && Pd>0) cout << "Case #"<<caso<<": "<< "Broken"<<endl;
	else{
		if(N>=100)
			cout << "Case #"<<caso<<": "<< "Possible"<<endl;
		else{
			long long sol = GCD(100,Pd);
			if((100/sol) <=N) cout << "Case #"<<caso<<": "<< "Possible"<<endl;
			else cout << "Case #"<<caso<<": "<< "Broken"<<endl;
		}
	}

}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}
