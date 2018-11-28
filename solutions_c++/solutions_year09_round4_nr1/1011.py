#include <stdio.h>
#include <vector>
#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <functional>
using namespace std;

char s[100];
int a[100];	

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	//
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			scanf("%s",s);
			int t=n-1;
			while((t>0)&&(s[t]=='0'))
				t--;
			a[i]=t;
		}
		int res=0;
		for(int i=0;i<n;i++)
		{
			int t=i;
			while(a[t]>i)
				t++;
			while(t>i)
			{
				res++;
				swap(a[t-1],a[t]);
				t--;
			}
		}
		printf("Case #%d: %d\n",t,res);
	}
	//
	return 0;
}