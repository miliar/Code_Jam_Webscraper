#include <algorithm>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

#define fo(i,n) for(int i=0;i<n;i++)

long long solve(){
	int n;
	scanf("%d",&n);

	vector<int> x(n),y(n);
	fo(i,n)scanf("%d",&x[i]);
	fo(i,n)scanf("%d",&y[i]);
	sort(x.begin(),x.end());
	sort(y.rbegin(),y.rend());
	long long ans=0;
	fo(i,n)ans+=x[i]*(long long)y[i];
	return ans;
}

int main(void){
	int t;
	scanf("%d",&t);
	fo(i,t)printf("Case #%d: %lld\n",i+1,solve());
	return 0;
}
