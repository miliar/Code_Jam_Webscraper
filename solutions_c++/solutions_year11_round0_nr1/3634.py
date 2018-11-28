#include <iostream>
#include <stdio.h>

using namespace std;

int abs(int i)
{if (i<0) return i* (-1); else return i;}

int main()
{

	int TestCase,k;
	cin>>TestCase;
	for(k=1;k<=TestCase;k++)
	{
	int current_time=0;
	int o_time=0,o_pos=1;
	int b_time=0,b_pos=1;

	int N,i,j,pos,time;
	char c;

	cin>>N;

	for(i=1;i<=N;i++)
	{
		cin>>c>>pos;
		if(c=='O')
		{
			time= abs(pos - o_pos) + 1 ;
			if(time <= (current_time - o_time))
			{
			current_time ++;
			}
			else
			{
			 current_time = time + o_time;
			}
			o_time=current_time;
			o_pos=pos;
		}
		else
		{
			time= abs(pos - b_pos) + 1 ;
			if(time <= (current_time - b_time))
			{
			current_time ++;
			}
			else
			{
			 current_time = time + b_time;
			}
			b_time=current_time;
			b_pos=pos;

		}
	}

	cout<<"Case #"<<k<<": "<<current_time<<"\n";
	}

return 0;
}

