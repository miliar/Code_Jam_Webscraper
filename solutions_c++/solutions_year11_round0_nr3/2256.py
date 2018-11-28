#include <set>   
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
#include <queue>   
#include <map> 
#include <string.h> 
#include <queue> 
using namespace std;


int arr[1001];
int main()
{
	freopen("1.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T,i,cas,n;
	scanf("%d",&T);
	for(cas=1;cas<=T;cas++)
	{
		int sm,all=0;
		scanf("%d",&n);
		for(i=0;i<n;i++)
		{
			scanf("%d",&arr[i]);
			all+=arr[i];
			if(i==0 || sm > arr[i] )
			{
				sm=arr[i];
			}
		}
		int same=0;
		for(i=0;i<n;i++)
		{ 
			int c=same;
			vector<int>str;
			while(c || arr[i] )
			{
				if( (c%2==1&&arr[i]%2==0) || (c%2==0&&arr[i]%2==1) )
				{
					str.push_back(1);
				}
				else
				{
					str.push_back(0);
				}
				c/=2;
				arr[i]/=2;
			}
			same=0;
			for(int ii=str.size()-1;ii>=0;ii--)
			{
				same=same*2+str[ii];
			}
		}
		if(same==0)
		{
			printf("Case #%d: %d\n",cas,all-sm);
		}
		else
		{
			printf("Case #%d: NO\n",cas);
		}
	}
	return 0;
}
