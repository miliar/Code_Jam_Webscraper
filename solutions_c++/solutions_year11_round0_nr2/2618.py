#include<stdio.h>
main()
{
	int abc,i,j,ab,k,c,d,m,n;
	char sc[50][4],sd[40][3],sn[150],now[150];
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	scanf("%d",&abc);
	for(ab=0;ab<abc;ab++)
	{
		scanf("%d ",&c);
		for(i=0;i<c;i++)
			scanf("%s",sc[i]);
		scanf("%d ",&d);
		for(i=0;i<d;i++)
			scanf("%s",sd[i]);
		scanf("%d ",&n);
		scanf("%s",sn);
		m=0;
		for(i=0;i<n;i++)
		{
			if(m==0)
			{
				m++;
				now[0]=sn[i];
				continue;
			}
			for(j=0;j<c;j++)
				if((sn[i]==sc[j][0]&&now[m-1]==sc[j][1])||(sn[i]==sc[j][1]&&now[m-1]==sc[j][0]))
				{
					now[m-1]=sc[j][2];
					break;
				}
			if(j!=c)
				continue;
			else
			{
				for(j=0;j<m&&m!=0;j++)
					for(k=0;k<d;k++)
						if((sn[i]==sd[k][0]&&now[j]==sd[k][1])||(sn[i]==sd[k][1]&&now[j]==sd[k][0]))
						{
							m=0;
							break;
						}
				if(m!=0)
				{
					now[m]=sn[i];
					m++;
				}
			}
		}
		printf("Case #%d: [",ab+1);
		if(m!=0)
			printf("%c",now[0]);
		for(i=1;i<m;i++)
			printf(", %c",now[i]);
		printf("]\n");
	}
}
