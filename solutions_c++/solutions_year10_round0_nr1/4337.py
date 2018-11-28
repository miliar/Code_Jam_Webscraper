#include <iostream>
#include <fstream>
#include <list>

using namespace std;

class Snapper {
public:
	Snapper() : input(false), status(false), output(false) { }
	bool input;
	bool status;
	bool output;
};

int main()
{
	ifstream inputFile("input.txt", ifstream::in);
	ofstream outputFile("output.txt", ifstream::out);

	long t;

	inputFile >> t;

	for(long round = 0; round < t; ++round) {

		long n, k;
		bool bulb;
		list<Snapper> snapper_chain;

		inputFile >> n;
		inputFile >> k;
//		cout << "Round: " << round << endl;
//		cout << "N: " << n << " K: " << k << endl;

		Snapper snapperSample;
		for(long n0 = 0; n0 < n; ++n0) {
			snapper_chain.push_back(snapperSample);
		}

		snapper_chain.front().input = true;

		// Snapping

		for(long k0 = 0; k0 < k; ++k0) {
	
			list<Snapper>::iterator i;
			//bool prevPower = true;
			//bool prevStatus = true;

			for(i = snapper_chain.begin(); i != snapper_chain.end(); ++i) {

				// Output: toggle if has power
				if(i->input)
					i->status = !(i->status);
			}

			bool prevOutput = true;

			for(i = snapper_chain.begin(); i != snapper_chain.end(); ++i) {
				
				i->input = prevOutput;					
				i->output = i->input && i->status;
				prevOutput = i->output;
			}

			/* Old algorithm
			for(i = snapper_chain.begin(); i != snapper_chain.end(); ++i) {
				// Input: if previous 
				i->power = (prevPower && prevStatus);
				
				// Output
				if(prevPower && prevStatus)
					i->status = !(i->status);

				prevPower = i->power;
				prevStatus = i->status;
			}*/
		}

		bulb = snapper_chain.back().output;

		if (bulb)
			outputFile << "Case #" << round+1 << ": " << "ON";
		else
			outputFile << "Case #" << round+1 << ": " << "OFF";

		//if(round != (t-1))
			outputFile << endl;

	}

	return 0;
}