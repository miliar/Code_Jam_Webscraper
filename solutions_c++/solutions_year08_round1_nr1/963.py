//#include <stdafx.h>

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
#include <string.h>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define MaxNum 310
bool com(int a,int b)
{
	if(a>b)return true;
	return false;
}
int main()
{
	int n;
	int t;
	scanf("%d",&t);
	
	int i,j;
	int c;
	int a[900],b[900];
	for(c=1;c<=t;c++)
	{
        scanf("%d",&n);
		for(i=0;i<n;i++)scanf("%I64d",&a[i]);
		for(i=0;i<n;i++)scanf("%I64d",&b[i]);
		sort(a,a+n);
		sort(b,b+n,com);
		__int64 sum=0;
		for(i=0;i<n;i++)
		{
			sum+=(a[i]*b[i]);
		}
		printf("Case #%d: %I64d\n",c,sum);
	}
   
	return 0;
}