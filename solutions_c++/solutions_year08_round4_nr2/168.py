#include<iostream>
using namespace std;
int main()
{
	freopen("1.txt","r",stdin);
	freopen("2.txt","w",stdout);
	int zu;
	scanf("%d",&zu);
	int g=1;
	while(zu--)
	{
		int x,y,z;
		scanf("%d%d%d",&x,&y,&z);
		if(x*y<z)
		{printf("Case #%d: IMPOSSIBLE\n",g++);continue;}
		bool f=0;
		int i,j,p,q;
		for(i=(z-1)/y+1;i<=x;i++)	
		{
			for(q=(z-1)/i+1;q<=y;q++)
			{
				if(i*q==z)
				{p=j=0;f=1;goto end;}
				for(j=(i*q-z-1)/y+1;j<=x;j++)
				{
					if((i*q-z)%j==0&&(i*q-z)/j<=y)
					{f=1;p=(i*q-z)/j;goto end;}
				}
			}
		}
end:;
		if(f==0){printf("Case #%d: IMPOSSIBLE\n",g++);continue;}
		printf("Case #%d: %d %d %d %d %d %d\n",g++,0,0,i,p,j,q);
	}

}
