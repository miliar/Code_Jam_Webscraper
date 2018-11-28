#include <iostream>
using namespace std;

int main()
{
	freopen("C:\\Users\\Administrator\\Downloads\\C-small-attempt1.in","r",stdin);
freopen("C:\\Users\\Administrator\\Downloads\\out1.txt","w",stdout);

	int T,N;
	int s;
	int c_min;
	int sum;
	int X;
	int c =1;
	scanf("%d",&T);
	while(T--)
	{
		c_min = 1000000; sum =0;X=0;
		scanf("%d",&N);
	
		while(N--)
		{
			scanf("%d",&s);
			if(s<c_min)
			{c_min = s;}
			sum +=s;
			X= X^s;
		}
		if(X == 0)
		{
			printf("Case #%d: %d\n",c++,sum-c_min);
		}
		else
		{
			printf("Case #%d: NO\n",c++);
		}
	}
	return 0;
}