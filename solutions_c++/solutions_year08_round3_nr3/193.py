#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include<iostream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<queue>
#include<list>
#include<bitset>
#include<cstring>
#include<climits>
#include<deque>
#include<utility>
#include <complex>
#include <numeric>
#include <functional>
#include <stack>
#include <iomanip>

using namespace std;

#define rep(i,n) for(int  i=0;i<(int)(n);++i)
long double ZERO=0;
const long double INF=1/ZERO,EPSILON=1e-12;
#define all(c) (c).begin(),(c).end() 
#define rep2(i,a,b) for(int i=(a);i<=((int)b);++i)
#define foreach(it,c) for(__typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

#define sz(v) ((int)((v).size()))
long long A[1000];
int a[500000];
long long mem[500000];

int main() {
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("c-small.txt2","wt",stdout);
	int T;
	cin>>T;
	rep(t,T)
	{
		long long n, m, X, Y , Z;
		
		cin>>n>>m>>X>>Y>>Z;
		rep(i,m)
			cin>>A[i];
		rep(i,n)
		{
			a[i]= A[i % m];
			A[i % m] = ((X * A[i % m])% Z + (Y * (i + 1))% Z) % Z;
		}
		for(int i=n-1;i>=0;i--)
		{
			mem[i]=1;
			rep2(j,i+1,n-1)
				if(a[j]>a[i])
				{
					mem[i]+=mem[j];
					mem[i]%=1000000007;
				}
		}
		long long r=0;
		rep(i,n)
			r=(r+mem[i])%1000000007;
		cout<<"Case #"<<t+1<<": "<<r<<endl;
	}
}