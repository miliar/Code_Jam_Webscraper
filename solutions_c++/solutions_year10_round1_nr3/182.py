#include <iostream>

using namespace std;

#define N 100
bool check(int x,int y)
{
	if(x<y) swap(x,y);
	if(y==0||x/y>1) return true;
	return !check(y,x%y);
}

int main()
{
	int t;
	scanf("%d",&t);
	int cse=0;
	while(t--)
	{
		cse++;
		int a1,a2,b1,b2;
		int x,y;
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		int sum=0;
		for(x=a1;x<=a2;x++)
		{
			for(y=b1;y<=b2;y++)
			{
				if(check(x,y))
				{
					sum++;
				}
			}
		}
		printf("Case #%d: %d\n",cse,sum);

	}
	return 0;
}
