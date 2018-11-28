#include <cstdio>
#include <algorithm>
using namespace std;

int main()
{
	int cases,button;
	char bot[2];
	scanf("%d",&cases);

	for(int i=1;i<=cases;i++)
	{
		int N,bpos=1,opos=1;
		int time=0,prevb=0,prevo=0;

		for(scanf("%d",&N);N--;)
		{
			scanf("%s %d",bot,&button);
			if(bot[0]=='B')
			{
				time=max(prevb+abs(button-bpos),time)+1;
				prevb=time;
				bpos=button;
			}
			else
			{
				time=max(prevo+abs(button-opos),time)+1;
				prevo=time;
				opos=button;
			}
		}
		printf("Case #%d: %d\n",i,time);
	}

	return 0;
}

