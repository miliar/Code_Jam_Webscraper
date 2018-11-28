#include<iostream>
using namespace std;
int a[10]={1,0,2,3,4,5,6,7,8,9};
int main()
{
	char s[100];
	int hash[40];

	int i,j,k;
	int t;
	char ans[100];
	__int64 da;
	int tt=0;
	freopen("A-small-attempt1.in","r",stdin);
	freopen("out.out","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		tt++;
		scanf("%s",&s);
		int num=0;
		int jin=0;
		da=0;
		memset(hash,-1,sizeof(hash));
		for(i=0;s[i]!='\0';i++)
		{
			if(s[i]>='0' && s[i]<='9')
			{
				if(hash[s[i]-'0']==-1)
				{
					hash[s[i]-'0']=a[num];
					ans[i]=a[num];
					num++;
				}
				else
				{
					ans[i]=hash[s[i]-'0'];
				}
			}
			else
			{
				if(hash[s[i]-'a'+10]==-1)
				{
					hash[s[i]-'a'+10]=a[num];
					ans[i]=a[num];
					num++;
				}
				else
				{
					ans[i]=hash[s[i]-'a'+10];
				}
			}
		}
		if(num==1)
			num=2;
		__int64 kk=1;
		for(j=i-1;j>=0;j--)
		{
			da=da+kk*(__int64)(ans[j]);
			kk=kk*num;
		}
		printf("Case #%d: ",tt);
		printf("%d\n",da);

	}
	return 0;
}