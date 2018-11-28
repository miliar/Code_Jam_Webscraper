#include<cstdio>
#include<cstring>
int n,t,i,p1,p2,a,l1,l2,t1,t2,time,mt=1;
struct node
{
	int a,i;
}f1[200],f2[200];
char s[9];
int abs(int n)
{
	if (n<0) return -n;
	return n;
}
int main()
{
	freopen("A3.in","r",stdin);
	freopen("A3.out","w",stdout);
	scanf("%d",&t);
	while(mt<=t)
	{
		memset(f1,0,sizeof(f1));
		memset(f2,0,sizeof(f2));
		scanf("%d",&n);
		l1=l2=0;
		for(i=0;i<n;i++) 
		{
			scanf("%s%d",s,&a);
			if (s[0]=='O') 
			{
				f1[l1].i=i;
				f1[l1++].a=a;
			}
			if (s[0]=='B')
			{
				f2[l2].i=i;
				f2[l2++].a=a;
			}
		}
		p1=p2=1;
		t1=t2=0;
		time=0;
		for(i=0;i<n;i++)
		{
			if (t1==l1)
			{
				f1[t1].i=n+1;
			}
			if (t2==l2)
			{
				f2[t2].i=n+1;
			}
			if (f1[t1].i<f2[t2].i)
			{
				int ti=abs(f1[t1].a-p1)+1;
				time+=ti;
				p1=f1[t1].a;
				if (p2>f2[t2].a)
				{
					if (p2-f2[t2].a>=ti) p2-=ti;
					else p2=f2[t2].a;
				}
				if (p2<f2[t2].a)
				{
					if (f2[t2].a-p2>=ti) p2+=ti;
					else p2=f2[t2].a;
				}
				t1++;
			}
			if (f1[t1].i>f2[t2].i)
			{
				int ti=abs(f2[t2].a-p2)+1;
				time+=ti;
				p2=f2[t2].a;
				if (p1>f1[t1].a)
				{
					if (p1-f1[t1].a>=ti) p1-=ti;
					else p1=f1[t1].a;
				}
				if (p1<f1[t1].a)
				{
					if (f1[t1].a-p1>=ti) p1+=ti;
					else p1=f1[t1].a;
				}
				t2++;
			}
		}
		printf("Case #%d: %d\n",mt,time);mt++;
	}
}
