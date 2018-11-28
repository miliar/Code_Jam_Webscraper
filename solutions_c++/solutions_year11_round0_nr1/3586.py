#include<iostream>
#include<queue>
#include<cmath>
using namespace std;

void main()
{
	queue<int> O;
	queue<int> B;
	queue<char> seq;
	int T,N,pos,time,Opos,Bpos,Odis,Bdis;
	char bot;
	cin>>T;
	for(int cases=1;cases <= T;cases++)
	{
		cin>>N;
		for(int i=0;i<N;i++)
		{
			cin>>bot>>pos;
			seq.push(bot);
			if(bot=='O')
				O.push(pos);
			else
				B.push(pos);
		}

		Opos=1; Bpos=1; time=0;

		while(!seq.empty())
		{
			if(!O.empty())
			{
				Odis = (Opos - O.front());
				Odis = Odis<0 ? Odis * -1 : Odis;
			}
			else
			{
				Odis =-1;
			}

			if(!B.empty())
			{
			Bdis = (Bpos - B.front());
			Bdis = Bdis<0 ? Bdis * -1 : Bdis;
			}
			else
			{
				Bdis = -1;
			}

			bot = seq.front();
			seq.pop();
			if(bot == 'O')
			{
				pos =  Odis + 1;
				Opos = O.front();
				if(Odis<Bdis)
				{
					if(Bpos < B.front() )
						Bpos = (Bpos + pos);// <= B.front() ? Bpos + pos : B.front() ;
					else if (Bpos > B.front() )
						Bpos = (Bpos - pos);// >= B.front() ? Bpos - pos : B.front();
				}
				else
				{
					Bpos = Bdis == -1 ? Bpos : B.front();
				}
				O.pop();
			}
			else
			{
				pos = Bdis + 1;
				Bpos = B.front();
				if(Bdis<Odis)
				{
					if(Opos < O.front() )
						Opos = (Opos + pos);// <= O.front() ? Opos + pos : O.front() ;
					else if (Opos > O.front() )
						Opos = (Opos - pos);// >= O.front() ? Opos - pos : O.front();
				}
				else
				{
					Opos = Odis == -1 ? Opos : O.front();
				}
				B.pop();
			}
			time = time + pos;

		}
		cout<<"Case #"<<cases<<": "<<time<<endl;
	}

}