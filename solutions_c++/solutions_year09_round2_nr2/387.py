#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int st,t;
	char buf[1024];
	int len,i,j;
	scanf("%d",&st);
	for (t=0;t<st;++t)
	{
		scanf("%s",buf);
		printf("Case #%d: ",t+1);
		len = strlen(buf);
		for (i=len-1;i>0;--i)
		{
			if (buf[i]>buf[i-1]) break;
		}
		char temp[120],top=0;
		if (i==0)
		{
			for (j=0;j<len;++j) temp[top++] = buf[j];
			sort(temp,temp+top);
			if (temp[0]=='0')
			{
				for (j=1;j<len;++j)
				{
					if (temp[j]!='0')
					{
						temp [j] ^= temp[0];
						temp [0] ^= temp[j];
						temp [j] ^= temp[0];
						break;
					}
				}
			}
			temp [top] = 0;
			printf("%c0%s\n",temp[0],temp+1);
		}
		else
		{
			for (j=0;j<i-1;++j) printf("%c",buf[j]);
			int k = i;
			for (j=i;j<len;++j)
			{
				if ( (buf[j]>buf[i-1] && buf[j]<buf[k] )) k = j;
			}
			for (j=i-1;j<len;++j)
			{
				if (j!=k) temp[top++] = buf[j];
			}
			sort(temp,temp+top);
			temp [top] = 0;
			printf("%c%s\n",buf[k],temp);
		}
	}
	return 0;
}



