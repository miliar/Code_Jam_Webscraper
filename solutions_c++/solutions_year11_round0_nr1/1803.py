#include<iostream>
#include<string.h>
#include<stdio.h>
#define abs(n) (n)>0?(n):(-n)
using namespace std ;
int line[2000];
int main()
{
	int N;
	cin>>N;
	for(int p=0;p<N;p++)
	{
		int M;
		cin>>M;
		char ch;
		int n ;
		int move_other ;
		char prev;
		int time_popo=0, dist_a=1 , dist_b=1;
		scanf(" %c %d",&ch,&n);
		{
			prev=ch;
			time_popo+=(n-1)+1;
			move_other=time_popo;
			if(ch=='O')
				dist_a=n;
			else
				dist_b=n;
		}
		for(int i=1;i<M;i++)
		{
			scanf(" %c %d" ,&ch , &n);
			int dist_to_move;
			if(ch=='O')
			{
				dist_to_move=abs((n-dist_a));
				dist_a=n;
			}
			else
			{
				dist_to_move=abs((n-dist_b));
				dist_b=n;
			}
			if(ch==prev)
			{
				move_other+=(dist_to_move)+1;
				time_popo+=(dist_to_move)+1;
			}
			else
			{
				prev=ch;
				if(move_other>dist_to_move)
				{
					move_other=1;
					time_popo++;
				}
				else
				{
					move_other=(dist_to_move-move_other)+1;
					time_popo+=move_other;
				}
			}
		}
		printf("Case #%d: %d\n",p+1,time_popo);
	}
}
