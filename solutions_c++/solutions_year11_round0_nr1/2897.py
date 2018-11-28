#include<cstdio>
int mo(int a)
{
	if (a < 0)
		return -a;
	else
		return a;
}
int main()
{
	int t,n,in,ca,in1,in2,s1[200],s2[200],x1,x2,q1,q2,p1,p2,g1[200],g2[200],i,j,ans;
	char ch;
	ca = 0;
	scanf("%d",&t);
	while(t--)
	{
		ca++;
		scanf("%d",&n);
		in1 = 0;
		in2 = 0;
		for (i=1;i<=n;i++)
		{
			scanf(" %c %d ",&ch,&j);
			if (ch=='O')
			{
				s1[in1] = i;
				g1[in1] = j;
//				printf("%d s1[in1] = %d g1[in1] = %d\n",in1,s1[in1],g1[in1]);
				in1++;
			}
			else
			{
				s2[in2] = i;
				g2[in2] = j;
//				printf("%d s2[in2] = %d g2[in2] = %d\n",in2,s2[in2],g2[in2]);
				in2++;
			}
		}
		s1[in1] = -1;
		s2[in2] = -1;
		ans = 0;
		x1 = 1;
		x2 = 1;
		p1 = 0;
		p2 = 0;
		for (i=1;i<=n;i++)
		{
			if (s1[p1]==i)
			{
				q1 = mo(x1-g1[p1])+1;
				ans = ans + q1;
				x1 = g1[p1];
				p1++;
				if (s2[p2]!=-1)
				{
					q2 = mo(x2-g2[p2]);
					q2 = (q2 < q1)?q2:q1;
					if (x2 < g2[p2])
						x2 = x2 + q2;
					else
						x2 = x2 - q2;
				}
			}
			else if (s2[p2]==i)
			{
				q2 = mo(x2-g2[p2])+1;
				ans = ans + q2;
				x2 = g2[p2];
				p2++;
				if (s1[p1]!=-1)
				{
					q1 = mo(x1-g1[p1]);
					q1 = (q1 < q2)?q1:q2;
					if (x1 < g1[p1])
						x1 = x1 + q1;
					else
						x1 = x1 - q1;
				}
			}
//				printf("x1 = %d x2 = %d p1  = %d p2  = %d ans = %d\n",x1,x2,p1,p2,ans);
		}
		printf("Case #%d: %d\n",ca,ans);
	}
	return 0;
}
