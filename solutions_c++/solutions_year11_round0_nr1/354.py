//Bot Trust
#include <cstdio>

int abs(int a)
{
	return a>0?a:-a;
}

int MAX(int a,int b)
{
	return a>b?a:b;
}

int main()
{
//	freopen("a.in","r",stdin);
//	freopen("a.out","w",stdout);
	int TST;
	scanf("%d",&TST);
	for(int tst=1;tst<=TST;++tst){
		int n;
		scanf("%d",&n);
		int to=0,tb=0,po=1,pb=1;
		for(int i=1;i<=n;++i){
			char c;
			int a;
			scanf(" %c %d",&c,&a);
			if(c=='O'){
				to+=abs(po-a)+1;
				if(to<=tb) to=tb+1;
				po=a;
			}
			else{
				tb+=abs(pb-a)+1;
				if(tb<=to) tb=to+1;
				pb=a;
			}
		}
		printf("Case #%d: %d\n",tst,MAX(to,tb));
	}
}
