#include <fstream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <cstdio>
#include <string>
#include <iostream>
#include <queue>
#include <cmath>
#include <set>
#include <memory.h>

using namespace std;

vector <long long> tree;

long long rec(long long top,long long lev,vector <long long> M,long long l,long long r)
{
	if (r==l+1)
	{
		if (M[l]<=0&&M[r]<=0) return 0;
		if (M[l]<=1&&M[r]<=1) return tree[top];
		return 100000000;
	}
	long long ans=rec(2*top,lev-1,M,l,(l+r)/2)+rec(2*top+1,lev-1,M,(l+r)/2+1,r);
	for(long long i=l;i<=r;i++)
		M[i]--;
	long long c=tree[top]+rec(2*top,lev-1,M,l,(l+r)/2)+rec(2*top+1,lev-1,M,(l+r)/2+1,r);
	ans=min(ans,c);
	return ans;
}

int main()
{
//	freopen("input.txt","r",stdin);
//	freopen("output.txt","w",stdout);
	ifstream dat("input.txt");
	ofstream sol("output.txt");
	long long T;
	dat >> T;
	for(long long t=1;t<=T;t++)
	{
		long long ans=0;
		int p;
		vector < vector <long long> > pr;
		dat >> p;
		vector <long long> M(1<<p,0);
		for(long long i=0;i<(1<<p);i++)
		{
			dat >> M[i];
			M[i]=p-M[i];
		}
		reverse(M.begin(),M.end());
		tree.clear();
		for(long long i=0;i<p;i++)
		{
			for(long long j=0;j<(1<<(p-i-1));j++)
			{
				long long a;
				dat >> a;
				tree.push_back(a);
			}
		}
		tree.push_back(0);
		reverse(tree.begin(),tree.end());
//		for(long long i=0;i<tree.size();i++)
//			sol << tree[i] << "	";
//		sol << endl;
		ans=rec(1,0,M,0,(1<<p)-1);
		sol << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}

