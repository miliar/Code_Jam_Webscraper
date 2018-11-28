#pragma comment(linker, "/STACK:65777216")

#include <algorithm>
#include <iostream>
#include <string>
#include<sstream>
#include<string.h>
#include <cstdio>
#include <vector>
#include <bitset>
#include <cmath>
#include <queue>
#include<stack>
#include <set>
#include <map>
#include<ctime>

using namespace std;

typedef long long ll;
typedef vector<int> vi;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef unsigned long long ull;

#define FOR(i,a,b) for (int i(a); i < (b); i++) 
#define REP(i,n) FOR(i,0,n) 
#define SORT(v) sort((v).begin(),(v).end())
#define UN(v) sort((v).begin(),(v).end()),v.erase(unique(v.begin(),v.end()),v.end())
#define CL(a,b) memset(a,b,sizeof(a))
#define pb push_back

bool u[1111111];
vi p;

int f1(ll n){
	int pr = 1;
	int to = min(n, 1000000ll);
	for(int i=2;i<=to;i++)if(!u[i]){
		int k = 0;
		ll t = 1;
		while(t*i<=n){
			t*=i;
			k++;
		}
		pr += k;
	}
	return pr;
}

int f2(ll n){
	int pr = 0;
	int to = min(n, 1000000ll);
	for(int i=2;i<=to;i++)if(!u[i]) pr++;
	return max(pr, 1);
}

int main(){ 
#ifdef LocalHost
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
#endif

	for(int i=2;i<=1000;i++)if(!u[i]){
		for(int j=i+i;j<=1000000;j+=i) u[j]=true;
	}
	for(int i=2;i<=1000000;i++)if(!u[i]) p.pb(i);

	int tc;
	cin>>tc;
	REP(TC,tc){
		ll n;
		cin>>n;
		printf("Case #%d: ",TC +1);
		cout<<f1(n) - f2(n)<<endl;
	}


/*#ifdef LocalHost
	cout<<endl<<endl<<clock()<<endl;
#endif*/
	return 0;
}