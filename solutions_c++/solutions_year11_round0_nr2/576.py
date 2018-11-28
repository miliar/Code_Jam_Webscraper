#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

bool ok(char ch1,char ch2,char t[])
{
	if(ch1 == t[0] && ch2 == t[1] )
		return true;
	if(ch1 == t[1] && ch2 == t[0])
		return true;

	return false;
}

char zuhe[50][5];
char kill[50][5];
int main()
{

	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int cas;
	scanf("%d",&cas);
	int i,j;
	int kk = 1;
	int k;
	int c;
	int d;

	while(cas --)
	{
		scanf("%d",&c);

		for(i=0;i<c;i++)
		{
			scanf("%s",zuhe[i]);
		}

		scanf("%d",&d);

		for(i=0;i<d;i++)
		{
			scanf("%s",kill[i]);
		}

		char a[105];
	
		string ans;

		int lena;

		scanf("%d",&lena);
		
		scanf("%s",a);
		
		ans = "";
		
		ans += a[0];

		for(i=1;i<lena;i++)
		{
			int len = ans.size();

			int mark = 0;

			for(j=0;j<c;j++)
			{
				if(ok(ans[len - 1],a[i],zuhe[j]) )
				{
					mark = 1;
					ans[len - 1] = zuhe[j][2];
					break;
				}
			}
			if(mark )
				continue;

			for(j=0;j<len;j++)
			{
				for(k=0;k<d;k++)
				{
					if(ok(ans[j],a[i],kill[k]) )
					{
						mark = 1;
						ans = "";
						break;
					}
				}
				if(mark)
					break;
			}
			if(mark == 0)
				ans += a[i];
		}
		
		int len = ans.size();

		printf("Case #%d: ",kk ++);

		if(len == 0)
		
			printf("[]\n");

		else if(len == 1)

			printf("[%c]\n",ans[0]);
		else
		{
			printf("[%c",ans[0]);

			for(i=1;i<len;i++)
			
				printf(", %c",ans[i]);

			printf("]\n");
		}

	}

	return 0;
}