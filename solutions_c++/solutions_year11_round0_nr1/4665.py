#include<iostream>
#include<fstream>

using namespace std;

enum Color{O,B};

struct Btm
{
	Color color;
	int pos;
};

int main()
{
	int time=0;
	int testCase;
	int trial=1;
	ifstream infile("A-large.in");
	ofstream outfile("A-large.out");
	infile>>testCase;
	while(trial<=testCase)
	{
		int btmNum;
		infile>>btmNum;
		Btm* btms=new Btm[btmNum];
		for(int i=0;i<btmNum;i++)
		{
			char color;
			infile>>color;
			if(color=='O')
				btms[i].color=Color::O;
			else
				btms[i].color=Color::B;
			infile>>btms[i].pos;
		}
		int Time=0;
		int OPos=1,BPos=1;
		int OExtratime=0,BExtratime=0;
		for(int i=0;i<btmNum;i++)
		{
			if(btms[i].color==Color::O)
			{
				if(OExtratime>=abs(btms[i].pos-OPos))
				{
					Time+=1;
					BExtratime+=1;
				}
				else
				{
					Time+=abs(btms[i].pos-OPos)-OExtratime+1;
					BExtratime+=abs(btms[i].pos-OPos)-OExtratime+1;
				}
				OExtratime=0;
				OPos=btms[i].pos;
			}
			else
			{
				if(BExtratime>=abs(btms[i].pos-BPos))
				{
					Time+=1;
					OExtratime+=1;
				}
				else
				{
					Time+=abs(btms[i].pos-BPos)-BExtratime+1;
					OExtratime+=abs(btms[i].pos-BPos)-BExtratime+1;
				}
				BExtratime=0;
				BPos=btms[i].pos;
			}
		}
		
		outfile<<"Case #"<<trial<<": "<<Time<<endl;
		delete[] btms;
		trial++;
	}
	outfile.close();	
}