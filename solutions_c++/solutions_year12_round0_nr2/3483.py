#include <iostream>
#include <fstream>
using namespace std;

int main(int argc, char* argv[]){
	int numOfCases, numOfContestants, numOfSurprises;
	int grades, numOfGreatDancers=0, surpriseCount, p;
	int controlSum1, controlSum2;


	ofstream output;
	ifstream input;
	
	input.open(argv[1]);
	if (!input){
		cout << "Cannot open file "<<argv[1]<<endl;
		return -1;
	}
	cout << "File "<< argv[1] <<" opened for reading" <<endl;

	output.open(argv[2]);
	if (!output){
		cout << "Cannot open file "<<argv[2]<<endl;
		return -1;
	}
	cout << "File "<< argv[2] <<" opened for writing" <<endl;

	input>>numOfCases;
	

	for(int i=0; i<numOfCases; i++){
		input>>numOfContestants;
		input>>numOfSurprises;
		surpriseCount = numOfSurprises;
		input>>p;
		if (p>1){
			controlSum1 = (p-1)+(p-1)+p;
			controlSum2 = (p-2)+(p-2)+p;
		}
		else{
			controlSum1 = controlSum2 = p;
		}

		output<<"Case #" <<i+1<<": ";
		for(int j=0; j<numOfContestants; j++){
			input>>grades;
			if (grades>=controlSum1) {
				//if grades are controlSum1 or more than it is possible to have one grade greater then p without surprising result
				numOfGreatDancers++;
			}
			else if (grades>=controlSum2){
				//if grades are between controlSum1 and controlSum2 then it is possible to have one grade greater then p but with surprise
				if (surpriseCount-1>=0){
					numOfGreatDancers++;
					surpriseCount--;
				}
			}
			//if grades are less then controlSum2 then it is not possible to have one grade greater then p
		}
		output<<numOfGreatDancers<<endl;
		numOfGreatDancers=0;
	}


	cout<<"Work finished"<<endl;
	input.close();
	output.close();

	return 0;


}