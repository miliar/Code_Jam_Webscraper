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
#define EPS (1e-7)
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
	int t;scanf("%d",&t);
	FILE* fp=fopen("out.txt","w");
	REP(setn,t){
		int r,c,d;scanf("%d%d%d",&r,&c,&d);
		vvi buf(r,vi(c));
		REP(i,r){
			REP(j,c){
				char cc;
				scanf("\n%c",&cc);
				buf[i][j]=cc-'0'+d;
			}
		}
		int sz=min(r,c);
		int res=-1;
		for(sz=min(r,c);sz>=3;--sz){
			REP(i,r-sz+1){
				REP(j,c-sz+1){
					lint sumx=0,sumy=0;
					lint div=0;
					REPN(k,i+sz,i){
						REPN(l,j+sz,j){
							sumy+=buf[k][l]*k;
							sumx+=buf[k][l]*l;
							div+=buf[k][l];
						}
					}
					sumx-=(buf[i][j]*j+buf[i][j+sz-1]*(j+sz-1)
					+buf[i+sz-1][j]*j+buf[i+sz-1][j+sz-1]*(j+sz-1));
					div-=(buf[i][j]+buf[i][j+sz-1]+buf[i+sz-1][j]+buf[i+sz-1][j+sz-1]);
					sumy-=(buf[i][j]*i+buf[i][j+sz-1]*i+buf[i+sz-1][j]*(i+sz-1)+
					buf[i+sz-1][j+sz-1]*(i+sz-1));
					double x=(double)sumx/div,y=(double)sumy/div;
					if(y>=(double)(sz-1)/2+i-EPS && y<=(sz-1)/2.0+i+EPS && 
						x>=(sz-1)/2.0+j-EPS && x<=(sz-1)/2.0+j+EPS){
							res=sz;
							goto exi;
					}
				}
			}
		}
		exi:;
		if(res==-1)
			fprintf(fp,"Case #%d: IMPOSSIBLE\n",setn+1);
		else fprintf(fp,"Case #%d: %d\n",setn+1,sz);
	}


					
	return 0;
}



