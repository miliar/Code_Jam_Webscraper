#include <iostream>
using namespace std;
double res = 0;
int a[1020];
int disorder,n;
void readin()
{
	int i;
	scanf("%d",&n);
	disorder = 0;
	for(i = 1;i<=n;++i)
	{
		scanf("%d",&a[i]);
		if(a[i]!=i)++disorder;
	}
}
void work(int caseNum)
{
	if(disorder  == 1) res = 0;
	else res = disorder;
	printf("Case #%d: %lf\n",caseNum,res);
}
int main()
{
	int tcase;
	freopen("D-large.in","r",stdin);
	freopen("D-large.out","w",stdout);
	scanf("%d",&tcase);
	int i;
	for(i = 1;i<=tcase;++i)
	{
		readin();
		work(i);
	}
	//fclose(stdin);

}