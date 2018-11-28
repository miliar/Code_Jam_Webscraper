#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#define REP(i,m) for(int i=0;i<m;++i)
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
int n,d;
pi vine[10005];
int pos[10005];
int main(){
	int t;scanf("%d",&t);
	REP(setn,t){
		printf("Case #%d: ",setn+1);
		scanf("%d",&n);
		REP(i,n) scanf("%d%d",&vine[i].fr,&vine[i].sc);
		sort(vine,vine+n);
		scanf("%d",&d);
		memset(pos,-1,sizeof(pos));
		pos[0]=min(vine[0].fr,vine[0].sc);
		int suc=0;
		REP(i,n) if(pos[i]>=0){
			if(vine[i].fr+pos[i]>=d) suc=1;
			for(int j=i+1;j<n;++j) if(vine[i].fr+pos[i]>=vine[j].fr){
				pos[j]=max(pos[j],min(vine[j].sc,vine[j].fr-vine[i].fr));
			}
		}
		if(suc) puts("YES");
		else puts("NO");
	}

	return 0;
}



