#define mset(a) memset(a,0,sizeof(a))

#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
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
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
using namespace std;
int d[20000],l[20000];
long long f[20000];
int main()
{
	int t;
	cin>>t;
	for(int tt=1;tt<=t;tt++)
	{
		int n;
		cin>>n;
		mset(f);
		for(int i=1;i<=n;i++)
			cin>>d[i]>>l[i];
		int D;
		cin>>D;
		f[1]=d[1]*2;
		for(int i=1;i<=n;i++)
		{
			if(f[i]>=D)
			{
				printf("Case #%d: YES\n",tt);
				goto l1;
			}
			for(int j=i+1;j<=n&&f[i]>=d[j];j++)
			{
				int x=(l[j]>d[j]-d[i])?(d[j]-d[i]):l[j];
				f[j]=max(f[j],(long long)d[j]+x);
			}
		}
		printf("Case #%d: NO\n",tt);

l1:;


	}
    return 0;
}
