#include <iostream>
#include <fstream>
#include <algorithm>
#include <bitset>
#include <cassert>
#include <cctype>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <deque>
#include <iomanip>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <stack>
#include <sstream>
#include <string>
#include <vector>
using namespace std;

#define EPS 1e-9
#define INF MOD
#define MOD 1000000007LL
#define fir first
#define iss istringstream
#define sst stringstream
#define ite iterator
#define ll long long
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<n;i++)
#define pi pair<int,int>
#define pb push_back
#define sec second
#define sh(i) (1LL<<i)
#define sz size()
#define vi vector<int>
#define vc vector
#define vl vector<ll>
#define vs vector<string>

int T,A,B;

int main(){
	cin>>T;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		cin>>A>>B;
		int ans=0;
		rep2(i,A,B+1)rep2(j,i+1,B+1){
			vi v,w;
			int a=i,b=j;
			while(a)v.pb(a%10),a/=10;
			while(b)w.pb(b%10),b/=10;
			rep(k,v.sz){
				int ok=1;
				rep(l,v.sz)if(v[l]!=w[(l+k)%v.sz]){ok=0;break;}
				if(ok){ans++;break;}
			}
		}
		cout<<ans<<endl;
	}
}
