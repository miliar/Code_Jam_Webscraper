#include <algorithm> 
#include <cassert>
#include <cctype> 
#include <cstdio> 
#include <cstdlib> 
#include <cmath> 
#include <cstring> 
#include <iostream>
#include <map> 
#include <set> 
#include <string> 
#include <sstream>
#include <queue> 
#include <vector> 
using namespace std;

int T, N, res;
vector<vector <int> > R;
int MOD=100003;
map <pair<int,int>, int> cn;

int cnk(int n, int k)
{
	if (cn.find(make_pair(n,k)) != cn.end()) return cn[make_pair(n,k)];
	int res=0;
	if (n<k) res=0;
	else if (n==k) res=1;
	else if (k<0) res=0;
	else if (n==1) res=1;
	else res=cnk(n-1,k-1)+cnk(n-1,k);
	res %= MOD;
	cn.insert(make_pair(make_pair(n,k), res));
	return res;
}


int get(int i, int j)
{
	if (R[i][j]!=-1) return R[i][j];
	if (j==1) {R[i][j]=0; return 0;}
	if (i==1) {R[i][j]=1; return 1;}
	int r=0;
	for (int k=1; k<=i-1;k++)
	{
		r += (get(i-k,i)*cnk(j-i-1,k-1) %MOD);
		r %= MOD;
	}
	R[i][j]=r;
	return r;
}


void solve()
{
	R.clear();	
	vector<int> t;
	t.resize(N+1,-1);
	R.resize(N+1, t);

	res=0;
	for(int i=1; i<=N-1; i++)
	{ 
		res += get(i,N);
		res %=MOD;
	}

}

void write(int i)
{
	printf("Case #%d: %d\n", i,res);


}
int main()
{
	freopen("C-small.in", "r", stdin);
	freopen("C-small.out", "w", stdout);


	scanf("%d",&T);
	
	for (int i=0; i<T; i++)
	{
		scanf("%d",&N);
		solve();
		write(i+1);
	}
	return 0;
}
