#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>

using namespace std;


int n;
char s[1000];
int val[1000];

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,ca,kk=1;
	scanf("%d",&ca);
	while(ca--) 
	{
		scanf("%d",&n);
		for(i=1;i<=n;i++) 
		{
			scanf("%s",s+1);
			for(j=n;j>=1;j--) if(s[j]=='1') break;
			val[i]=j;
		}
		int cnt=0;
		for(i=1;i<=n;i++) 
			if(val[i]>i) 
			{
				for(j=i+1;j<=n;j++) if(val[j]<=i) break;
				if(j==n+1) break;
				for(k=j;k>i;k--) 
				{
					cnt++;
					swap(val[k],val[k-1]);
				}
			}
		printf("Case #%d: %d\n",kk++,cnt);
	}
	return 0;
}