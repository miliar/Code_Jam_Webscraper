#include<iostream>
#include<algorithm>
#include<cstdio>
#include<cstring>
#include<vector>
#include<complex>
#define REP(i,m) for(int i=0;i<m;++i)
#define pb push_back
#define mp make_pair
#define EPS (1e-3)
#define fr first
#define sc second
#define dump(x)  cerr << #x << " = " << (x) << endl
#define prl cerr<<"called:"<< __LINE__<<endl
using namespace std;
static const int INF =500000000; 
template<class T> void debug(T a,T b){ for(;a!=b;++a) cerr<<*a<<' ';cerr<<endl;}
typedef long long int lint;
typedef pair<int,int> pi;
int r[1005];
int n,w,h;
typedef complex<double> P;
P p[1005],q[1005];
pi rank[1005];
int main(){
	int t;scanf("%d",&t);
	REP(setn,t){
		printf("Case #%d:",setn+1);
		scanf("%d%d%d",&n,&w,&h);
		REP(i,n){
			scanf("%d",&r[i]);
			rank[i]=mp(r[i],i);
		}
		sort(rank,rank+n,greater<pi>());
		const int MX=1000000000;
		REP(i,n){
			int flag=1;
			while(flag){
cont:;

			p[i]=P(w*(double)(rand()%MX)/MX,h*(double)(rand()%MX)/MX);
			REP(hoge,100){
				flag=0;
				REP(j,i) if(abs(p[j]-p[i])<=rank[i].fr+rank[j].fr+EPS){
					double exe=r[i]+r[j]+EPS*2-abs(p[i]-p[j]);
					P dif=p[i]-p[j];
					double ab=abs(dif);
					dif.real()/=ab;dif.imag()/=ab;
					p[i]+=dif*exe;
					flag=1;
				}
				if(p[i].real()<EPS || p[i].real()>=w-EPS || p[i].imag()<EPS || p[i].imag()>=h-EPS)
					goto cont;
				}
			}

		}

		REP(i,n) q[rank[i].sc]=p[i];
		REP(i,n) printf(" %.8f %.8f",q[i].real(),q[i].imag());
		putchar('\n');

	}
	return 0;
}




