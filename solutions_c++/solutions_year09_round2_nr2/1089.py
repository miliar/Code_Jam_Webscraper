#include<iostream>
#include<vector>
#include<string>
#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

int main(void)
{
	freopen("E:\\B-small.in","r",stdin);
	freopen("E:\\B-small.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int tcase;
	for(tcase  = 1 ;tcase <= t ;tcase++)
	{
		char s[100];
		scanf("%s",s);
		int len = strlen(s)-1,i;
		char temp;
		char tempi,tempj;
		for(i=len-1;i>=0;i--)
		{
			int j;
			temp = 127;
			tempi = -1;
			for(j=len;j>i;j--)
			{
				if(s[j] > s[i] && s[j] < temp)
				{
					temp = s[j];
					tempi = j;
					tempj = i;
				}
			}
			if(temp != 127)
				break;
		}
		printf("Case #%d: ",tcase);
		if(i == -1)
		{
			sort(s,s+len+1);
			int tempi;
			for(tempi = 0;;tempi++)
				if(s[tempi] > '0')
					break;
			putchar(s[tempi]);
			printf("0");
			for(i=0;i<=len;i++)
				if(i != tempi)
					putchar(s[i]);
			puts("");
		}
		else
		{
			for(i=0;i<tempj;i++)
				putchar(s[i]);
			putchar(s[tempi]);
			char ss[100];
			int k = 0;
			for(i=tempj;i<=len;i++)
			{
				if(i != tempi)
				{
					ss[k++] = s[i];
				}
			}
			sort(ss,ss+k);
			ss[k] = '\0';
			puts(ss);
		}
	}
	return 0;
}
				
