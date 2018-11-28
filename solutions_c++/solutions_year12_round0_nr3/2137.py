// <-------------------[sWitCHcAsE]---------------------->
#include<cstdio>
#include<iostream>
#include<algorithm>
#include<cstdlib>
#include<cmath>
#include<cassert>
#include<vector>
#include<map>
#include<cstring>
#include<cassert>
#include<queue>
#include<set>
#define FOR(i,n) for(int i=0;i<n;i++)
#define FORS(i,a,n) for(int i=a;i<n;i++)
#define ERR(x) cerr<<#x<<" "<<x<<endl
#define pb push_back
#define FOREACH(it,x) for(typeof((x).begin()) it=(x).begin();it!=(x).end();it++)
using namespace std;

typedef vector<int> VI;
typedef long long ll;
typedef long double ld;
int A,B;
set<int> mem[2000005];

int solve(int n) {
	int ans = 0;
	return distance(mem[n].begin(), mem[n].upper_bound(B));
	cerr<<"Solve with B "<<B<<endl;
	FOREACH(it,mem[n]) {
		cerr<<"Set of "<<n<<" contains "<<*it<<" ";
		if ( *it <= B)ans++;
		if ( *it > B)break;
	}
	cerr<<endl;
	return ans;
}
int main(int argc,char** args)
{
	int kases=0,T;
	scanf("%d",&T);
	ll ans = 0;
	int Tens[10];
	Tens[1]=1;
	FORS(i,2,8) Tens[i]=10*Tens[i-1];
	int tmp,d;
#define MAX 2000001
	for(int i = 1; i <=MAX; i++) {
		tmp = i;
		d=0;
		while(tmp)d++,tmp/=10;
		for(int j = 1; j<d; j++) {
			tmp = (i%Tens[d-j+1]);
			tmp*=Tens[j+1];
			tmp+=i/Tens[d-j+1];
			if ( tmp>i) {
				mem[i].insert(tmp);
			}
		}
	}
	while(T--) {
		cerr<<"Done with Case "<<kases<<endl;
		kases++;
		cout<<"Case #"<<kases<<": ";
		scanf("%d %d", &A, &B);
		ans = 0;
		for(int i=A;i<=B;i++) {
			ans+= solve(i);
		}
		cout<<ans<<endl;
	}

}
