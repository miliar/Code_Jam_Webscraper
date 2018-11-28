#include <stdio.h>
#include <iostream>
using namespace std;

int n;
int id;
char ch;

int main()
{
	int cas,T;
	freopen("A-large.in","r",stdin);
	freopen("3.out","w",stdout);
	scanf("%d",&T);
	for(cas=1;cas<=T;++cas)
	{
		scanf("%d",&n);
		int i;
		int time[2];
		int pos[2];
		pos[0]=pos[1]=1;
		time[0]=time[1]=0;
		for(i=1;i<=n;++i)
		{
			getchar();
			scanf("%c%d",&ch,&id);
			if(ch=='O')
			{
				time[0] = time[0]+abs(id-pos[0])+1;
				if(time[0]<=time[1]) time[0]=time[1]+1;
				pos[0]=id;
			}
			else
			{
				time[1] = time[1]+abs(id-pos[1])+1;
				if(time[1]<=time[0]) time[1]=time[0]+1;
				pos[1]=id;
			}
		}
		printf("Case #%d: %d\n",cas,time[0]>time[1]?time[0]:time[1]);
	}


	return 0;
}