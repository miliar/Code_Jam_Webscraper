#pragma comment (linker, "/STACK:90000000")
#include <string>
#include <memory.h>
#include <cassert>
#include <vector>
#include <cmath>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <sstream>
#include <utility>
using namespace std;
#define forn(i, n) for (int i = 0; i < (int)(n); ++i)
#define forv(i, v) for (int i = 0; i < (int)(v.size()); ++i)
#define fors(i, s) for (int i = 0; i < (int)(s.length()); ++i)
#define all(a) (a).begin(), (a).end()
#define pb push_back
#define mp make_pair
#define lng long long
#define eps 1e-9
#define iinf 1000000000
#define SQ(a) ((a)*(a))
#define EQ(a,b) fabs((a)-(b))<eps

int src[1100];
int n;
double dp[1100];

double solve(){
	vector<int> nums;
	forn(i,n)
		nums.pb(src[i]);
	sort(all(nums));
	forn(i,n)
		src[i]=lower_bound(all(nums),src[i])-nums.begin();
	double res=0;
	forn(i,n){
		if(src[i]==-1)
			continue;
		int p=i;
		int l=0;
		do{
			int t=src[p];
			src[p]=-1;
			p=t;
			++l;
		}while(p!=i);
		res+=dp[l];
	}
	return res;
}

int main(){
#ifdef __ASD__
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
#endif
	
	//forn(i,1000)cout<<1000-i<<' ';return 0;

	dp[0]=1e100;
	dp[1]=0;
	for(n=2;n<=1000;++n){
		dp[n]=1;
		for(int k=1;k<n;++k){
			double t=dp[k];
			if(n-k>1)
				t+=dp[n-k]-1;
			dp[n]+=t/n;
		}
		dp[n]*=1.0*n/(n-1);
	}

	int tc;
	cin>>tc;
	forn(qqq,tc){
		cin>>n;
		forn(i,n)
			cin>>src[i];
		printf("Case #%d: %.10lf\n",qqq+1,solve());
	}

    return 0;
}