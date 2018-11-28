#include<iostream>
using namespace std;
typedef long long Lint;
Lint n,pd,pg;
Lint gcd(Lint a,Lint b){
	return b?gcd(b,a%b):a;
}
void readin()
{
	scanf("%I64d%I64d%I64d",&n,&pd,&pg);
}
void work(int CaseNum)
{
	if((pg == 100 && pd !=100)||(pg == 0)&& (pd !=0))
	{
		printf("Case #%d: Broken\n",CaseNum);
		return;
	}
	if((pg == 100 && pd ==100)||(pg == 0)&& (pd ==0))
	{
		printf("Case #%d: Possible\n",CaseNum);
		return;
	}
	if(pd == 0)
	{
		printf("Case #%d: Possible\n",CaseNum);
		return;
	}
	Lint tmp = gcd(pd,100);
	tmp = 100/tmp;
	if(tmp>n)
		printf("Case #%d: Broken\n",CaseNum);
	else printf("Case #%d: Possible\n",CaseNum);

}

int main()
{
	int tcase;
	int i;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&tcase);
	for(i = 1;i<=tcase;++i)
	{
		readin();
		work(i);
	}
}