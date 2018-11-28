#include <iostream>
#include <fstream>
#include <string>
using namespace std;

int main(){
	int numberEngines, numberQueries, numberSwitches, numberCases;
	numberQueries = 0;
	numberSwitches = 0;

	bool engineUsed[100];
	for (int i = 0; i < 20; i++) engineUsed[i] = false;

	string engines[100];
	int queries[1000];
	
	ifstream inFile;
	inFile.open("1.in");

	ofstream outFile;
	outFile.open("1.out");
	//cout<<"here!";

	//get number queries
	inFile>>numberCases;
	//cout<<"numq:"<<numberCases<<endl;

	int counter = 1;
	int tmp;

	//for each query
	while (counter <= numberCases){
		//cout<<"counter:"<<counter<<endl;
		//get number search engines
		inFile>>numberEngines;

		//cout<<"engines:"<<numberEngines;
		//get all the search engines into an array
		getline(inFile,engines[0]);
		for (int i = 0; i < numberEngines; i++){
			//engines[i] = getline(inFile);
			getline(inFile,engines[i]);
			//engines[i] = inFile.getline();
			//inFile>>engines[i];
			//cout<<i<<engines[i]<<endl;
		}

		string temp1;

		//get all the queries into an array
		inFile>>numberQueries;
		//cout<<"numqs:"<<numberQueries<<endl;
		getline(inFile,temp1);
		for (int i = 0; i < numberQueries; i++){
			//inFile>>temp1;
			getline(inFile, temp1);
			//temp1 = inFile.getline();
			//cout<<"TEMP:::"<<temp1<<endl;
			//replace the query with the index of its search engine's value in the search engine array
			for (int j = 0; j < numberEngines; j++){
				//cout<<"engine[j]:"<<engines[j]<<endl;
				if (temp1 == engines[j]) queries[i] = j;
			}
		}

		//now the real work begins
		int queryHolder = 0;
		while (queryHolder < numberQueries){

			//counts how many engines have been used
			int numUsed = 0;

			//check to see if all but one engine has been used or not
			for (int i = 0; i < numberEngines; i++){
				if (engineUsed[i]) numUsed++;
			}
	
			//if all have been searched we have to switch
			if (numUsed == numberEngines - 1 && engineUsed[queries[queryHolder]] == false){
				numberSwitches++;

				//clear out that array
				for (int i = 0; i < numberEngines; i++) engineUsed[i] = false;

				//make sure we've counted that last search engine as used
				engineUsed[queries[queryHolder]] = true;
				queryHolder++;

			}
			else{
				//work until every search engine but one has been searched; this means we have to switch
				if (engineUsed[queries[queryHolder]] == false){
					engineUsed[queries[queryHolder]] = true;
				}
				//advance to the next query
				queryHolder++;
			}
		}

		//after we're done with one test case, show our output and reset all the variables
		outFile<<"Case #"<<counter<<": "<<numberSwitches<<endl;
		
		numberSwitches = 0;
		for (int i = 0; i < numberEngines; i++) engineUsed[i] = false;
	
		counter++;
	}

	inFile.close();
	outFile.close();

}