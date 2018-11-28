#include <iostream>
#include <cstring>
#include <stdio.h>
#include <algorithm>

using namespace std;
int ca = 1,t,N,L,H,oth[105],ans;

int main()
{
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);

	cin>>t;
	while(t--)
	{
		cout<<"Case #"<<ca++<<": ";
	
		scanf("%d %d %d",&N,&L,&H);

		for(int i = 0;i < N;++i) scanf("%d",&oth[i]);

		bool flag = true;

		for(int i = L;i <= H;++i)
		{
			flag = true;

			for(int k = 0;k < N;++k)
			{
				if((i % oth[k] != 0) && (oth[k] % i != 0))
				{
					flag = false;
					break;
				}
			}

			if(flag == true) {ans = i; break;}
		}

		if(flag )
		{
			printf("%d\n",ans);
		}
		else
		{
			printf("NO\n");
		}

	}
	return 0;
}