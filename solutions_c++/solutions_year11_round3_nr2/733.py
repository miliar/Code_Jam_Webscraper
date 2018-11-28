#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back


int main(){
	long long int tc, n, L, t, c, a[2000], b[2000];
	long long int	ans;
	scanf("%lld",&tc);
	REP(tt,tc){
		ans=0;
		scanf("%lld%lld%lld%lld",&L,&t,&n,&c);
		REP(i,c)scanf("%lld",&b[i]);
		REP(i,n)a[i]=b[i%c];
		REP(i,n)ans+=a[i]*2;
		if(L==1){
			long long int tmp=0, m=0, bef;
			bool f=false;
			REP(i,n){
				bef=tmp;
				tmp+=a[i]*2;
				if(f)m=max(m,a[i]);
				else if(tmp>=t){
					m=a[i]-(t-bef)/2;
					f=true;
				}
			}
			ans-=m;
		}
		if(L==2){
			long long int tmp=0, m=0, bef;
			bool f=false;
			long long int c[2000];
			REP(i,n){
				bef=tmp;
				tmp+=a[i]*2;
				if(f)c[i]=a[i];
				else if(tmp>=t){
					c[i]=a[i]-(t-bef)/2;
					f=true;
				}
				else c[i]=0;
				//m=max(m,c[i]);
				long long int ex=0, bex=0;
				bool ch=false;
				for(int j=i+1;j<n;j++){
					/*					bex=ex;
					ex+=a[j]*2;
					if(ch)m=max(m,c[i]+a[j]);
					else if(ex>=t){
						m=max(m,c[i]+(a[j]-(t-bex)/2));
						ch=true;
						}*/
					m=max(m,c[i]+a[j]);
				}
			}
			ans-=m;
		}
		printf("Case #%d: %lld\n",tt+1,ans);
	}
	return 0;
}
