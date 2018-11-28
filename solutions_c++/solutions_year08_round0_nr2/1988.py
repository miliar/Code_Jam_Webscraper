// Train.cpp : Defines the entry point for the console application.
//
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <iostream>

using namespace std;

struct triptime {
	int start;
	int end;
};		

struct testcase {
	int turnAroundTime;
	vector<triptime> aTimes;
	vector<triptime> bTimes;
};

bool ttCompare(triptime one, triptime two) {
	if (one.start < two.start)
		return true;
	else if (one.start == two.start) {
		if (one.end < two.end)
			return true;
	}
	return false;
}

vector<testcase> readInput(char *fileName) {
	vector<testcase>testCases;
	fstream fp;
	int nCases = 0, nA = 0, nB = 0, turnAroundTime=0;
	fp.open(fileName, ios::in);
	fp>>nCases;
	for (int i=0; i<nCases; i++) {

		testcase newCase;

		fp>>newCase.turnAroundTime;
		fp>>nA>>nB;

		string timefortrip;
		getline(fp, timefortrip);
		for (int j=0; j<nA; j++) {			
			getline(fp, timefortrip);
			triptime a;
			a.start = atoi((timefortrip.substr(0,2) + timefortrip.substr(3,2)).c_str());
			a.end = atoi((timefortrip.substr(6,2) + timefortrip.substr(9,2)).c_str());
			newCase.aTimes.push_back(a);
		}

		for (int k=0; k<nB; k++) {
			getline(fp, timefortrip);
			triptime b;
			b.start = atoi((timefortrip.substr(0,2) + timefortrip.substr(3,2)).c_str());
			b.end = atoi((timefortrip.substr(6,2) + timefortrip.substr(9,2)).c_str());
			newCase.bTimes.push_back(b);
		}

		sort(newCase.aTimes.begin(), newCase.aTimes.end(), ttCompare);
		sort(newCase.bTimes.begin(), newCase.bTimes.end(), ttCompare);

		testCases.push_back(newCase);
	}
	return testCases;
}

void processTestCase(testcase t, int& nTrainsA, int& nTrainsB) {
	nTrainsA = 0, nTrainsB = 0;
	int aCounter = 0, bCounter = 0;
	bool trainAvailA = false, trainAvailB = false;
	vector<int> aArrive, bArrive;

	bool Adone = false, Bdone = false;
	while (!Adone || !Bdone) {

		int aStart = 0, bStart = 0;

		if (bCounter<t.bTimes.size())
			bStart = t.bTimes[bCounter].start;
		else
			bStart = 20000;

		if (aCounter<t.aTimes.size())
			aStart = t.aTimes[aCounter].start;
		else
			aStart = 20000;

		if(aArrive.size()>0 && aArrive[0] + t.turnAroundTime <= aStart)
			trainAvailA = true;
		else
			trainAvailA = false;

		if(bArrive.size()>0 && bArrive[0] + t.turnAroundTime <= bStart)
			trainAvailB = true;
		else
			trainAvailB = false;

		 if(!Adone && aStart < bStart) {
			if (trainAvailA == false)
				nTrainsA ++;
			else
				aArrive.erase(aArrive.begin());
			bArrive.push_back(t.aTimes[aCounter].end);
			aCounter ++;
		}
		else  if(!Bdone){
			if(trainAvailB == false)
				nTrainsB ++;
			else
				bArrive.erase(bArrive.begin());
			aArrive.push_back(t.bTimes[bCounter].end);
			bCounter ++;
		}
		if (aCounter == t.aTimes.size())
			Adone = true;
		if (bCounter == t.bTimes.size())
			Bdone = true;

		sort(aArrive.begin(), aArrive.end());
		sort(bArrive.begin(), bArrive.end());
	}
}

int main(int argc, char* argv[]) {
	vector<testcase> myTestCases = readInput("C:\\train.txt");
	fstream fout;
	fout.open("c:\\trainout.txt", ios::out);
	for(unsigned int i=0; i < myTestCases.size();  i++) {
		int nTrainsA = 0, nTrainsB = 0;
		processTestCase(myTestCases[i], nTrainsA, nTrainsB) ;
		 cout << "Case #"<<i+1<< ": "<< nTrainsA << " " << nTrainsB <<endl;
		 fout << "Case #"<<i+1<< ": "<< nTrainsA << " " << nTrainsB <<endl;
	}
}
