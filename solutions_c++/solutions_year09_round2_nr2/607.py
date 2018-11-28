#include<cstdio>
#include<cstring>
#include<algorithm>

using namespace std;

char a[100];

void process()
{
	int i,j;
	for(i=strlen(a)-1;i;i--)
	{
		if(a[i]>a[i-1]) break;
	}
	if(i)
	{
		i--;
		for(j=i+1;j<strlen(a);j++)
		{
			if(a[j]<=a[i]) break;
		}
		j--;
		swap(a[i],a[j]);
		sort(a+i+1,a+strlen(a));
		char temp=a[i];
		printf("%s\n",a);
	}
	else
	{
		int i;
		sort(a,a+strlen(a));
		for(i=0;a[i]=='0';i++);
		printf("%c",a[i]);
		printf("0");
		a[i]=0;
		printf("%s%s\n",a,a+i+1);
	}
}

int main()
{
	freopen("output.txt","w",stdout);
	int t;
	scanf("%d",&t);
	for(int i=0;i<t;i++)
	{
		scanf("%s",a);
		printf("Case #%d: ",i+1);
		process();
	}
}