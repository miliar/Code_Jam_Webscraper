#include <string>
#include <vector>
#include<sstream>
#include<iostream>
#include<fstream>
#include<algorithm>
#include<stack>
#include<queue>
#include<deque>
#include<numeric>
#include<functional>
#include<list>
#include<cstdio>
#include<cstring>
#include<set>
#include<map>
#include<cstdlib>
#include<cmath>
#include<climits>
#define REP(num,num2) for(int num=0;num<(int)num2;++num)
#define REPN(num,num2,init) for(int num=init;num<(int)num2;++num)
#define FOR(itr,data) for(__typeof((data).begin()) itr=(data).begin();itr!=(data).end();++itr)
#define ITR(tp) __typeof((tp).begin())
#define ALL(typ) (typ).begin(),(typ).end()
#define pb push_back
#define mp make_pair
#define fr first
#define sc second
#define SPR(x) ((x)*(x))
#define EXIST(s,e) ((s).find(e)!=(s).end())
#define INF ((int)1e9)
#define dump(x)  cerr << #x << " = " << (x) << endl;
#define debug(x) cerr << #x << " = " << (x) << " (L" <<__LINE__ << ")" << " " << __FILE__ << endl;
#define prl cerr<<"called:"<< __LINE__<<endl;
using namespace std;
int dx[]={1,0,-1,0},dy[]={0,1,0,-1};
typedef long long int lint;
typedef long double ld;
typedef vector<int> vi;
typedef vector<vector<int> > vvi;
typedef vector<pair<int,int> > vp;
typedef pair<int,int> pi;
typedef vector<string> vs;
const ld PI  = acos(-1.0);
int main(){
	FILE* fp=fopen("out.txt","w");
	int t;scanf("%d",&t);
	REP(setn,t){
		int x,s,r,tt,n;scanf("%d%d%d%d%d",&x,&s,&r,&tt,&n);
		ld t=tt;
		int sum=0;
		vector<pair<ld,ld> > walk;
		REP(i,n){
			int b,e,w;scanf("%d%d%d",&b,&e,&w);
			sum+=e-b;
			walk.pb(mp(w,e-b));
		}
		sum=x-sum;
		dump(sum);
		walk.pb(mp(0,sum));
		sort(ALL(walk));
		ld res=0;
		REP(i,walk.size()){
			if(walk[i].sc>t*(walk[i].fr+r)){
				res+=t;
				walk[i].sc-=(ld)t*(walk[i].fr+r);
				res+=(ld)walk[i].sc/(walk[i].fr+s);
				t=0;
			}else{
				res+=(ld)walk[i].sc/(walk[i].fr+r);
				t-=(ld)walk[i].sc/(walk[i].fr+r);
			}
		}
		printf("Case #%d: %.7f\n",setn+1,(double)res);
		fprintf(fp,"Case #%d: %.7f\n",setn+1,(double)res);
	}
	return 0;
}



