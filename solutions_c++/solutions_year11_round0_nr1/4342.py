#include<iostream>
#include<stdlib.h>
#include<algorithm>
#include<math.h>
#include<stdio.h>
#include<string.h>
using namespace std;

struct move
{
	char player;
	int button;
}moves[108];

int main()
{
	int T,N,o,b,oPos,bPos;
	cin>>T;
	for(int t=0;t<T;t++)
	{
		cin>>N;
		o=b=0;
		for(int i=0;i<N;i++)
			cin>>moves[i].player>>moves[i].button;
		int timer=0,diff=0;
		oPos=bPos=1;
		for(int i=0;i<N;i++)
		{
			if(moves[i].player=='O')
			{
				if(i==0)
				{
					diff=moves[i].button-oPos+1;
					timer=diff;
				}
				else if(moves[i].player==moves[i-1].player)
				{
					diff=diff+abs(moves[i].button-oPos)+1;
					timer=timer+abs(moves[i].button-oPos)+1;
				}
				else
				{
					if(diff>=abs(moves[i].button-oPos))
					{
						timer++;
						diff=1;
					}
					else
					{
						timer+=abs(moves[i].button-oPos)-diff+1;
						diff=abs(moves[i].button-oPos)-diff+1;
					}
				}
				oPos=moves[i].button;
			}
			else
			{
				if(i==0)
				{
					diff=moves[i].button-bPos+1;
					timer=diff;
				}
				else if(moves[i].player==moves[i-1].player)
				{
					diff+=abs(moves[i].button-bPos)+1;
					timer+=abs(moves[i].button-bPos)+1;
				}
				else
				{
					if(diff>=abs(moves[i].button-bPos))
					{
						timer++;
						diff=1;
					}
					else
					{
						timer+=abs(moves[i].button-bPos)-diff+1;
						diff=abs(moves[i].button-bPos)-diff+1;
					}
				}
				bPos=moves[i].button;
			}
		}	
		cout<<"Case #"<<t+1<<": "<<timer<<endl;
	}

	return 0;
}
