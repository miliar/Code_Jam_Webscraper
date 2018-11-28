#include <iostream>
#include <algorithm>
using namespace std;
#define tiao system("pause")

int t,n;
char a[111];
int len;
char s[111];
int b[111];
char ss[111];
char wb[111];
bool visited[111];

int main(void)
{
	int i,j,k,ci,cici,cicici;
	
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	
	scanf("%d",&t);
	for (int cb=1; cb<=t; cb++)
	{
		scanf("%s",s);

		len = strlen(s);
		strcpy(a,s);
		sort(a,a+len);
		bool isCB = true;
		for (i=0; i<len; i++)
		{
			if (s[i] < s[i+1])
			{
				isCB = false;
				break;
			}
		}
		
		if (isCB)
		{
			if (a[0] != '0')
			{
				printf("Case #%d: %c0",cb,a[0]);
				for (i=1; i<len; i++) printf("%c",a[i]);
				printf("\n");
				continue;
			}
			else
			{
				for (i=0; i<len; i++)
					if (a[i] != '0')
					{
						printf("Case #%d: %c0",cb,a[i]);
						for (j=0; j<len; j++)
							if (i != j)
							{
								printf("%c",a[j]);
							}
						printf("\n");
						break;
					}
				continue;
			}
		}
		
		strcpy(wb,a);
		reverse(wb,wb+len);
		
		memset(visited,0,sizeof(visited));
		for (i=0; i<len; i++)
		{
			for (j=0; j<len; j++)
			{
				if (!visited[j] && s[i] == a[j])
				{
					b[i] = j;
					visited[j] = true;
					break;
				}
			}
		}		
		
		bool isOK = false;
		memset(ss,0,sizeof(ss));
		while(next_permutation(b,b+len))
		{
			for (i=0; i<len; i++)
				ss[i] = a[b[i]];
			if (strcmp(ss,s) > 0)
			{
				isOK = true;
				printf("Case #%d: %s\n",cb,ss);
				break;
			}
		}
		
		if (!isOK)
		{
			if (a[0] != '0')
			{
				printf("Case #%d: %c0",cb,a[0]);
				for (i=1; i<len; i++) printf("%c",a[i]);
				printf("\n");
				continue;
			}
			else
			{
				for (i=0; i<len; i++)
					if (a[i] != '0')
					{
						printf("Case #%d: %c0",cb,a[i]);
						for (j=0; j<len; j++)
							if (i != j)
							{
								printf("%c",a[j]);
							}
						printf("\n");
						break;
					}
				continue;
			}
		}
	}

//	tiao;
	return 0;
}
