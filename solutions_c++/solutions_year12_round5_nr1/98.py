#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#include<cmath>
#define REP(i,m) for(int i=0;i<m;++i)
#define REPN(i,m,in) for(int i=in;i<m;++i)
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
using namespace std;
static const int INF =500000000; 
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
typedef long long int lint;
typedef pair<int,int> pi;
pair<pi,int> lev[1005];
bool comp(const pair<pi,int>& a,const pair<pi,int>& b){
	double left=a.fr.fr+(1.0-a.fr.sc/100.0)*b.fr.fr,
		right=b.fr.fr+(1.0-b.fr.sc/100.0)*a.fr.fr;
	if(abs(left-right)<1e-5) return a.sc<b.sc;
	return left<right;
}
int res[1005];
int main(){
	int t;scanf("%d",&t);
	int setn=0;
	while(t--){
		int n;scanf("%d",&n);
		REP(i,n) scanf("%d",&lev[i].fr.fr);
		REP(i,n) scanf("%d",&lev[i].fr.sc);
		REP(i,n) lev[i].sc=i;
		++setn;
		printf("Case #%d:",setn);

		sort(lev,lev+n,comp);
		REP(i,n) printf(" %d",lev[i].sc);
		putchar('\n');
	}
		
	
	return 0;
}



