#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
#include<sstream>
#include<map>

using namespace std;

char st[100];

bool cmp(char a,char b)
{
	return a<b;
}

int main()
{
	int t;
	int i,j;
	int len;
	int cas=0;
	freopen("in","r",stdin);
	freopen("out","w",stdout);

	scanf("%d",&t);

	while (t--)
	{
		cas++;
		scanf("%s",st);
		len=strlen(st);
		for (i=0;i<len/2;i++) 
		{
			swap(st[i],st[len-1-i]);
		}
		for (i=1;i<len;i++)
			if (st[i]<st[i-1]) break;

		printf("Case #%d: ",cas);
		if (i==len) //add zero
		{
			sort(st,st+len);
			for (i=0;i<len && st[i]=='0';i++);
			printf("%c",st[i]);
			for (j=0;j<i;j++) putchar('0');
			putchar('0');
			for (i++;i<len;i++) putchar(st[i]);
			putchar('\n');
		}
		else
		{
			int p=i-1;
			for (j=i-1;j>=0;j--)
				if (st[j]<st[p] && st[j]>st[i]) p=j;
			swap(st[i],st[p]);
			sort(st,st+i);
			for (j=len-1;j>=i;j--) putchar(st[j]);
			for (j=0;j<i;j++) putchar(st[j]);putchar('\n');
		}
	}
	return 0;
}