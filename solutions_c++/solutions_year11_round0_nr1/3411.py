#include<stdio.h>

int seq[2][110];
int p[2][110];
int abs(int a)
{
	if(a>=0)
		return a;
	return -a;
}
int main(int argc,char* argv[])
{
	freopen("A.input","r",stdin);
	freopen("A.out","w",stdout);
	int T;
	scanf("%d",&T);
	int cas=1;
	while(T--)
	{
	int n;
	scanf("%d",&n);
	seq[0][0]=0,seq[1][0]=0;
	for(int i=0;i<n;i++)
	{
		char c;
		int tmp;
		scanf(" %c %d",&c,&tmp);
		if(c=='O')
		{
			seq[0][++seq[0][0]]=tmp;
			p[0][seq[0][0]]=i+1;
		}
		else
		{
			seq[1][++seq[1][0]]=tmp;
			p[1][seq[1][0]]=i+1;
		}
	}
	int s=1,t=1;
	int nows=1,nowt=1;
	int ans=0;
	while(s<=seq[0][0]&&t<=seq[1][0])
	{
		int needs=abs(seq[0][s]-nows)+1;
		int needt=abs(seq[1][t]-nowt)+1;
		if(p[0][s]<p[1][t])
		{
			ans+=needs;
			nows=seq[0][s];
			if(needs<needt)
			{
				if(seq[1][t]<nowt)
					nowt=nowt-needs;
				else
					nowt=nowt+needs;
			}
			else
				nowt=seq[1][t];
			s++;
		}
		else
		{
			ans+=needt;
			nowt=seq[1][t];
			if(needt<needs)
			{
				if(seq[0][s]<nows)
					nows=nows-needt;
				else
					nows=nows+needt;
			}
			else
				nows=seq[0][s];
			t++;
		}
	}
	while(s<=seq[0][0])
	{
		ans+=abs(seq[0][s]-nows)+1;
		nows=seq[0][s];
		s++;
	}
	while(t<=seq[1][0])
	{
		ans+=abs(seq[1][t]-nowt)+1;
		nowt=seq[1][t];
		t++;
	}
	printf("Case #%d: %d\n",cas++,ans);
	}
	return 0;
}
