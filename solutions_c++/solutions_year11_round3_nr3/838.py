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
int a[100000];
int main()
{
int t;
cin>>t;
for(int tt=1;tt<=t;tt++)
{
	int n,l,h;
	cin>>n>>l>>h;
	for(int i=0;i<n;i++)
		cin>>a[i];
	int ans;
	for(ans=l;ans<=h;ans++)
	{
		for(int i=0;i<n;i++)
			if(!(a[i]%ans==0||ans%a[i]==0))
				goto l1;
	printf("Case #%d: %d\n",tt,ans);
	goto l2;
l1:;
	}
	if(ans>h)
		printf("Case #%d: NO\n",tt);
l2:;
}
return 0;
}
