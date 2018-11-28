// Bot Trust.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <fstream>

using namespace std;

int _tmain(int argc, _TCHAR* argv[])
{


	long N, Ni, Opos=1, Bpos=1, newpos, time=0, Otime=0, Btime=0;
	char move, prevmove;
	bool switched=false;
	

	ofstream bot_out;
    bot_out.open("bot.rez");

	ifstream bot_in;
    bot_in.open("bot.dat");

	bot_in >> N;
	for(long i=0;i<N;i++)
	{
		bot_in >> Ni;
		bot_in >> move >> newpos;
		Bpos=1;
		Opos=1;
		Btime=0;
		Otime=0;
		switched=false;

		if(move=='O')
		{
			Otime+=abs(newpos-Opos)+1;
			prevmove=move;
			Opos=newpos;
		}
		else
		{
			Btime+=abs(newpos-Bpos)+1;
			prevmove=move;
			Bpos=newpos;

		}

		cout<<"Otime "<<Otime<<endl<<"Btime "<<Btime<<endl;
		cout<<time<<endl;
		

		for(long j=1;j<Ni;j++)
		{
			bot_in >> move >> newpos;
			
			cout<<move<<" "<<newpos<<endl;


			if(move=='O')
			{
				if(prevmove=='O')
				{
					Otime+=abs(newpos-Opos)+1;
					switched=false;
				}
				else //If other moved
				{
					switched=true;
					if(abs(newpos-Opos)+1>Btime) //If Otime has been irrelevant
					{
						time+=Btime;
						Otime=abs(newpos-Opos)+1-Btime;
						Btime=0;
					}
					else //
					{
						time+=Btime;
						Otime=1;
						Btime=0;
					}
					
				}
				prevmove=move;
				Opos=newpos;
			}



			else//If B
			{
				if(prevmove=='B')
				{
					Btime+=abs(newpos-Bpos)+1;
					switched=false;
				}
				else //If other moves
				{
					switched=true;
					if(abs(newpos-Bpos)+1>Otime) //If Btime has been irrelevant
					{
						time+=Otime;
						Btime=abs(newpos-Bpos)+1-Otime;
						Otime=0;
					}
					else //
					{
						time+=Otime;
						Btime=1;
						Otime=0;
					}
				}

				prevmove=move;
				Bpos=newpos;

			}

			cout<<"Otime "<<Otime<<endl<<"Btime "<<Btime<<endl;
			cout<<time<<endl;

		}
		//if(!switched) 
		//{
			if(prevmove=='O') time+=Otime;
			else time+=Btime;
		//}
		cout <<"Final "<< time << endl<<endl;

		bot_out << "Case #"<<i+1<<": "<<time<<endl;
		time=0;
	}

    bot_in.close();


	cin >> time;
	



    
	
    

    

   
    bot_out.close();
	
	
	return 0;
}

