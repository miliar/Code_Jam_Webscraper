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

int a[300][2];

int main()
{
	freopen("B-small-attempt1.in","r",stdin);
	freopen("B-small-attempt1.out","w",stdout);
	double left,right,mid,prev;
	int i,k,l,t,b1,n,d;
	scanf("%d",&t);
	for (l=0;l<t;l++)
	{
		scanf("%d%d",&n,&d);
		for (i=0;i<n;i++)
			scanf("%d%d",&a[i][0],&a[i][1]);
		left=0;right=1e10;
		for (k=0;k<300;k++)
		{
			mid=(left+right)/2;
			prev=-1e10;
			b1=1;
			for (i=0;i<n;i++)
			{
				if (a[i][0]-mid>prev+d) prev=a[i][0]-mid;
				else prev=prev+d;
				prev+=(double)(a[i][1]-1)*d;
				if (fabs(prev-a[i][0])>mid)
				{
					b1=0;
					break;
				}
			}
			if (b1==1) right=mid;
			else left=mid;
		}
		printf("Case #%d: %.2lf\n",l+1,(left+right)/2);
	}
	return 0;
}

