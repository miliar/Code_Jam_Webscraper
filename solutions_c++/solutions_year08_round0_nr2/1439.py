#include <iostream>
#include <string>
#include <fstream>
#include <vector>
#include <cmath>
#include <algorithm>

#define PI 	3.14159265358979323846
#define A2B	true
#define B2A	false

using namespace std;

// JOURNEY
struct Journey
{
	int 	js;
	int 	je;
	bool 	di;
};

// JOURNEY
struct Train
{
	bool 	start;		// start station
	bool 	current;	// current station
	int 	at;		// available time
};


// comparex function for sorting
bool jcomp(const Journey & a, const Journey & b)
{
	return (a.js < b.js);
}

// comparex function for sorting
bool tcomp(const Train & a, const Train & b)
{
	return (a.at < b.at);
}

// get a solution
Journey solveJourney
(
	vector<Journey> * journeys
) {

	// starting points
	Journey res;
	res.js = 0;
	res.je = 0;

	// 1. sort the journeys in ascending order
	sort(journeys->begin(), journeys->end(), jcomp);

	// 2. create a vector to store current trains
	vector<Train> trains;

	// 2. set the current time
	int ct = 0;

	// keep going if we still have journeys to complete
	for (int j = 0; j < journeys->size(); j++)
	{
	
		// get the current kourney
		Journey cur = (*journeys)[j];

		// sort the train list
		sort(trains.begin(), trains.end(), tcomp);

		// 
		bool found = false;
		
		// check whether there is a train ready to perform the 
		for (int i = 0; i < trains.size(); i++)
		{
			// just take the first avialabke train at the required station
			if (trains[i].current == cur.di && trains[i].at <= cur.js)
			{
				found = true;

				// set the train details
				trains[i].current = !trains[i].current;
				trains[i].at = cur.je;

				break;
			}

		}

		// if no trains match credentials we need to add one
		if (!found)
		{
			//c reate a new train
			Train nt;
			nt.start = cur.di;
			nt.current = !cur.di;
			nt.at = cur.je;

			// add it
			trains.push_back(nt);
		}	

	}


	// check whether there is a train ready to perform the 
	for (int i = 0; i < trains.size(); i++)
	{
		if (trains[i].start)
			res.js++;
		else
			res.je++;

	}

	// return the result
	return res;


}

// parse a formatted date into number of minutes
Journey parseTime
(
	string ts,
	string te,
	int txtime,
	bool dir
) {
	Journey tmp;

	// convert from XX:YY to minutes from 00h00
	tmp.js = atoi(ts.substr(0,2).c_str()) * 60 + atoi(ts.substr(3,2).c_str());
	tmp.je = atoi(te.substr(0,2).c_str()) * 60 + atoi(te.substr(3,2).c_str()) + txtime;

	// record the journey direction
	tmp.di = dir;

	return tmp;
}

int main
(
	int argc,
	const char * argv[]
) {

	// get the file name
	const char * fname_in = argv[1];
	const char * fname_out = argv[2];

	// open the file
	ifstream infile(fname_in);
	ofstream outfile(fname_out);

	// for parsing
	string tmp;

	// get the number of search rounds
	getline(infile, tmp, (char)'\n');
	int rounds = atoi(tmp.c_str());
	cout << "Rounds : " << rounds << endl;

	// loop through rounds
	for (int i = 0; i < rounds; i++)
	{

		cout << "--> Round " << (i+1) << endl;

		int txtime, ab, ba;
		infile >> txtime >> ab >> ba >> ws; 
		cout << "Turnaround : " << txtime << endl;
		cout << "A->B Trips : " << ab<< endl;
		cout << "B->A Trips : " << ba << endl;

		// store journeys
		vector<Journey> journeys;

		string ts, te;

		for (int j = 0; j < ab; j++)
		{
			infile >> ts >> ws >> te >> ws; 			
			journeys.push_back(parseTime(ts, te, txtime, A2B));
		}

		for (int j = 0; j < ba; j++)
		{
			infile >> ts >> ws >> te >> ws; 			
			journeys.push_back(parseTime(ts, te, txtime, B2A));
		}

		// get a solution
		Journey soln = solveJourney(&journeys);

		// get the solution
		outfile << fixed << "Case #" << (i+1) << ": " << soln.js << " " << soln.je << endl;


	}

	// close file access
	infile.close();
	outfile.close();

}
