#include <stdio.h>
#include <string.h>

__int64 a[1010],c[1010],cnt[1010];
bool b[1010];

int main(){
	__int64 cas,x,i,j,r,k,n,s,sum,t,ans;
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%lld",&cas);
	for (x=1; x<=cas; x++){
		scanf("%lld%lld%lld",&r,&k,&n);
		for (i=0; i<n; i++)
			scanf("%lld",&a[i]);
		memset(b,false,sizeof(b));
		t = 0; sum = 0; i = 0;
		while (true){
			if (b[i]) break;
			c[i] = sum;
			cnt[i] = t;
			s = 0;
			b[i] = true;
			j = i;
			while (a[i]+s<=k){
				s += a[i];
				i++;
				i %= n;
				if (i==j) break;
			}
			sum += s;
			t++;
		}
		sum -= c[i];
		t -= cnt[i];
		ans = 0;
		if (r>=cnt[i]){
			r -= cnt[i];
			ans += c[i];
		}
		ans += (r/t)*sum;
		if (ans==0) i = 0;
		r %= t;
		while (r--){
			s = 0;
			j = i;
			while (a[i]+s<=k){
				s += a[i];
				i++;
				i %= n;
				if (i==j) break;
			}
			ans += s;
		}
		printf("Case #%lld: ",x);
		printf("%lld\n",ans);
	}
	return 0;
}