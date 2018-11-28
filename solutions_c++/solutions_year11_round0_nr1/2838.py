#include <stdio.h>
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++)
	{
		int pos[2],time[2];
		pos[0]=pos[1]=1;
		time[0]=time[1]=0;
		int n;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			char c;
			do{scanf("%c",&c);}
			while(c!='O'&&c!='B');
			
			int j;
			if(c=='O')j=0;
			else j=1;
			int p;
			scanf("%d",&p);
			int d=p-pos[j]<=0?pos[j]-p:p-pos[j];			
			if(time[j]+d>=time[1-j])
			{
				time[j]=time[j]+d+1;
			}
			else time[j]=time[1-j]+1;
			pos[j]=p;
		}
		printf("Case #%d: %d\n",cas,time[0]>time[1]?time[0]:time[1]);
	}
}

