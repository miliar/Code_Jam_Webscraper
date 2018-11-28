const int Debug = 1;
/*
 * SOUR:
 * ALGO:
 * DATE:2011 5月22 00时06分37秒
 * COMM:
 * */
#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
#include<cassert>
#include<cmath>
#include<queue>
#include<vector>
#include<map>
#include<stack>
#include<set>
using namespace std;
#define pb(x) push_back(x)
#define fi first
#define se second
#define rab(i,a,b) for(int i(a), _n(b); i <= (_n); i++)
#define rep(i,n) rab(i,0,(n)-1)
 
typedef std::vector < int >vi;
typedef std::pair < int, int > pii;
typedef long long LL;
 
template <class T> void ckmin(T &a,T b) { if (a > b) { a = b; } }
template <class T> void ckmax(T &a,T b) { if (a < b) { a = b; } }
template <class T> void pr(T &a) { cout << a << ' '; }
template <class T> void print(T &a) { a.__str__(); }
template <class T> int size(const vector<T> &v) { return (int)v.size(); }
#define fpr(...) \
	fprintf(stderr, "%s(%d)-%s: ",__FILE__,__LINE__,__FUNCTION__); \
fprintf(stderr, __VA_ARGS__);
int countbit(int n) { return n == 0 ? 0 : 1 + countbit(n & (n - 1)); }
 
const int maxint = 0x7fffffff;
const long long max64 = 0x7fffffffffffffffll;
/*Every problem has a simple, fast and wrong solution.*/
/*std::ios::sync_with_stdio(false);*/
 
char mp[1010][1010];
double wp[1010],owp[1010],oowp[1010];
int w[1010],t[1010];
int n;
int main()
{
	int Cas,ca=0;
	scanf("%d",&Cas);
	while(Cas--){
		printf("Case #%d:\n",++ca);
		scanf("%d",&n);
		int i,j,k;
		for(i=0;i<n;++i)scanf("%s",mp[i]);
		memset(w,0,sizeof(w));
		memset(t,0,sizeof(t));
		for(i=0;i<n;++i){
			for(j=0;j<n;++j){
				if(mp[i][j]!='.'){
					if(mp[i][j]=='1')t[i]++,w[i]++;
					else if(mp[i][j]=='0')t[i]++;
				}
			}
		}
		for(i=0;i<n;++i){
			if(t[i])wp[i]=w[i]*1./t[i];
			else wp[i]=0;
		}
		for(i=0;i<n;++i){
			double sum=0;
			for(j=0;j<n;++j){
				if(mp[i][j]!='.'){
					int ww=0,tt=0;
					for(k=0;k<n;++k)if(i!=k){
						if(mp[j][k]!='.'){
							if(mp[j][k]=='1')ww++;
							tt++;
						}
					}
					if(tt)sum+=ww*1./tt;
					else sum+=0;
				}
			}
			//printf("%d:%lf %d\n",i,sum,t[i]);
			if(t[i])owp[i]=sum/t[i];
			else owp[i]=0;
		}

		for(i=0;i<n;++i){
			double sum=0;
			for(j=0;j<n;++j){
				if(mp[i][j]!='.'){
					sum+=owp[j];
				}
			}
			if(t[i])oowp[i]=sum/t[i];
			else oowp[i]=0;
		}
		for(i=0;i<n;++i){
			double ans=0;
			ans=wp[i]/4+owp[i]/2+oowp[i]/4;
			printf("%.12lf\n",ans);
		}


		//for(i=0;i<n;++i)printf("%d/%d  ",w[i],t[i]);putchar(10);
		//for(i=0;i<n;++i)printf("%lf  ",wp[i]);putchar(10);
		//for(i=0;i<n;++i)printf("%lf  ",owp[i]);putchar(10);
		//for(i=0;i<n;++i)printf("%lf  ",oowp[i]);putchar(10);

	}
    return 0;
}
