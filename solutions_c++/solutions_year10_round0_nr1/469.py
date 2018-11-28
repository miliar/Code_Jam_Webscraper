#include <cstdio>
int Test,Case;
int N,M;

inline void Readin()
{
	scanf("%d%d",&N,&M);
}

inline void Solve()
{
	puts(((1<<N)-1&M)==((1<<N)-1)?"ON":"OFF");
}

int main()
{
	//freopen("i.txt","r",stdin);
	
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
