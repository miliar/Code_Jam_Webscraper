#include <fstream>
#include <string>
#include <iostream>
#include <vector>

using namespace std;

int Rollercoaster(int nRides, int nCapacity, vector<int>& arrGroups)
{
	int nTotalPeople = 0;
	for(int i=0; i<nRides; i++)
	{
		int nPeopleOnRollerCoaster = 0;
		vector<int> arrPeopleOnRollercoaster;
		while( arrGroups.size() > 0 && arrGroups[0] <= (nCapacity-nPeopleOnRollerCoaster) )
		{
			arrPeopleOnRollercoaster.push_back(arrGroups[0]);
			nPeopleOnRollerCoaster += arrGroups[0];
			arrGroups.erase(arrGroups.begin());
		}
		nTotalPeople += nPeopleOnRollerCoaster;
		for(int j=0; j<arrPeopleOnRollercoaster.size(); j++)
			arrGroups.push_back(arrPeopleOnRollercoaster[j]);
	}

	return nTotalPeople;
}

int main()
{
	fstream infile("C-small-attempt0.in", ios::in);
	int nTestCases;
	infile >> nTestCases;

	fstream outfile("Out", ios::out);
	for(int i=0; i<nTestCases; i++)
	{
		int nRuns, nCapacity, nNumbers;
		infile >> nRuns >> nCapacity >> nNumbers;
		vector<int> arrGroups(nNumbers);
		for(int j=0; j<nNumbers; j++)
		{
			infile >> arrGroups[j];
		}
		outfile << "Case #" << i+1 << ": " << Rollercoaster(nRuns, nCapacity, arrGroups) << endl;
	}
	outfile.close();
	return 0;
}
