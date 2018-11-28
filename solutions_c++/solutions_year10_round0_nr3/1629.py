#include <cstdio>
#include <map>
#include <algorithm>
#include <vector>
using namespace std;
int main(){
	freopen("C-large.in","r",stdin);
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d\n",&t);
	for(int tc=1; tc<=t; tc++){
		printf("Case #%d: ",tc);
		int n,k,r;
		scanf("%d %d %d\n",&r,&k,&n);
		vector<long long> a(n);
		for(int i=0; i<n; i++)
			scanf("%lld ",&a[i]);
		long long sum = 0;
		for(int i=0; i<n; i++)
			sum += a[i];
		if(sum <= (long long)k){
			printf("%lld\n",(long long)r*sum);
		}
		else{
			vector<vector<long long> > c;
			map<vector<long long>,int> d;
			vector<long long> money;
			bool dd=true;
			long long ans = 0;
			int stopindex;
			for(int i=0; i<r; i++){
				if(d.count(a)>0){
					stopindex=i;
					dd=false;
					break;
				}
				c.push_back(a);
				long long sum=0;
				int last = 0;
				for(int j=0; j<n; j++){
					if(sum+a[j]>k){
						last=j;
						break;
					}
					else
						sum+=a[j];
				}
				ans+=sum;
				money.push_back(sum);
				d[a]=i;
				rotate(a.begin(),a.begin()+last,a.end());
			}
			if(dd){
				printf("%lld\n",ans);
			}
			else{
				r--;
				int st = d[a];
				int ed = stopindex-1;
				int len = ed-st+1;
				int st2 = st-st;
				int ed2 = ed-st;
				int now2 = r-st;
				long long sum =0;
				for(int i=st; i<=ed; i++)
					sum += money[i];
				int cnt = now2/len;
				ans += (long long)(cnt-1)*sum;
				for(int i=0; i<=now2%len; i++)
					ans += money[i+st];
				printf("%lld\n",ans);
			}
		}
	}
	return 0;
}