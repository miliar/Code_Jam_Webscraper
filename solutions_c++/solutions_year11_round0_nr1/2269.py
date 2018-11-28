#include<stdio.h>
#include<string.h>
char s[2];
int W[105],w1[105],w2[105],k1,k2,t1,t2,w;
int abs(int x)
{
	return x>0?x:-x;
}
int max(int a,int b)
{
	return a>b?a:b;
}
int main()
{
	int t,k,i,p1,p2,ta,tb,ca=1;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&k);
		w1[0]=w2[0]=1;
		for(k1=k2=i=0;i<k;i++)
		{
			scanf("%s%d",s,&w);
			if(s[0]=='O')
			{
				w1[++k1]=w;
				W[i]=0;
			}
			else 
			{
				w2[++k2]=w;
				W[i]=1;
			}
		}
		ta=tb=p1=p2=t1=t2=0;

		if(W[0])
		{
			t2=w2[++p2];
			ta+=w2[p2];
		}
		else
		{
			t1=w1[++p1];
			tb+=w1[p1];
		}
		


		for(i=1;i<k;i++)
		{
			if(W[i])
			{
				t2+=max(tb,abs(w2[p2+1]-w2[p2]))+1;
				if(abs(w2[p2+1]-w2[p2])>tb)ta+=abs(w2[p2+1]-w2[p2])-tb+1;
				else ta++;
				tb=0;
				p2++;
			}
			else
			{
				t1+=max(ta,abs(w1[p1+1]-w1[p1]))+1;
				if(abs(w1[p1+1]-w1[p1])>ta)tb+=abs(w1[p1+1]-w1[p1])-ta+1;
				else tb++;
				ta=0;
				p1++;
			}
		}
		printf("Case #%d: %d\n",ca++,t1>t2?t1:t2);
	}
}
