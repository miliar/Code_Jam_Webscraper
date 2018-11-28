#include <iostream>
#include <cstdio>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <algorithm>


using namespace std;

#define rep(i,n) for(i=0;i<(n);i++)
#define foru(i,a,b) for(i=(a);i<=(b);i++)
#define ford(i,a,b) for(i=(a);i>=(b);i--)

int n,r,limit;
int a[2000];
int b[2000];
long long eu[2000];
int tot;

int next(int x){
	if (x==n) return 1;
	else return x+1;
}

int main(){
   freopen("C-large.in","r",stdin);
   freopen("output.txt","w",stdout);
   int i,j,k,test,cases;
   scanf("%d",&test);
   cases=0;
   while (test){
		test--;
		cases++;
		printf("Case #%d: ",cases);
		scanf("%d%d%d",&r,&limit,&n);
		foru(i,1,n) scanf("%d",&a[i]);
		tot=0;
		memset(b,0,sizeof(b));
		int start=1,last;
		long long ans=0;
		
		while (1) {
			tot++;
			b[start]=tot;
			last=start;
			k=0;
			while (1) {
				if (k+a[start] <= limit) k+=a[start];
				else break;
				start=next(start);
				if (start==last) break;
			}
			ans=ans + k;
			eu[tot]=k;
			if (b[start]!=0 || r==tot) break;
		}
		if (r==tot) cout<<ans<<endl;
		else {
			r= r- tot;
			int cir= tot - b[start] + 1;
			
		//	cout<<r<<" "<<cir<<endl;
			
			long long t=0;
			foru(i,b[start],tot) t+=eu[i];
			
	//		cout<<ans<<" "<<t<<endl;
			
			ans = ans + t * (r / cir);
//			cout<<ans<<endl;
			r= r % cir;
			foru(i,b[start],b[start]+r-1) ans+=eu[i];
			
			cout<<ans<<endl;
		}
	}
   
   return 0;
}
