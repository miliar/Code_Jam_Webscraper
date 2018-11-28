#include <iostream>
#include <fstream>

using namespace std;

int buttons;
int Oarr[100];
int Barr[100];

int Oprio[100];
int Bprio[100];

int Oindex;
int Bindex;

int Oloc;
int Bloc;

int Odone;
int Bdone;

int time;

void moveORobot(bool hit)
{
	if(Oloc == Oarr[Odone])
	{
		if(hit)
			Odone++;
		else
			return;
	}
	else
	{
		if(Oloc < Oarr[Odone])
			Oloc++;
		else
			Oloc--;
	}
}

void moveBRobot(bool hit)
{
	if(Bloc == Barr[Bdone])
	{
		if(hit)
			Bdone++;
		else
			return;
	}
	else
	{
		if(Bloc < Barr[Bdone])
			Bloc++;
		else
			Bloc--;
	}
}

void moveRobots()
{
	if(Odone == Oindex && Bdone != Bindex)
	{
		moveBRobot(true);
	}
	else if(Bdone == Bindex && Odone != Oindex)
	{	
		moveORobot(true);
	}
	else if(Oprio[Odone] < Bprio[Bdone])
	{
		moveORobot(true);
		moveBRobot(false);
	}
	else if(Bprio[Bdone] < Oprio[Odone])
	{
		moveBRobot(true);
		moveORobot(false);
	}
}

int main()
{
	ifstream in;
	in.open("input.txt");

	ofstream out;
	out.open("output.txt");

	int tc = 0;
	int i_tc = 0;

	in >> tc;
	while(i_tc < tc)
	{
		for(int i=0; i<100; i++)
			Oarr[i] = Barr[i] = Oprio[i] = Bprio[i] = 0;
		
		Oindex = Bindex = 0;

		in >> buttons;

		char r_char;
		for(int i=0; i<buttons; i++)
		{
			in >> r_char;
			if(r_char == 'B')
			{
				in >> Barr[Bindex];
				Bprio[Bindex] = i;
				Bindex++;
			}
			else if(r_char == 'O')
			{
				in >> Oarr[Oindex];
				Oprio[Oindex] = i;
				Oindex++;
			}
		}

		Oloc = Bloc = 1;
		Odone = Bdone = 0;
		time = 0;

		while((Odone < Oindex) || (Bdone < Bindex))
		{
			moveRobots();
			time++;
		}
		
		out << "Case #" << i_tc+1 << ": " << time << endl;

		/*for(int i=0; i<Bindex; i++)
			cout << Barr[i] << " ";
		cout << endl;
		for(int i=0; i<Oindex; i++)
			cout << Oarr[i] << " ";
		cout << endl << endl;*/

		i_tc++;
	}

	in.close();
	out.close();

	cout << endl;
	system("pause");
	return 0;
}