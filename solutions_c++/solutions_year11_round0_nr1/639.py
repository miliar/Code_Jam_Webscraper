#include <iostream>
using namespace std;

int a[200];
int n;
void readin()
{
	int tmp,i;
	char ch;
	scanf("%d ",&n);
	for(i= 0;i<n;++i)
	{
		scanf("%c %d",&ch,&tmp);
		if(ch =='O'||ch == 'o' )
			a[i] = tmp;
		else a[i] = -tmp;
		getchar();
	}
}
void work(int CaseNum)
{
	int R1 = 1;
	int R2 = 1;
	int lastMove1 = 0,lastMove2 = 0;
	int res = 0,i;
	int er;
	for(i = 0;i<n;++i)
	if(a[i] > 0)
	{
		int t;
		t = a[i] - R1;
		R1 = a[i];
		if(t<0)t = -t;
		er = res - lastMove1;
		if(er >= t)t = 0;
		else t = t - er;
		res += t + 1;
		lastMove1 = res;
	}
	else 
	{
		int t;
		t = -a[i] - R2;
		R2 = -a[i];
		if(t<0)t = -t;
		er = res - lastMove2;
		if(er >= t) t= 0;
		else t -= er;
		res += t + 1;
		lastMove2 = res;
	}
	printf("Case #%d: %d\n",CaseNum,res);
}
int main()
{
	int tcase;
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d",&tcase);
	int i;
	for(i = 1;i<=tcase;++i)
	{
		readin();
		work(i);
	}
	fclose(stdin);

}