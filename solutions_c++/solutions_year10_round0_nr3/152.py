#include <iostream>

using namespace std;

int n,k,r,cn;
__int64 ans;
int fee[1005];
__int64 feel[1005];
__int64 sumf[1005];
int next[1005];


void calc(int t){
	int p = 0;
	int now = t;
	for(int i=0;i<n;i++){
		if(p+fee[now]>k)break;
		p+=fee[now];
		now = (now+1)%n;
	}
	next[t] = now;
	feel[t] = p;
}
int main(){
	freopen("result.out","w",stdout);

	cin>>cn;
	for(int ccn=1;ccn<=cn;ccn++){
		cin>>r>>k>>n;
		for(int i=0;i<n;i++) scanf("%d",fee+i);

		for(int i=0;i<n;i++){
			sumf[i] = 0;
			calc(i);
		}

		int now = 0;
		ans = 0;
		for(int i=0;i<r;i++){
			ans += feel[now];
			now = next[now];
		}
		printf("Case #%d: %I64d\n",ccn,ans);
		
	}
	return 0;
}