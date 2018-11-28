#include <iostream>
#include <cmath>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,k,l,x,y,c,t,count=1,s;
	scanf("%d",&t);
	while (t--)
	{
		scanf("%d%d%d",&x,&y,&c);
		k=ceil(log(double(y)/double(x))/log(c));
		k--;
		s=0;
		while (k>0)
		{
			k=(k)/2;
			s++;
		}
		printf("Case #%d: %d\n",count++,s);
	}
}