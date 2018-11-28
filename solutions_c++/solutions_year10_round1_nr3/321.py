#include<iostream>
using namespace std;
bool func(int a,int b)
{
	if(a<b)
		swap(a,b);
	if(a==b)
		return false;
	else if(a/b>=2)
		return true;
	else
	{
		if(func(a-b,b))
			return false;
		else
			return true;
	}
}
int main()
{
	int cas,a1,a2,b1,b2,a,b,ii,cnt;
	//freopen("C-small-attempt0.in","r",stdin);
	//freopen("2.txt","w",stdout);
	scanf("%d",&cas);
	for(ii=1;ii<=cas;ii++)
	{
		scanf("%d%d%d%d",&a1,&a2,&b1,&b2);
		cnt=0;
		for(a=a1;a<=a2;a++)
			for(b=b1;b<=b2;b++)
				if(func(a,b))
					cnt++;
		printf("Case #%d: %d\n",ii,cnt);
	}
	return 0;
}
