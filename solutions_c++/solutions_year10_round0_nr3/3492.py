#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <queue>

using namespace std;


int doit(int r, int k, queue<int> & groups){

	int result = 0;
	int capacity = k;
	queue<int> onBoard;

	for (int i=0; i<r; i++){
		while (groups.size()>0 && groups.front() <= capacity){
			capacity -= groups.front();
			result += groups.front();
			onBoard.push(groups.front());
			groups.pop();
		}

		capacity = k;
		while (onBoard.size()>0){ //unload
			groups.push(onBoard.front());
			onBoard.pop();
		}


	}

	return result;

}

void main(){
	ifstream infile("C-small-attempt0.in");
	ofstream outfile("out.txt");
	
	string oneLine;
	getline(infile,oneLine);
	istringstream st(oneLine);
	int totalTests;
	st>>totalTests;
	for (int i=1; i<=totalTests; i++){
		getline(infile,oneLine);
		istringstream st(oneLine);
		int r;
		int k;
		int n;
		st >> r; 
		st >> k; 
		st >> n; 


		int temp;

		getline(infile,oneLine);
		istringstream st2(oneLine);

		queue<int> groups;
		for (int j=0; j<n; j++)
		{
			st2 >> temp;
			groups.push(temp);


		}
		
		outfile<< "Case #"<<i<<": ";
		outfile<<doit(r, k, groups);
		outfile<<endl;
		
	
	}

}







