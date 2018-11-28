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
int a[2000];
int main()
{
int t,tt;
cin>>t;
for(tt=1;tt<=t;tt++)
{
	mset(a);
	int n;
	cin>>n;
	int ans=0;
	int sum=0;
	for(int i=0;i<n;i++)
	{
		cin>>a[i];
		ans=ans^a[i];
		sum+=a[i];
	}
	if(ans!=0)
		printf("Case #%d: NO\n",tt);
	else{sort(&a[0],&a[n]);
	printf("Case #%d: %d\n",tt,sum-a[0]);
	}
	
	
}
	
return 0;
}
