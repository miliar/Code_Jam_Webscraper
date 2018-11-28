#include<iostream>
using namespace std;

int a[110],b[110],an,bn,a1,b1;
int Abs(int a)
{
	return a>0? a:-a;
}
int main()
{
	int t,test=1,n,i,k,aa,bb,sum;
	char ch;

	freopen("A-large.in.txt","r",stdin);
	freopen("2.txt","w+",stdout);

	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		an=bn=a1=b1=0;
		aa=1,bb=1,sum=0;
		for(i=0;i<n;i++)
		{
			scanf(" %c%d",&ch,&k);
			if(ch=='O')
			{
				a[an++]=k;
				if(bn==b1) continue;

				while(b1!=bn)
				{
					sum+=Abs(b[b1]-bb)+1;
					if(Abs(a[a1]-aa)<=Abs(b[b1]-bb)+1)
						aa=a[a1];
					else if(a[a1]-aa>0)
						aa=aa+Abs(b[b1]-bb)+1;
					else
						aa=aa-(Abs(b[b1]-bb)+1);
					
					bb=b[b1];
					b1++;
				}
			}
			else
			{
				b[bn++]=k;
				if(an==a1) continue;

				while(a1!=an)
				{
					sum+=Abs(a[a1]-aa)+1;
					if(Abs(b[b1]-bb)<=Abs(a[a1]-aa)+1)
						bb=b[b1];
					else if(b[b1]-bb>0)
						bb=bb+Abs(a[a1]-aa)+1;
					else
						bb=bb-(Abs(a[a1]-aa)+1);
					
					aa=a[a1];
					a1++;
				}
			}
		}
		while(a1!=an) 
		{
			sum+=Abs(a[a1]-aa)+1;
			aa=a[a1];
			a1++;
		}
		while(b1!=bn)
		{
			sum+=Abs(b[b1]-bb)+1;
			bb=b[b1];
			b1++;
		}
		printf("Case #%d: %d\n",test++,sum);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}