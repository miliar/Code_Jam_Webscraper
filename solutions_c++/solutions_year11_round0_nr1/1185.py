#include <cstdio>
#include <cstdlib>

int main()
{
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		int N;
		scanf("%d",&N);
		int n1=1,n2=1;
		int re=0;
		char ch[105];
		int to[105];
		for(int i=0;i<N;i++)
			scanf(" %c%d",ch+i,to+i);
		for(int i=0;i<N;i++)
			if (ch[i]=='O')
			{
				int Time=abs(to[i]-n1)+1;
				n1=to[i];
				re+=Time;
				for(int j=i+1;j<N;j++)
					if (ch[j]=='B')
					{
						if (abs(to[j]-n2)<=Time)
							n2=to[j];
						else if (to[j]>n2)
							n2+=Time;
						else if (to[j]<n2)
							n2-=Time;
						break;
					}
			}
			else// (ch[i]=='B')
			{
				int Time=abs(to[i]-n2)+1;
				n2=to[i];
				re+=Time;
				for(int j=i+1;j<N;j++)
					if (ch[j]=='O')
					{
						if (abs(to[j]-n1)<=Time)
							n1=to[j];
						else if (to[j]>n1)
							n1+=Time;
						else if (to[j]<n1)
							n1-=Time;
						break;
					}
			}
		printf("Case #%d: %d\n",t,re);
	}
	return 0;
}
