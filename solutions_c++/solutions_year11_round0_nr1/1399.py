#include<cstdlib>
#include<stdio.h>

using namespace std;

class bot
{
	public:
		bot() : pos(1), time(0) {}
		int pos;
		int time;
		int go(int newpos, int MinNewTime)
		{
			int len=abs(pos-newpos)+1;
			if(time+len<MinNewTime)
				time=MinNewTime;
			else time+=len;
			pos=newpos;
			//printf("time=%d len=%d ",time,len);
			return time;
		}
};

int main()
{
	int k,n;
	char c;
	int v;
	scanf("%d",&k);
	for(int i=0;i<k;++i)
	{
		bot blue,orange;
		int t=0;
		scanf("%d",&n);
		for(int j=0;j<n;++j)
		{
			scanf(" %c %d",&c,&v);
			if(c=='O')
				t=orange.go(v,t+1);
			else if(c=='B')
				t=blue.go(v,t+1);
			else printf("KABOOOM! ");
		}
		printf("Case #%d: %d\n",i+1,t);
	}
	return 0;
}
