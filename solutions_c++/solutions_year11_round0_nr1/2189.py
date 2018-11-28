#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int testcases;
        fin >> testcases;
	vector <int> steps;
	for(int i=0; i<testcases; i++)
	{
		vector <char> colors;
		vector <int> Bbuttons;
		vector <int> Obuttons;
		int buttons, Bplace = 1, Oplace = 1, count = 0, bcount = 0, ocount = 0, time = 0;
		fin >> buttons;
		for(int j=0; j<buttons; j++)
		{
			char temp;
			int tempo;
			fin >> temp;
			colors.push_back(temp);
			fin >> tempo;
			if(temp == 'B')
				Bbuttons.push_back(tempo);
			else Obuttons.push_back(tempo);
		}
		while(count < colors.size())
		{
			if(colors[count] == 'B')
			{
				if(bcount < Bbuttons.size() && Bplace == Bbuttons[bcount])
				{
					bcount++;
					count++;
				}
                                else if(bcount < Bbuttons.size() && Bplace != Bbuttons[bcount])
				{
					if(Bplace < Bbuttons[bcount]) Bplace++;
					else Bplace--;
				}
				if(ocount < Obuttons.size() && Oplace != Obuttons[ocount])
				{
					if(Oplace < Obuttons[ocount]) Oplace++;
					else Oplace--;
				}
			}
			else
			{
				if(ocount < Obuttons.size() && Oplace == Obuttons[ocount])
				{
					ocount++;
					count++;
				}
                                else if(ocount < Obuttons.size() && Oplace != Obuttons[ocount])
				{
					if(Oplace < Obuttons[ocount]) Oplace++;
					else Oplace--;
				}
				if(bcount < Bbuttons.size() && Bplace != Bbuttons[bcount])
				{
					if(Bplace < Bbuttons[bcount]) Bplace++;
					else Bplace--;
				}
			}
			time++;
		}
		steps.push_back(time);
	}
	for(int i=0; i<steps.size(); i++)
		fout << "Case #" << i+1 << ": " << steps[i] << endl;
	return 0;
}
