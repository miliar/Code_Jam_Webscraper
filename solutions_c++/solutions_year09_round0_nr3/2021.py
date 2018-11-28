#include<stdio.h>
#include<string.h>
char real[]={"welcome to code jam"};
int res[505][20];
char str[505];
int calc(int indx_str,int indx_real)
{
	if(str[indx_str]==0)
		return 0;


	if(res[indx_str][indx_real]>0)
	{
		return res[indx_str][indx_real];
	}
	else if(indx_real==18&&str[indx_str]=='m')
		res[indx_str][indx_real]=1+calc(indx_str+1,indx_real);

	else if(str[indx_str]==real[indx_real])
		res[indx_str][indx_real]=calc(indx_str+1,indx_real)+calc(indx_str+1,indx_real+1);
	else
		res[indx_str][indx_real]=calc(indx_str+1,indx_real);
	
	return res[indx_str][indx_real];
}

int main()
{
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w",stdout);

	int ans;
	int CS,l,cs=1;
	scanf("%d",&CS);
	getchar();
	while(CS--)
	{
		gets(str);
		l=strlen(str);
		memset(res,0,sizeof(res));
		ans=calc(0,0);

		printf("Case #%d: %04d\n",cs++,ans);
	}

	return 0;
}