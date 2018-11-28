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
#include <ctime>
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

#pragma comment(linker, "/STACK:400000000")

#define EPS 1e-9
#define INF MOD
#define MOD 1000000007LL
#define fir first
#define foreach(it,X) for(it=X.begin();it!=X.end();it++)
#define iss istringstream
#define ite iterator
#define ll long long
#define mp make_pair
#define rep(i,n) rep2(i,0,n)
#define rep2(i,m,n) for(int i=m;i<n;i++)
#define pi pair<int,int>
#define pb push_back
#define sec second
#define sh(i) (1LL<<i)
#define sst stringstream
#define sz size()
#define vi vector<int>
#define vc vector
#define vl vector<ll>
#define vs vector<string>

ll T,N,d[10010],l[10010],D;
ll maxlen[10010];

int main(){
	cin>>T;
	rep(tc,T){
		cout<<"Case #"<<tc+1<<": ";
		cin>>N;
		rep(i,N)cin>>d[i]>>l[i];
		cin>>D;
		d[N]=D;
		l[N]=1;
		N++;
		fill(maxlen,maxlen+N,0);
		maxlen[0]=d[0];
		rep(i,N){
			rep2(j,i+1,N){
				if(d[j] > d[i] + maxlen[i])break;
				maxlen[j]=max(maxlen[j],min(l[j],d[j]-d[i]));
			}
		}
		cout<<(maxlen[N-1]?"YES":"NO")<<endl;
	}
}
