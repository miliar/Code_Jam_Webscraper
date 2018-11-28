#include<iostream>
#include<string>
#include<cmath>
using namespace std;

int main()
{
	freopen("din.txt","r",stdin);
	freopen("dout.txt","w",stdout);
	int cas_num;
	scanf("%d",&cas_num);
	for(int case_num=1;case_num<=cas_num;case_num++)
	{
		printf("Case #%d: ",case_num);
		int m;
		scanf("%d",&m);
		int a[10001]={};
		for(int i=0;i<m;i++)
		{
			int x;
			scanf("%d",&x);
			a[x]++;
		}
		int maxn = m;
		for(int i=1;i<=10000;i++)
		{
			if(a[i]==0)
				continue;
			int beg = i;
			int end = 10000;
			for(int j=i+1;j<=10000;j++)
			{
				if(a[j]<a[j-1])
				{
					end=j-1;
					break;
				}
			}
			maxn = min(maxn,end-beg+1);
			for(int j=beg;j<=end;j++)
				a[j]--;
			i--;
		}
		cout<<maxn<<endl;
	}
}