#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
#include<string.h>
#include<math.h>
#include<csetjmp>
#include <bitset>
#include <cassert>
#include <cctype>
#include <climits>
#include <cmath>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>
#include <deque>
#include <fstream>
#include <functional>
#include <iomanip>
#include <iostream>
#include <limits>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <string>
#include <utility>
#include <vector>
int main()
{
	freopen("A.txt","w",stdout);
	double ans;
	int i,n,m,cs=0,k,T,t1,t2,j,c,t,f,a;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		for(ans=0,i=1;i<=n;i++)
		{
			scanf("%d",&a);
			if(a!=i) ans++;
		}
		printf("Case #%d: %.6f\n",++cs,ans);
	}
	return 0;
}