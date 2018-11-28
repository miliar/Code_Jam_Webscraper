#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>

using namespace std;

//int mark[2000005];

int main()
{
	freopen("C2.in","r",stdin);
	freopen("C2.out","w",stdout);
	int t,i,j,k,A,B,ans,cs=0,x,y,z,v;
	int got[12];
	scanf("%d",&t);
	char s[12];
	while(t--)
	{
		scanf("%d%d",&A,&B);
		cs++;

		ans = 0;
		for(i=A;i<=B;i++)
		{
			sprintf(s,"%d",i);
			j = strlen(s) - 1;
			v = 0;
			while(j--)
			{
				x = 0, y = 1,z = 0;
				k = 0;
				while(k<=j)
					x = x*10 + s[k] - '0',k++,y*=10;
				while(s[k])
					z = z*10 + s[k] - '0',k++;
				k = z*y + x;

				if(k>i && !(k<A) && !(k>B))
				{//	printf("-> %d %d\n",i,k),
					for(x=y=0;x<v;x++)
						if(got[x] == k)
							y = 1;
					if(y==0)
					{
						ans++;
						got[v] = k;
						v++;
					}
				}
			}
		}

		printf("Case #%d: %d\n",cs,ans);
	}
	return 0;
}