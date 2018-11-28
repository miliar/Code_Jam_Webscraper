#include<stdio.h>
#include<stdlib.h>
#include<map>
using namespace std;
map<int,int> m;
int main()
{
	freopen("c-small.in","r",stdin);
	freopen("c-small.out","w",stdout);
	int tt,t;
	scanf("%d",&tt);
	for(t=1;t<=tt;t++)
	{
		int n;
		scanf("%d",&n);
		m.clear();
		for(int i=0;i<n;i++)
		{
			int a,b;
			scanf("%d %d",&a,&b);
			m[a]=b;
		}
		int cnt=0;
		map<int,int>::iterator ii;
		while(1)
		{
			bool g=0;
			for(ii=m.begin();ii!=m.end();ii++)
			{
				int iii = ii->first;
				if(ii->second>1)
				{
					m[iii]-=2;
					m[iii-1]++;
					m[iii+1]++;
					g=1;
					break;
				}
			}
			if(g==0) break;
			cnt++;
		}

		printf("Case #%d: %d\n",t,cnt);
	}
	return 0;
}
