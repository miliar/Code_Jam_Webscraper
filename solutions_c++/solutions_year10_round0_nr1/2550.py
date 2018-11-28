#include <iostream>
#include <cstring>
using namespace std;
int main()
{
	//freopen("D://A-small-attempt0.in","r",stdin);
	//freopen("D://1.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		int n,k;
		scanf("%d%d",&n,&k);
		int x=0;
		for(int j=0;j<n;j++)
		{
			x=(x<<1)+1;
		}
		k=k&x;
		if(k!=x)
			printf("Case #%d: OFF \n",i+1);
		else
			printf("Case #%d: ON \n",i+1);
	}
	return 0;
}