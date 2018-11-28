#include <cstdio>
#define REP(i,a)for(int i=0;i<(a);i++)

const int v[31]={-1,-1,27,143,751,935,607,903,991,335,47,943,471,55,447,463,991,95,607,263,151,855,527,743,351,135,407,903,791,135,647};
int T,n;

int main()
{
	freopen("C.in","r",stdin);freopen("C.out","w",stdout);
	scanf("%d",&T);
	REP(t,T)
	{
		scanf("%d",&n);
		printf("Case #%d: %.3d\n",t+1,v[n]);
	}
	return 0;
}
