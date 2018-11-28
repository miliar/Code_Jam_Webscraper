#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

struct Snapper{

	Snapper(){
		powered=false;
		state=false;
	}

	bool powered;
	bool state;

};

bool doit(int snapperCount, int snapCount){

	vector<Snapper> snapperArr(snapperCount);
	snapperArr[0].powered=true;

	for (int i=0; i< snapCount; i++){
		for (vector<Snapper>::iterator itr=snapperArr.begin(); itr!=snapperArr.end(); itr++){
			if (itr->powered){ //switch states
				if (itr->state) itr->state=false;
				else itr->state=true;
			}		
		}

		for (vector<Snapper>::iterator itr=snapperArr.begin(); itr!=snapperArr.end()-1; itr++){
			if (itr->powered && itr->state) //send power
				(itr+1)->powered=true;	
			else (itr+1)->powered=false;
		}
	}

	if (snapperArr[snapperCount-1].powered && snapperArr[snapperCount-1].state) return true;
	else return false;




}

void main(){
	ifstream infile("A-small-attempt0.in");
	ofstream outfile("out.txt");
	
	string oneLine;
	getline(infile,oneLine);
	istringstream st(oneLine);
	int totalLines;
	st>>totalLines;
	for (int i=1; i<=totalLines; i++){
		getline(infile,oneLine);
		istringstream st(oneLine);
		int snapperCount;
		int snapCount;
		st >> snapperCount;
		st >> snapCount;
		if (doit(snapperCount, snapCount)){
			outfile<<"Case #"<<i<<": ON"<<endl;
		}
		else{
			outfile<<"Case #"<<i<<": OFF"<<endl;
		}
	
	}
}







