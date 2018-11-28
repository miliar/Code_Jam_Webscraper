#include<iostream>
#include<algorithm>
#include<cassert>
#include<utility>
#include<limits>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<sstream>
#include<cmath>
#include<ctime>
#include<vector>
#include<bitset>
#include<string>
#include<map>
#include<set>
#include<iomanip>
#include<queue>
#include<stack>
#include<numeric>
using namespace std;
typedef long long ll;
#define EPS (1e-8)
#define ALL(x) (x).begin(),(x).end()
#define AS assert
#define clr clear
#define PB push_back
#define SZ(x) ((int)(x).size())
#define MP make_pair
#define X first
#define Y second
#define PII pair<int,int>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define FORD(i,b,c) for(int (i)=(b);(i)>=c;(i)--)
#define REPD(i,c) FORD(i,c,0)
#define FOR(i,b,c) for(int (i)=(b);(i)<(c);(i)++)
#define REP(i,c) FOR(i,0,c)
#define PQ priority_queue
#define LL(x) ((x)<<1)
#define RR(x) ((x)<<1|1)
#define READ freopen("data.in","r",stdin)
#define see(x) (cerr<<"[Line:"<<__LINE__<<"]: "<<#x<<"="<<x<<'\n')
#ifndef INT_MAX
#define INT_MAX (numeric_limits<int>::max())
#define INT_MIN (numeric_limits<int>::min())
#endif
#define ll_max (numeric_limits<long long>::max())
#define ll_min (numeric_limits<long long>::min())
#define CB __builtin_popcount
//prime 999983 100003 899981 900001 900007
const int dm[8][2]={{0,1},{-1,1},{-1,0},{-1,-1},{0,-1},{1,-1},{1,0},{1,1}};
//const int dm[8][2]={{2,-1},{2,1},{1,2},{-1,2},{-2,1},{-2,-1},{-1,-2},{1,-2}};
//const int dm[4][2]={{0,1},{1,0},{-1,0},{0,-1}};
template<class itype,class otype>void convert(otype&out,const itype&in){istringstream str(in);str>>out;}//slow
int dp[120][120][120];
void init(){
	for(int i=0;i<120;i++)
		for(int j=0;j<120;j++)
			for(int k=0;k<120;k++)
				dp[i][j][k]=INT_MAX;
}
vector<pair<char,int> >info;
struct dalong{
	int poso,posb,idx;
	dalong(){}
	dalong(int poso,int posb,int idx):poso(poso),posb(posb),idx(idx){}
};
int main(){
	int T,cas=0;
	scanf("%d",&T);
	while(T--){
		cas++;
		int n;
		info.clear();
		pair<char,int>inp;
		init();
		scanf("%d",&n);
		for(int i=0;i<n;i++){
			scanf(" %c%d",&inp.first,&inp.second);
			info.push_back(inp);
		}
		dp[1][1][0]=0;
		queue<dalong>Q;
		dalong S,E;
		Q.push(dalong(1,1,0));
		while(Q.empty()==0){
			S=Q.front();
			Q.pop();
			int val=dp[S.poso][S.posb][S.idx];
#define check(x) (x.poso>=1&&x.poso<=100&&x.posb>=1&&x.posb<=100&&x.idx<=n)
			if(info[S.idx].first=='O'&&S.poso==info[S.idx].second){
				E=S;
				E.idx++;
				for(int i=0;i<8;i++){
					E.posb=dm[i][0]+S.posb;
					if(check(E)&&dp[E.poso][E.posb][E.idx]>val+1){
						dp[E.poso][E.posb][E.idx]=val+1;
						Q.push(E);
					}
				}
			}
			if(info[S.idx].first=='B'&&S.posb==info[S.idx].second){
				E=S;
				E.idx++;
				for(int i=0;i<8;i++){
					E.poso=dm[i][0]+S.poso;
					if(check(E)&&dp[E.poso][E.posb][E.idx]>val+1){
						dp[E.poso][E.posb][E.idx]=val+1;
						Q.push(E);
					}
				}
			}
			for(int i=0;i<8;i++){
				E.poso=dm[i][0]+S.poso;
				E.posb=dm[i][1]+S.posb;
				E.idx=S.idx;
				if(check(E)&&dp[E.poso][E.posb][E.idx]>val+1){
					dp[E.poso][E.posb][E.idx]=val+1;
					Q.push(E);
				}
			}
		}
		int ret=INT_MAX;
		for(int i=0;i<120;i++)
			for(int j=0;j<120;j++)
				ret=min(ret,dp[i][j][n]);
		printf("Case #%d: %d\n",cas,ret);
	}
}
