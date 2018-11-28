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
const double PI  = acos(-1.0);
int main(){
	FILE *fp=fopen("out.txt","w");
	int T;scanf("%d",&T);
	REP(setn,T){
		int L,t,N,C;
		scanf("%d%d%d%d",&L,&t,&N,&C);
		vi dis(N);
		REP(i,C){
			scanf("%d",&dis[i]);
			for(int j=i+C;j<N;j+=C)
				dis[j]=dis[i];
		}
		t/=2;
		vi length;
		lint res=0;
		REP(i,dis.size()) res+=dis[i];
		REP(i,N){
			if(t>0){
				if(t>=dis[i])
					t-=dis[i];
				else{
					length.pb(dis[i]-t);
					t=0;
				}
			}else{
				length.pb(dis[i]);
			}
		}
		res*=2;
		sort(ALL(length),greater<int>());
		REP(i,L){
			res-=length[i];
		}
		fprintf(fp,"Case #%d: %lld\n",setn+1,res);
	}



	return 0;
}



