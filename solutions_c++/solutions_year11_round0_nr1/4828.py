#include <iostream> //cin, cout
#include <fstream> //ifstream, ofstream
#include <string> //string, getline()
#include <math.h>

using namespace std;

int main()
{
	string line;
	int Opos, Bpos, Otime, Btime, total, cases, buttons, Otemp, Btemp, Opress, Bpress;
	char last, now;
	ifstream file("example.txt");
	ofstream output("results.txt");


	if (file.is_open())
	{
		file >> cases;

		for (int i = 1; i <= cases; i++)
		{
			total = 0;
			Opos = 1;
			Bpos = 1;
			Otime = 0;
			Btime = 0;
			Opress = 0;
			Bpress = 0;

			file >> buttons;
			
			file >> now;
			buttons --;
			if (now == 'O')
			{
				file >> Otemp;
				Otime = Otime + abs(Otemp - Opos);
				Opos = Otemp;
				Opress++;
			}
			else
			{
				file >> Btemp;
				Btime = Btime + abs(Btemp - Bpos);
				Bpos = Btemp;
				Bpress++;
			}

			while (buttons > 0)
			{
				do
				{
					last = now;
					file >> now;
					buttons --;
					if (now == 'O')
					{
						file >> Otemp;
						Otime = Otime + abs(Otemp - Opos);
						Opos = Otemp;
						Opress++;
					}
					else
					{
						file >> Btemp;
						Btime = Btime + abs(Btemp - Bpos);
						Bpos = Btemp;
						Bpress++;
					}
				} while(now == last && buttons > 0 );

				if (now == 'B')
				{
					if ((Otime + Opress) >= Btime)
					{
						total = total + Otime + Opress;
						Otime = 0;
						Btime = 0;
						Opress = 0;
					}
					else
					{
						total = total + Otime + Opress;
						Btime = Btime - Otime - Opress;
						Otime = 0;
						Opress = 0;
					}
				}
				else
				{

					if ((Btime + Bpress) >= Otime)
					{
						total = total + Btime + Bpress;
						Otime = 0;
						Btime = 0;
						Bpress = 0;
					}
					else
					{
						total = total + Btime + Bpress; 
						Otime = Otime - Btime - Bpress;
						Btime = 0;
						Bpress = 0;
					}
				}
			}
			total = total + Otime + Opress + Btime + Bpress;
			output << "Case #" << i << ": "<< total << endl;
		}
	}
	file.close();
	return 0;
}