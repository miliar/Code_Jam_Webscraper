#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>
using namespace std;
int a,b;
bool us[2000200]={0};
int check(int num)
{
	int l=0,x=1,ans=0,num2=num;
	while((num/x)>=10)
	{
		x*=10;
		l++;
	}
	int ll=l;
	while(l--)
	{
		int y=num2%10;
		num2/=10;
		num2+=y*x;
		if(y!=0&&num2<num&&num2>=a&&!us[num2])
		{
			us[num2]=1;
			ans++;
		}
	}
	num2=num;
	while(ll--)
	{
		int y=num2%10;
		num2/=10;
		num2+=y*x;
		if(num2<num)
		us[num2]=0;
	}
	return ans;
}
int main()
{
    freopen("C-large.in","r",stdin);
	freopen("C-large.out","w",stdout);
	int t,k=0;
	scanf("%d",&t);
	while(t--)
	{
		k++;
		int count=0;
		scanf("%d%d",&a,&b);
		for(int i=a;i<=b;i++)
		{
			count+=check(i);
		}
		printf("Case #%d: %d\n",k,count);
	}
    return 0;
}