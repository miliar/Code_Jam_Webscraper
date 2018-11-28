//============================================================================


//============================================================================

#include <iostream>
#include <fstream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <queue>


using namespace std;



int earnMoney(int numOfTimes, int capacity, queue <int> &groupList){

	int euro = 0;
	int tempCap = capacity;
	queue <int> tempList;
	while(numOfTimes!=0){
		
		tempCap = capacity;
		while(groupList.size()!=0){
			int group = groupList.front();

			if(tempCap >= group){
				tempCap -= group;
				euro += group;
				tempList.push(group);
				groupList.pop();
			}else{
				break;
			}
		}
		while(tempList.size()!=0){		
			groupList.push(tempList.front());
			tempList.pop();
		}
	
		numOfTimes--;
	} 

	return euro;
};

int main() {

	ifstream inData;
	ofstream outData;
	
	//char  fileName[256];

	//cin.getline(fileName,256);
	outData.open("outputFile");
	inData.open("inputFile");
//	inData.open(fileName);
	if(!inData){
		cerr << "error input file error"<<endl;
		exit(1);
	}
	int nLines;

	inData >> nLines;


	int count =1;
	while(!inData.eof() && nLines !=0 ){
	

		int numOfTimes,	capacity, numOfGroup;;

		inData >> numOfTimes;
		inData >> capacity;
		inData >> numOfGroup;

		queue <int> groupList;

		while(numOfGroup!=0){
			int numOfPeop;
			inData >> numOfPeop;
			groupList.push(numOfPeop);
			numOfGroup--;
		}

		int euros = earnMoney(numOfTimes, capacity, groupList);


		outData << "Case #"<< count << ": "<< euros<<endl;

		count++;
		nLines--;
		

	}

	inData.close();
	outData.close();

	system("PAUSE");
	return 0;
}

