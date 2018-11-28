#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int r, k, n;
long long next[1000], profit[1000], mod[1001];
int g[1000];

void init() {
	scanf("%d %d %d ",&r, &k, &n);
	for (int i=0; i<n; i++) 
		scanf("%d ",g+i);	
}
void calc() {
	long long ans = 0;
	memset(next,-1,sizeof(next));
	memset(profit,0,sizeof(profit));
	int i;
	for (i=0; next[i]==-1 && r; i=next[i]) {
		int j=i, rest = k;
		for (j=i; rest>=g[j]; j=(j+1)%n) {			
			rest-=g[j];
			profit[i]+=g[j];
			if ((j+1)%n==i) {
				j = (j+1)%n;
				break;
			}
		}
		next[i] = j;
		r--;
		ans+=profit[i];		
	}
	if (r) {
		long long s = 0;
		int j, cnt;
		mod[0] = 0;
		for (j=i, cnt=1;; j=next[j], cnt++) {
			s+=profit[j];
			mod[cnt] = s;
			if (next[j]==i) break;
		}
		ans+=(r/cnt)*s+mod[r%cnt];
	}
	cout<<ans<<endl;
}

int main()
{
	int t;
	scanf("%d ",&t);
	for (int i=1; i<=t; i++) {
		init();
		cout<<"Case #"<<i<<": ";
		calc();
	}
	return 0;
}
