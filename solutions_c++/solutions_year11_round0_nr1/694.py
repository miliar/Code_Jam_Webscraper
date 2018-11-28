#include <stdio.h>
#include <stdlib.h>

int max(int a,int b)
{
	return (a>b)?a:b;
}

int main()
{
	int otime, btime;
	int opos, bpos;
	int pos;
	char cc;
	int cas,asd;
	int ins,i;
	freopen("A-large.in","r",stdin);
freopen("A-large.out","w",stdout);
	scanf("%d",&cas);
	for(asd=0;asd<cas;asd++)
	{
		otime = btime = 0;
		opos = bpos = 1;
		scanf("%d",&ins);
		for(i=0;i<ins;i++){
		scanf(" %c %d",&cc,&pos);
		if(cc == 'O')
		{
			otime = max(otime + abs(opos - pos) ,btime) + 1; 
			opos = pos;
		}
		else if(cc=='B')
		{

			btime = max(btime + abs(bpos - pos) ,otime) + 1;
			bpos = pos;
		}}
		printf("Case #%d: %d\n",asd+1,max(otime,btime));
	}

	return 0;
}