#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <queue>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <cctype>

using namespace std;
typedef long long ll;

const double PI=acos(-1.0);
const double eps=1e-11;

#define dump(x) cerr<<#x<<" = "<<(x)<<endl;

int countbit(int n) {return (n==0)?0:1+countbit(n&(n-1));}
int lowbit(int n) {return n&(n^(n-1));}
string toString(ll v) { ostringstream sout;sout<<v;return sout.str();}
string toString(int v) { ostringstream sout;sout<<v;return sout.str();}

const int M=300;

int n,sa;
int P[200][30];
int flag[200][200];

//template
int mat[M],tmat[M];
int hungry_aug(int i) {
	int v,j;
	for (j = 0 ; j < n; j++)
		if ( flag[i][j] && tmat[j]==0) {
			tmat[j]=1;v=mat[j];mat[j]=i;
			if (v==-1 || hungry_aug(v)) return 1;
			mat[j]=v;
		}
		return 0;
}
int hungry() {
	int i,k=0;
	memset(mat,-1,sizeof(mat));
	for (i = 0; i < n; i++) {
		memset(tmat,0,sizeof(tmat));
		k+=hungry_aug(i);
	}
	return k;
}
//template



bool test(int a,int b)
{
	int i;
	for (i=0;i<sa;i++) 
		if (P[a][i]>=P[b][i]) return false;
	return true;
}

int main()
{
	int i,j,k;
	int t,v;
	int cas=0;

	freopen("in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d",&t);
	while (t--)
	{
		cas++;
		scanf("%d%d",&n,&sa);	

		for (i=0;i<n;i++)
			for (j=0;j<sa;j++)
				scanf("%d",&P[i][j]);

		memset(flag,0,sizeof(flag));

		for (i=0;i<n;i++)
			for (j=0;j<n;j++)
				if (i!=j)
			{
				if (test(i,j))
					flag[i][j]=1;
			}

		int ans=n-hungry();

		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
