/*
  Google Code Jam Problem "Saving The Universe"  7/16/08  8:59 p.m.
  by John Alway

*/
#include "stdio.h"
#include <vector>
#include <string>
#include <map>
#include <cmath>
#include <iostream>
#include <fstream>

using namespace std;


int NumberOfSwitches(vector<string> &Engines,vector<string> &Queries)
{

	bool good=true;
	int maxPath=0, begin=0;
	int switchCount=0;
	int numEngines=Engines.size();
	int numQueries=Queries.size();
	int j, *depth = new int[numEngines];

	while(good)
	{ 
		for(int i=0; i < numEngines; i++){
			for(j=begin; j<numQueries; j++)
			{
				if(Engines[i] == Queries[j]){
					depth[i] = j;
					break;
				}
			}
			if(j == numQueries){
				maxPath = j;
				break;
			}
			//Find greatest depth for next path/jump
			if(maxPath < depth[i]){
				maxPath = depth[i];
			}
		}
		if(maxPath >= numQueries)
			break;
	 
		switchCount++;
		begin=maxPath;
	}

	delete [] depth;
	return switchCount;
}


int main()
{

	vector<string> Engines;
	vector<string> Queries;

	int numEngines, numQueries, numSwitches;
	int idx=1;
	int cnt=0;
	char str[350], buf[350]; 
	string dataOut;
	int infile=0;
 
	//ifstream in("A-small-attempt0.in");
	ifstream in("A-large.in");
	//ifstream in("TestUniverse.in");

	if(!in){
		cout << "Cannot Open file.\n" << endl;
		return 1;
	}

	//ofstream out("smallout.txt");
	ofstream out("largeout.txt");
	//ofstream out("TestOut.txt");

	if(!out){
		cout << "Cannot Open Output File.\n" << endl;
		return 1;
	}

	in.getline(str,349);
	sscanf(str,"%d",&cnt);



	while(in){
		in.getline(str, 349); 
		sscanf(str,"%d",&numEngines);

		for(int i=0;i<numEngines;i++){
			in.getline(str, 349);
			Engines.push_back(str);
		}

		in.getline(str, 349);
		sscanf(str,"%d",&numQueries);

		for(int i=0;i<numQueries;i++){
			in.getline(str, 349);
			Queries.push_back(str);
		}

		numSwitches = NumberOfSwitches(Engines,Queries);


		sprintf(buf,"Case #%d: ",idx++);
		dataOut = buf;
		sprintf(buf,"%d",numSwitches); 
		dataOut += buf;

		cout << dataOut << endl;

		dataOut += "\r";
		out.write(dataOut.c_str(),dataOut.length());
		Engines.clear();
		Queries.clear();
		if(idx > cnt) break;
	}

	out.close();
	in.close();

	return 0;
}