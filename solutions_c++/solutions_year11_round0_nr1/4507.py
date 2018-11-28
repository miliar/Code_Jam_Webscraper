#include<fstream>
#include<iostream>

using namespace std;

ifstream fin;

int sign(int x)
{
	if(x<0)
		return -1;
	if(x>0)
		return 1;
	else
		return 0;
}

class state
{
	public:
	int otarget;
	int btarget;
	char botToPushButton;
	int ocurr;
	int bcurr;
	int buttonsPushed;
	int noOfbuttons;
	int secs;
	char* seq;
	int* oqueue;
	int* bqueue;
	bool done;
	
	state(void);
	void run();	
};


state::state(void)
{	
	fin>>noOfbuttons;
	seq = new char[noOfbuttons];
	oqueue = new int[noOfbuttons];
	bqueue = new int[noOfbuttons];

	char* nextBot = seq;
	int* o = oqueue;
	int* b = bqueue;

	char c;
	while((fin.get(c))&&(c!='\n'))
	{
		if(c == 'O'||c == 'o')
		{
			*nextBot++ = 'o';
			fin>>(*o);
			o++;
		}
		else if(c == 'B'||c == 'b')
		{
			*nextBot++ = 'b';
			fin>>(*b);
			b++;			
		}
	}
	
	done = false;
	otarget = *oqueue++;
	btarget = *bqueue++;
	ocurr = 1;
	bcurr = 1;
	botToPushButton = *seq++;
	buttonsPushed = 0;
}

void state::run(void)
{
	int odiff = otarget - ocurr;
	int bdiff = btarget - bcurr;
	
	if(botToPushButton == 'o')
	{
		bcurr+= sign(bdiff);
		if(odiff == 0)
		{
			buttonsPushed++;
			if(buttonsPushed == noOfbuttons)
				done = true;
			else
			{
				botToPushButton = *seq++;
				otarget = *oqueue++;
			}
		}
		else
			ocurr+= sign(odiff);
	}
	else
	{
		ocurr+= sign(odiff);
		if(bdiff == 0)
		{
			buttonsPushed++;
			if(buttonsPushed == noOfbuttons)
				done = true;
			else
			{
				botToPushButton = *seq++;
				btarget = *bqueue++;
			}
		}
		else
			bcurr+= sign(bdiff);
	}
}

int main()
{
	fin.open("A-large.in");
	int noTests;
	fin>>noTests;
	ofstream fout("output.out");

	int i=0;
	while(i<noTests)
	{
		state t;
		t.secs = 0;
		while(!t.done)
		{
			t.run();
			t.secs++;
		}
		i++;
		fout<<"Case #"<<i<<": "<<t.secs<<'\n';
	}
}


