#include<iostream>
#include<cstdio>
#include<cstring>
#include<cstdlib>
using namespace std;
const int maxn=105;

struct{
   char tp; int x;
}all[maxn];
int n;
int main()
{
	int cases;
	scanf("%d",&cases);
	for (int tcase=1;tcase<=cases;tcase++)
	{
		scanf("%d",&n);
		for (int i=1;i<=n;i++)
		{
			do{
				scanf("%c",&all[i].tp);
			}while (all[i].tp!='O' && all[i].tp!='B');
			scanf("%d",&all[i].x);
		}
		int now=1,op=1,bp=1,nop,nbp;
		for (int days=1;;days++)
		{
			nop=nbp=-1;
			for (int i=now;i<=n;i++)
			if (all[i].tp=='O') {nop=all[i].x;break;}				
			for (int i=now;i<=n;i++)
			if (all[i].tp=='B') {nbp=all[i].x;break;}

			if (all[now].tp=='O' && op==all[now].x) 
			{
				now++;
				nop=-1;
			}
			else if (all[now].tp=='B' && bp==all[now].x) 
			{
				now++;
				nbp=-1;
			}
			if (nop!=-1)
			{
			if (op<nop) op++;
			else if (op>nop) op--;
			}
			if (nbp!=-1)
			{
			if (bp<nbp) bp++;
			else if (bp>nbp) bp--;
			}

			if (now>n) 
			{
				printf("Case #%d: %d\n",tcase,days);
				break;
			}
		}
	}
	return 0;
}
