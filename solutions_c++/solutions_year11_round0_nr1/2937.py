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
struct edge{
	int to,cost;
	edge(int st,int sc){
		to=st;cost=sc;
	}
};
int main(){
	int T;scanf("%d",&T);
	FILE *fp=fopen("out.txt","w");
	REP(setn,T){
		int n;scanf("%d\n",&n);
		int time1=0,time2=0;
		int p=1,p2=1;
		REP(i,n){
			char c;int pl;scanf("%c %d\n",&c,&pl);
			if(c=='O'){
				time1+=abs(p-pl)+1;
				time1=max(time1,time2+1);
				p=pl;
			}else{
				time2+=abs(p2-pl)+1;
				time2=max(time2,time1+1);
				p2=pl;
			}
		}
		printf("Case #%d: %d\n",setn+1,max(time1,time2));
		fprintf(fp,"Case #%d: %d\n",setn+1,max(time1,time2));
	}
	return 0;
}



