//BISMILLAHIRRAHMANIRRAHIM

#include <iostream>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

long long g[1009];

long long gcd(long long a,long long b) { return b?gcd(b,a%b):a ; }


long long absl(long long a) { return a>=0?a:-a ; }

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("Bs.out","w",stdout);
	
	int i,j,k,n,T,I,r;
	long long t;
	cin>>T;
	for(I=1;I<=T;I++) {
		cin>>n;
		for(i=0;i<n;i++) scanf("%Ld",&g[i]);
		t=absl(g[0]-g[1]);
		for(i=2;i<n;i++) t=gcd(t,abs(g[i]-g[i-1]));
		//cout<<t<<'\n';
		printf("Case #%d: %Ld\n",I,(g[0]%t)?(t-(g[0]%t)):0);
	}
	return 0;
}
