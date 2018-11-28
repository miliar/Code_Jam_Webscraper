#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <algorithm>
using namespace std;

const char INFILE_NAME[]        = "in.in";
const char OUTFILE_NAME[]       = "gcj.Out";

ifstream fin;						// Input file
ofstream fout;						// Output file

struct Train {
    int		time;
	bool	left;
	int		arrivaltime;
    string	route;
};
void sort (vector<Train> &trains);

int trainsort(const void *first, const void *second) {
	Train fir = *(Train*)first;
	Train sec = *(Train*)second;
	if( fir.time < sec.time )
	{
			return -1;
	}
	else if ( fir.time == sec.time )
	{
		return 0;
	}
	else
		return 1;
}

Train processTrain(string hhmm, string dir, int delay);

int main()
{
	fout.open(OUTFILE_NAME, ios::out);

	if (fout)
	{
		fin.open(INFILE_NAME, ios::in);
	}

	int cases;
	fin >> cases;

	for( int acase = 0; acase < cases; acase++ )
	{
		int astart = 0;
		int bstart = 0;

		int atrain = 0;
		int btrain = 0;

		int delay;
		fin >> delay;

		int anum;
		fin >> anum;

		int bnum;
		fin >> bnum;
		fin.ignore(100,'\n');

		int routes = anum + bnum;
		//Train* trains = new Train[routes];
		vector<Train> trains;

		for( int i = 0; i < anum; i++ )
		{
			string aroute;
			getline (fin,aroute);
			Train atrain = processTrain(aroute,"AB",delay);
			trains.push_back(atrain);
		}
		for( int i = 0; i < bnum; i++ )
		{
			string aroute;
			getline(fin,aroute);
			Train btrain = processTrain(aroute,"BA",delay);
			trains.push_back(btrain);
		}
		sort(trains);

		for( int i = 0; i < routes*2; i++ )
		{
			Train current = trains.front();
			if( !current.left )
			{
				if( current.route == "AB" )
				{
					if( atrain == 0 )
					{
						astart++;
					}
					else
					{
						atrain--;
					}
				}
				else
				{
					if( btrain == 0 )
					{
						bstart++;
					}
					else
					{
						btrain--;
					}
				}
				current.left = true;
				current.time = current.arrivaltime;
			}
			// it has left, process arrival
			else
			{
				if( current.route == "AB" )
				{
					btrain++;
				}
				else
				{
					atrain++;
				}
				current.time = 24*60;
			}
			trains.front() = current;
			sort(trains);
		}
		cout << "Case #" << acase+1 << ": " << astart << " " << bstart << endl;
		fout << "Case #" << acase+1 << ": " << astart << " " << bstart << endl;
	}

	if (fin)
	{
		fin.close();
	}
	fout.close();

}
void sort (vector<Train> &trains)
{
	Train temp;
	for(unsigned int i = 0; i < trains.size()-1; i++ )
	{
		for (unsigned int j = i+1; j < trains.size(); j++ )
		{
			if (trains[i].time > trains[j].time)
			{
				temp = trains[i];
				trains[i] = trains[j];
				trains[j] = temp;
			}
		}
	}
	return;
}

Train processTrain(string hhmm, string dir, int delay)
{
	Train train;
	int hours = (hhmm[0]-'0')*10 + (hhmm[1]-'0');
	int minutes = (hhmm[3]-'0')*10 + (hhmm[4]-'0');
	int leave = hours*60 + minutes;

	hours = (hhmm[6]-'0')*10 + (hhmm[7]-'0');
	minutes = (hhmm[9]-'0')*10 + (hhmm[10]-'0');
	int arrive = hours*60 + minutes;

	train.time = leave;
	train.arrivaltime = arrive + delay;
	train.left = false;
	train.route = dir;
	//cout << "train time is " << train.time << "; arrival is " << train.arrivaltime << endl;

	return train;
}
