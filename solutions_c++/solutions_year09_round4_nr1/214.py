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


int n;
ll A[55];
ll mask[55];

int main()
{
	int i,j,k;
	int t,v;
	int cas=0;

	freopen("in","r",stdin);
	freopen("out","w",stdout);

	mask[0]=1;
	for (i=1;i<60;i++) mask[i]=mask[i-1]*2;


	scanf("%d",&t);
	while (t--)
	{
		cas++;
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			A[i]=0;
			for (j=0;j<n;j++)
			{
				scanf("%1d",&v);
				A[i]|=v*mask[j];
			}
		}
		int ans=0;
		for (i=0;i<n;i++)
		{
			for (j=i;j<n;j++)
			{
				for (k=i+1;k<n;k++)
					if (mask[k]&A[j]) break;
				if (k==n)
					 break;
			}
			ll tmp=A[j];
			for (k=j-1;k>=i;k--)
			{
				A[k+1]=A[k];
				ans++;
			}
			A[i]=tmp;
		}
		printf("Case #%d: %d\n",cas,ans);
	}
	return 0;
}
