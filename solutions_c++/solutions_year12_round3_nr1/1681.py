// codejam.cpp : Defines the entry point for the console application.
//

#include <iostream>
#include <string>
#include <map>
#include <sstream>
#include <vector>
//#include "boost/iterator/counting_iterator.hpp"

using namespace std;

int multiplePaths(vector<vector<int>> data, int class1, int class2) {
	
	//cout<<'('<<class1+1<<','<<class2+1<<')';

	if (class1 == class2) {
		//cout<<'b';
		return 1;
	}
	int result = 0;
	for (int i = 0; i < data[class1].size(); i++) {
		result += multiplePaths(data,data[class1][i],class2);
		if (result >1) {
			//cout<<'c';
			return 2;
		}
	}	
	
	return result;
}

bool isDiamond(vector<vector<int>> data) {
	int nClasses = data.size(); 

	for (int i = 0; i < nClasses; i++) {
		for (int j = 0; j < nClasses; j++) {
			if (i==j) continue;
			int count = multiplePaths(data,i,j);
			if (count >1) {
				//cout<<count<<endl;
				return true;
			}
			//cout<<endl;
		}			
	}

	return false;
}

int main(int argc, char** argv[])
{	
	if (!cin.good()) return 1;

	int ntests;
	cin >> ntests;		
	if (!cin.good()) return 1;

	for (int testNumber = 1; testNumber <= ntests; testNumber++) {		
		vector<vector<int>> data;
		int nClasses;
		cin >> nClasses;
		for (int classNumber = 1; classNumber <= nClasses; classNumber++) {
			vector<int> classData;
			int nParents;
			cin >> nParents;
			for (int i = 0; i < nParents; i++) {
				int parentClass;
				cin >> parentClass;
				classData.push_back(parentClass-1);
			}
			data.push_back(classData);
			
		}

		
		//Eat newline
		//string line;
	    //getline(cin, line);	
		bool result = isDiamond(data);
		
		cout << "Case #" << testNumber << ": " << (result?"Yes":"No") << endl;
		
	}
		
	return 0;
}

