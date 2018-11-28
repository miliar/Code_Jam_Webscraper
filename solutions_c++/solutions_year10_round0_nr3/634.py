#include <cstdio>
#include <algorithm>
#include <vector>
#include <cstring>
#include <string>
#include <map>
#include <cmath>
#include <set>
using namespace std;
const double PI = acos(-1.0);
const int mn=1005;

int r,k,n;
int a[mn];
long long s[mn],next[mn];

int main() {
    freopen("C-large.in", "r", stdin);
    freopen("C-large.out", "w", stdout);
    
    
	int Tn;
	scanf("%d", &Tn);
	for (int T = 1; T <= Tn; T++) {
		scanf("%d%d%d",&r,&k,&n);
		for(int i=0;i<n;i++){
            scanf("%d",a+i);
            s[i]=0;
            next[i]=0;
        }
        for(int i=0;i<n;i++){
            int p=i;
            while(p<n && s[i]+a[p]<=k)
                s[i]+=a[p++];
            if(p==n){
                p=0;
                while(p<i && s[i]+a[p]<=k)
                s[i]+=a[p++];
            }
            next[i]=p;
        }
        
        long long ans=0;
        for(int i=0,p=0;i<r;i++){
            ans+=s[p];
            p=next[p];
        }
        
		printf("Case #%d: ", T);
		printf("%I64d\n",ans);
	}
	return 0;
}
