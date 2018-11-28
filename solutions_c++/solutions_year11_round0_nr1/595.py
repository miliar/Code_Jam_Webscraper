#include<iostream>
using namespace std;
int main()
{
	freopen("1.in","r",stdin);
	freopen("1.out","w",stdout);
	int cs,c,i,op,time,o,b,p[110],n,aimO,aimB;
	char r[110][5];
	scanf("%d",&cs);
	for (c=1;c<=cs;c++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
			scanf("%s%d",r[i],&p[i]);
		time=0;
		op=-1;
		o=1;
		b=1;
		while (op<n-1)
		{
			//cout<<time<<" "<<op<<endl;
			time++;
			aimO=aimB=-1;
			for (i=op+1;i<n;i++)
			{
				if (r[i][0]=='O' && aimO==-1)
					aimO=p[i];
				if (r[i][0]=='B' && aimB==-1)
					aimB=p[i];
				if (aimO!=-1 && aimB!=-1) break;
			}
			if (r[op+1][0]=='O')
			{
				if (o!=aimO)
				{
					if (o<aimO) o++;
					else o--;
				}
				else
				{
					op++;
				}
				
				if (b!=aimB)
				{
					if (b<aimB) b++;
					else b--;
				}
			}
			else
			{
				if (b!=aimB)
				{
					if (b<aimB) b++;
					else b--;
				}
				else
				{
					op++;
				}
				
				if (o!=aimO)
				{
					if (o<aimO) o++;
					else o--;
				}
			}
		}
		printf("Case #%d: %d\n", c,time);
	}
	return 0;
}
