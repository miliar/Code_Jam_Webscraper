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
		int r,c;scanf("%d%d",&r,&c);
		vector<vector<char> > buf(r,vector<char>(c)),out;
		REP(i,r){
			REP(j,c){
				scanf("\n%c\n",&buf[i][j]);
			}
		}
		out=buf;
		int fail=0;
		REP(i,r){
			REP(j,c){
				if(buf[i][j]=='.' || buf[i][j]=='/')continue;
				int failed=0;
				REP(k,2) REP(l,2) 
				if(i+k>=r || j+l>=c || buf[i+k][j+l]!='#'){
					 failed=1;}
				if(failed){
					fail=1;
					goto exi;
				}
				REP(k,2) REP(l,2)
				buf[i+k][j+l]='/';
				out[i][j]='/';
				out[i+1][j+1]='/';
				out[i+1][j]='\\';
				out[i][j+1]='\\';
			}
		}
		exi:;
		fprintf(fp,"Case #%d:\n",setn+1);
		if(fail){
			fprintf(fp,"Impossible\n");
		}else{
			REP(i,r){
				REP(j,c){
					fprintf(fp,"%c",out[i][j]);
				}
				fprintf(fp,"\n");
			}
		}
	}



	return 0;
}



