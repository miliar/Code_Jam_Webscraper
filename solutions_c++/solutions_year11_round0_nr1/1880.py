#include<cstdio>
#include<algorithm>
using namespace std;
#define MOVE 1
#define PUSH 2
#define STAY 0
int robot[999],move[999];
int o[9999],b[9999];
int main()
{
	int t,n;
	scanf("%d",&t);
	int test=1;char ch;
	for(;test<=t;test++)
	{
		int ir=0,im=0,steps=0;
		scanf("%d",&n);
		for(int i=0;i<n;i++)
		{
			ch=0;
			while(!(ch=='O' || ch=='B'))
			{
				scanf("%c",&ch);
			}
			robot[ir++]=ch;
			scanf("%d",&move[im]);im++;
		}
		int curo=1,curb=1;
		int io=0,ib=0,lpo=-1,lpb=-1;
		for(int i=0;i<n;i++)
		{
			//printf("%d %d\n",io,ib);
			if(robot[i]=='O')
			{
				while(move[i] > curo)
				{
					o[io++]=MOVE;
					curo++;
				}
				while(move[i] < curo)
				{
					o[io++]=MOVE;
					curo--;
				}
				while(io <= lpb)io++;
				o[io++]=PUSH;
				lpo=io-1;
			}
			if(robot[i]=='B')
			{
				while(move[i] > curb)
				{
					b[ib++]=MOVE;
					curb++;
				}
				while(move[i] < curb)
				{
					b[ib++]=MOVE;
					curb--;
				}
				while(ib <= lpo)ib++;
				b[ib++]=PUSH;
				lpb=ib-1;
			}
		}
		printf("Case #%d: %d\n",test,max(io,ib));
	}
}
