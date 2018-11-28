#include<iostream>
#include<cstdio>
using namespace std;
int A,B;
int used[10];
int used_num;
int jud(int n)
{
	int i,j;
	used_num = 0;
	int ans = 0;
	char strtemp[8];
	char strtemp2[8];
	int length = 0;
	int temp = n;
	while(temp)
	{
		length++;
		temp/=10;
	}
	temp = n;
	for(i=1;i<length;i++)
	{
		sprintf(strtemp,"%0*d",length,temp);
		sprintf(strtemp2,"%s%c",strtemp+1,strtemp[0]);
		sscanf(strtemp2,"%d",&temp);
		if(temp>n&&temp<=B)
		{
			ans++;
			used[used_num] = temp;
			used_num++;
		}
	}
	for(i=0;i<used_num;i++)
	{
		for(j=i+1;j<used_num;j++)
			if(used[i] == used[j])
				ans--;
	}
	return ans;
}
int main()
{
//  	freopen("C-small-attempt0.in","r",stdin);
//  	freopen("C-small-attempt0.out","w",stdout);

	int ans;
	int ans_temp;
	int t;
	int cases = 0;
	int i;
	scanf("%d",&t);
	while(t--)
	{
		ans = 0;
		cases++;
		scanf("%d%d",&A,&B);
		for(i=A;i<=B;i++)
		{
			ans+=jud(i);
		}
		printf("Case #%d: %d\n",cases,ans);
	}
	return 0;
}


