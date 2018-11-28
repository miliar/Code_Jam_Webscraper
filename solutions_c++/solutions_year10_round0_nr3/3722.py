#include <iostream>
#include <vector>
using namespace std;

vector<int> list,term;

int Star(int r,int k,int n)
{
	list.clear();
	term.clear();
	int i,j,g;
	for(i=0;i<n;i++)
	{
		int a;
		scanf("%d",&a);
		list.push_back(a);
	}
	int len,sum=0,Sum=0;
	len=list.size();
	for(i=0;i<r;i++)
	{
		term.clear();
		sum=0;
		for(j=0;j<len;j++)
		{
			if(sum+list[j]<=k)
			{
				sum+=list[j];
				g=j;
			}
			else break;
		}
		Sum+=sum;
		for(j=g+1;j<len;j++)
		{
			term.push_back(list[j]);
		}
		for(j=0;j<=g;j++)
		{
			term.push_back(list[j]);
		}
		list=term;
	}
	return Sum;
}

int main()
{
	freopen("C-small-attempt3.in","r",stdin);
    freopen("C-small-attempt3.out","w",stdout);
	int t,Case=0;
	scanf("%d",&t);
	while(t--)
	{
		Case++;
		int r,k,n;
		scanf("%d%d%d",&r,&k,&n);
		int sum;
		sum=Star(r,k,n);
		printf("Case #%d: %d\n",Case,sum);
	}
}
