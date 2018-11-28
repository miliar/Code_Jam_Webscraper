

#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include<string.h>
using namespace std;
int main()
{
	int t;
	scanf("%d",&t);
	int i;
	for(i=0;i<t;i++)
	{
		int n,p,s,j;
		scanf("%d %d %d",&n,&s,&p);
		int ans=0;
		for(j=0;j<n;j++)
		{
			int sc;
			scanf("%d",&sc);
			int n1 = sc/3;
			int n2 = (sc-n1)/2;
			int n3 = sc-n1-n2;

			int state=0;
			if(sc%3==0 || sc%3==2)
				state=1;
	//		printf("%d %d %d\n",n1,n2,n3);
//			if(abs(n1-n2)<=1 && abs(n2-n3)<=1)
//			{
			if(n3>=p)
					ans++;
//				else if(s>0 && n3+1>=)
//			}

			else if(s>0 && n3+1>=p && n2-1>=0 && state==1)
			{
				s--;
				ans++;
			}
		}
		printf("Case #%d: %d\n",i+1,ans);

	}
	return 0;
}
