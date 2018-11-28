#include <iostream>
#include <stdio.h>
#include <stdlib.h>
using namespace std;
int N;

int T;
inline void stuff(int t)
{
	int button,curO=1,curB=1,BT=0,OT=0;
	char rob,last='O';
	for(int i=0;i<N;i++)
	{
		cin>>rob;		
		cin>>button;
		if(rob=='O')
		{
			OT=OT+abs(button-curO)+1;
			curO=button;
			if(last=='B')
			{
				if(OT<=BT)
				{
					OT=BT+1;
				}
			}
			last='O';
		}
		else
		{
			BT=BT+abs(button-curB)+1;
			curB=button;
			if(last=='O')
			{
				if(BT<=OT)
				{
					BT=OT+1;
				}
			}
			last='B';
		}
	}
	if(OT>BT)
		cout<<"Case #"<<t+1<<": "<<OT<<endl;
	else
		cout<<"Case #"<<t+1<<": "<<BT<<endl;
}

int main(void)
{
	cin>>T;
	for(int i=0;i<T;i++)
	{
		cin>>N;
		stuff(i);
	}
	
}
