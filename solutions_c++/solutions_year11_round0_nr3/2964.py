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
	int T;scanf("%d",&T);
	FILE* fp=fopen("out.txt","w");
	REP(setn,T){
		int N;scanf("%d",&N);
		vi nums(N);
		REP(i,N){
			scanf("%d",&nums[i]);
		}
		sort(ALL(nums));
		int maxbit=1<<N;
		int res=-1;
		REPN(bit,maxbit-1,1){
			int a=0,b=0,really=0;
			REP(i,N){
				if(bit>>i&1){
					really+=nums[i];
					REP(j,21){
						if(a>>j&1 && nums[i]>>j&1){
							a^=1<<j;
						}else if(nums[i]>>j&1){
							a|=1<<j;
						}
					}
				}else{
					REP(j,21){
						if(b>>j&1 && nums[i]>>j&1){
							b^=1<<j;
						}else if(nums[i]>>j&1){
							b|=1<<j;
						}
					}
				}
			}
			if(a==b)
				res=max(really,res);
		}
		if(res!=-1)
		fprintf(fp,"Case #%d: %d\n",setn+1,res);
		else fprintf(fp,"Case #%d: NO\n",setn+1);
	}
	return 0;
}



