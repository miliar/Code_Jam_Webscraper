#include<stdio.h>
#define FILENAME "large"
int T, V;
int process(__int64 s,__int64 e)
{
	if(s*V >= e) return 0;
	int cnt = 0;
	__int64 a = s, b = e;
	while(a < b)
	{
		a *= V; cnt ++;
	}

	int i;
	a = s;
	for(i=1;i<=cnt/2;i++) a *= V;
	int tmp1, tmp2, ans1, ans2;

	//test a
	tmp1 = process(a,e); tmp2 = process(s,a);
	if(tmp1 > tmp2) ans1 = tmp1;
	else ans1 = tmp2;

	//test a*V
	if(cnt%2==1){
		a *= V;
		tmp1 = process(a,e); tmp2 = process(s,a);
		if(tmp1 > tmp2) ans2 = tmp1;
		else ans2 = tmp2;
	}
	else ans2 = ans1;

	int ans = ans1<ans2?(ans1+1):(ans2+1);
	return ans;
}
int main()
{
	freopen(FILENAME ".in","r",stdin);
	freopen(FILENAME ".out","w",stdout);
	__int64 t;
	scanf("%d",&T);
	for(t=1;t<=T;t++)
	{
		int s, e;
		scanf("%d %d %d",&s,&e,&V);
		printf("Case #%I64d: %d\n",t,process(s,e));
	}
}