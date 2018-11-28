#include<cstdio>
#include<cstring>
#include<cmath>
#include<cctype>
#include<vector>
#include<stack>
#include<queue>
#include<set>
#include<map>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<numeric>
#include<fstream>
using namespace std;
#define min(a,b) ((a)<(b)?(a):(b))
#define max(a,b) ((a)>(b)?(a):(b))
#define memo(a,v) memset(a,v,sizeof(a))
#define pb push_back
#define all(a) a.begin(),a.end()
#define eps (1e-9)
#define inf (1<<29)
#define i64 __int64
int a[1005];
bool vi[1005];
int main(){
	freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int i,j,cs,k,r,n,t,p,q;
	i64 s,sum,ans;
	scanf("%d",&t);
	for(cs = 1;cs<=t;cs++){
		scanf("%d %d %d",&r,&k,&n);
		for(i = 0;i<n;i++){
			scanf("%d",&a[i]);
		}
		i = 0;
		q = r;
		s = 0;
		memo(vi,0);
		sum = 0;
		while(r){
			if(vi[i]) break;
			vi[i] = 1;
			s = 0;
			for(j=0;j<n;j++,i++,i%=n){
				if(s+a[i]>k) break;
				s+=a[i];
			}
			sum+=s;
			r--;
		}
		p = i;
		if(r){
			i = 0;
			ans = 0;
			while(q){
				if(i == p) break;
				
				s = 0;
				for(j=0;j<n;j++,i++,i%=n){
					if(s+a[i]>k) break;
					s+=a[i];
				}
				q--;
				ans+=s;
			}
			q-=r;
			sum-=ans;
			r += q;
			ans+= r/q * sum;
			r%=q;
			i = p;
			while(r){
				
				s = 0;
				for(j=0;j<n;j++,i++,i%=n){
					if(s+a[i]>k) break;
					s+=a[i];
				}
				r--;
				ans+=s;
			}
		}
		else ans = sum;
		printf("Case #%d: %I64d\n",cs,ans);
	}
	return 0;
}