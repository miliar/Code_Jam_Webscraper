#include<stdio.h>
#include<map>

using namespace std;

map< int, int > a;
int n;

int main(void)
{
	int l0, l1, l2, t1, t2;
	int T;
	int ret = 0;

	freopen("C1.in","r",stdin);
	freopen("C1.out","w",stdout);

	scanf("%d",&T);

	for(l0=1;l0<=T;l0++)
	{
		fprintf(stderr,"%d %d\n",l0,T);
		scanf("%d",&n);
		a.clear();
		for(l1=0;l1<n;l1++)
		{
			scanf("%d %d",&t1,&t2);
			a[t1] = t2;
		}

		ret = 0;
		int flag;
		while(1)
		{
			map< int, int >::iterator it;

			flag = 0;
			for(it=a.begin(); it!=a.end(); ++it)
			{
				if((it->second) >= 2)
				{
					int left = (it->first) - 1;
					int right = (it->first) + 1;

					if(a.count(left) == 0)
					{
						a[left] = 1;
					}
					else
					{
						a[left]++;
					}
					if(a.count(right) == 0)
					{
						a[right] = 1;
					}
					else
					{
						a[right]++;
					}
					ret++;
					flag = 1;

					(it->second) -= 2;
					
					if((it->second) == 0)
					{
						a.erase(it);
					}
					break;
				}
			}
			if(flag == 0) break;
		}
		printf("Case #%d: %d\n",l0,ret);
	}
}