#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main()
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int CS,l,i,j,cs=1;
	char a[100],temp;
	scanf("%d",&CS);

	while(CS--)
	{
		memset(a,'0',sizeof(a));
		scanf("%s",a);
		l=strlen(a);
		reverse(a,a+l);
		a[l]='0';
		i=0;
		while(a[i]<=a[i+1])
			i++;
		if(i+1==l)
			l++;

		int max=99;
		int maxpos=99;
		for(j=i;j>=0;j--)
		{
			if(a[j]<max&&a[j]>a[i+1])
			{
				max=a[j];
				maxpos=j;
			}
		}
		temp=a[i+1];
		a[i+1]=a[maxpos];
		a[maxpos]=temp;
		reverse(a,a+l);
		i=l-i-1;
		a[l]=0;
		sort(a+i,a+l);
		printf("Case #%d: %s\n",cs++,a);
	}
	return 0;
}