#include<iostream>
#include<cmath>
using namespace std;
int main()
{
	int t;
	freopen("C-small.in","r",stdin);
	freopen("C-small.out","w",stdout);
	scanf("%d",&t);
	int x=0;
	int n;
	while(t--)
	{
		int l,p,c;
		scanf("%d %d %d",&l,&p,&c);
		int ans =ceil(log(double(p)/double(l))/log(double(c)))-1;
		int count=0;
		while (ans>0)
		{
			ans=(ans)/2;
			count++;
		}

        
		printf("Case #%d: %d\n",++x,count);
	}
	return 0;
}



