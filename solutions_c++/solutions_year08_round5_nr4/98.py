//{{{
#include <vector> 
#include <list> 
#include <map> 
#include <set> 
#include <deque> 
#include <queue> 
#include <stack> 
#include <bitset> 
#include <valarray> 
#include <algorithm> 
#include <functional> 
#include <numeric> 
#include <utility> 
#include <complex> 
#include <memory> 
#include <new> 
#include <iterator> 
#include <limits> 
#include <sstream> 
#include <iostream> 
#include <iomanip> 
#include <cstdio> 
#include <cmath> 
#include <cstdlib> 
#include <cstring> 
#include <ctime> 
#include <cassert> 
#include <cctype> 
using namespace std;
//}}}
const int maxh=10007;
int fact[maxh];
int pow_mod(int a,int b,int c){
	int r=1;
	while(b){
		if(b&1)
			r=r*a%c;
		a=a*a%c;
		b>>=1;
	}
	return r;
}
int mod_inverse(int a,int b){
	return pow_mod(a,b-2,b);
}
int fact_mod(int a,int b){
	return pow_mod(fact[b-1],a/b,b)*fact[a%b]%b;
}
int get_factors(int a,int b){
	int r=0;
	while(a/=b)
		r+=a;
	return r;
}
int solve(int A,int B){
	if(2*A<B||(2*A-B)%3!=0)
		return 0;
	if(2*B<A||(2*B-A)%3!=0)
		return 0;
	int X=(2*A-B)/3,Y=(2*B-A)/3;
	if(get_factors(X+Y,maxh)>get_factors(X,maxh)+get_factors(Y,maxh))
		return 0;
	int a=fact_mod(X+Y,maxh);
	int b=mod_inverse(fact_mod(X,maxh),maxh);
	int c=mod_inverse(fact_mod(Y,maxh),maxh);
	return a*b%maxh*c%maxh;
}
int main(){
	int tests;
	fact[0]=1;
	for(int i=1;i<maxh;i++)
		fact[i]=fact[i-1]*i%maxh;
	scanf("%d",&tests);
	for(int t=1;t<=tests;t++){
		int X,Y,n;
		scanf("%d%d%d",&X,&Y,&n);
		vector<pair<int,int> > A(n);
		for(int i=0;i<n;i++){
			scanf("%d%d",&A[i].first,&A[i].second);
			A[i].first--,A[i].second--;
		}
		if(X==1&&Y==1){
			printf("Case #%d: %d\n",t,1);
			continue;
		}
		int ret=0;
		for(int i=0;i<1<<n;i++){
			vector<pair<int,int> > B;
			for(int j=0;j<n;j++)
				if(1<<j&i)
					B.push_back(A[j]);
			B.push_back(make_pair(0,0));
			B.push_back(make_pair(X-1,Y-1));
			sort(B.begin(),B.end());
			int ans=1;
			for(int j=1;j<B.size();j++){
				if(B[j].first<=B[j-1].first||B[j].second<=B[j-1].second){
					ans=0;
					break;
				}
				ans=ans*solve(B[j].first-B[j-1].first,B[j].second-B[j-1].second)%maxh;
			}
			if(B.size()%2==0)
				ret=(ret+ans)%maxh;
			else
				ret=(ret+maxh-ans)%maxh;
		}
		printf("Case #%d: %d\n",t,ret);
	}
scanf("%*s");
	return 0;
}
