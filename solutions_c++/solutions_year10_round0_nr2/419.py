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


int gcd(int a,int b)
{
	while(b!=0)
	{
		int t = a%b;
		a = b;
		b = t;
	}
	return a;
}

int max(int a,int b){return a>b?a:b;}
int main()
{
	//freopen("A-small-attempt0.in","r",stdin);freopen("A2-small-output.txt","w",stdout);
	freopen("B-small-attempt6.in","r",stdin);freopen("B2-small-output.txt","w",stdout);
	//freopen("A-large.in","r",stdin);freopen("A-large-output.txt","w",stdout);

	int T ;
	scanf("%d",&T);
	int nums[10];

	for(int Case=1;Case<=T;Case++)
	{
		int n ;
		scanf("%d",&n);
		int i=0;
		for(i=0;i<n;i++)
			scanf("%d",&nums[i]);
		int j=0;
		int ret = abs(nums[0]-nums[1]);
		
		for(i=0;i<n;i++)for(j=i+1;j<n;j++)
			ret = gcd(ret,abs(nums[i]-nums[j]));

		int ans = 0;
		for(i=0;i<n;i++)
			ans = max(ans,(ret-nums[i]%ret)%ret);
		printf("Case #%d: %d\n",Case,ans);
	}
}