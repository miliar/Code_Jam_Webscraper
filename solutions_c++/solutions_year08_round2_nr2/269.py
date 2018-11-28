#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <map>
#include <set>
#include <queue>
#include <list>
#include <deque>
#include <stack>
#include <sstream>
#include <fstream>

#define ll long long int
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define RFOR(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define RREP(i,n) RFOR(i,0,n)
#define EACH(it,v) for(typeof(v.begin()) it=v.begin();it!=v.end();++it)
#define V(x) vector< x >
#define vi V(int)
#define vs V(string)
#define pb push_back
#define mkp make_pair
#define PII pair <int,int>
#define uli unsigned long long int
#define GI ({int t;scanf("%d",&t);t;})
#define SORT(X) sort(x.begin(),x.end())
const int INF = (int)1<<30;

using namespace std;
int prime[1001][1001];
vi primes;
bool isprime(int k) {
	if(k<2) return false;
	if(k==2 || k==3) return true;
	if(k%2==0) return false;
	for(int i=3;i*i<=k;i+=2) if(k%i==0) return false;
	return true;
}
int maxprimes[1001];
int gcd(int a,int b) {
	return !b?a:gcd(b,a%b);
}
void precompute() {
	REP(i,1001) if(isprime(i)) primes.pb(i);
	REP(i,primes.size()) {
		for(int j=1;j*primes[i]<=1000;j++)
			maxprimes[j*primes[i]]=primes[i];
	}
	REP(i,1001)
		FOR(j,i,1001)
			prime[i][j]=prime[j][i]=maxprimes[gcd(i,j)];
	//REP(i,20){REP(j,20) cout<<prime[i][j]<<" ";cout<<endl;}
	//cout<<primes.size()<<endl;
}
int p[2001],rank[2001];
vector<int>v;
void make_set(int i)
{
 p[i]=i;rank[i]=0;
}
int find_set(int x)
{
 if(x!=p[x]) p[x]=find_set(p[x]);
 return p[x];
}
void union_set(int X,int Y)
{
 int x=find_set(X);
 int y=find_set(Y);
 if(rank[x]>rank[y])p[y]=x;
 else 
 {
  p[x]=y;
  if(rank[x]==rank[y])rank[y]++;
 }
 return; 
}
int kruskal(int P)
{
 REP(i,2000)make_set(i);
 REP(i,v.size())
 	FOR(j,i+1,v.size())
		if(prime[v[i]][v[j]]>=P && find_set(i)!=find_set(j))
   		union_set(i,j);
 set<int> st;
 REP(i,v.size()) st.insert(find_set(i));
 return st.size();
}
int main() {	int T=GI;
	precompute();
	REP(t,T) {
		v.clear();
		ll A,B,P;
		cin>>A>>B>>P;
		FOR(i,A,B+1) v.pb(i);
		int ans=kruskal(P);		
		//REP(i,v.size()) cout<<find_set(i)<<endl;
		//printf("Case #%d: %d\n",t+1,ans);
		cout<<"Case #"<<t+1<<": "<<ans<<endl;
	}
	return 0;
}
