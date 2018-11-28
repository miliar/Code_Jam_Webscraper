#include <fstream>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int cases;
	fin>>cases;
	int tcase = 1;
	while(cases--)
	{
		int n;
		fin>>n;
		vector <vector<int>> taskQueue;
		for(int i = 0; i < n; i++) {
			int tempInt;
			string tempStr;
			fin>>tempStr>>tempInt;
			vector <int> tempVec;
			(tempStr == "B")?tempVec.push_back(0):tempVec.push_back(1);
			tempVec.push_back(tempInt);
			taskQueue.push_back(tempVec);
		}
		vector<int> lPos;
		lPos.resize(2);
		lPos[0] = 1;
		lPos[1] = 1;
		vector<int> lTime;
		lTime.resize(2);
		lTime[0] = 0;
		lTime[1] = 0;

		int result = 0;
		while(!taskQueue.empty()) {
			vector<int> currItem = taskQueue.front();
			taskQueue.erase(taskQueue.begin());
			int currIndex = currItem[0];
			int toPosition = currItem[1];
			//getlTime
			int origTime = abs(toPosition - lPos[currIndex]);
			int timeTaken;
			if (origTime <= lTime[currIndex^1]) {
				
				timeTaken = 1;
				lTime[currIndex^1] = 0;
			} else {
				timeTaken = origTime - lTime[currIndex^1] + 1;
				lTime[currIndex^1] = 0;
			}
//			cout<<"origTime"<<origTime<<"lTime"<<lTime[currIndex^1]<<endl;
//			cout<<"timeTaken"<<timeTaken<<endl;

			//int timeTaken = abs(toPosition - lPos[currIndex])
			//int timeTaken = abs(toPosition - lPos[currIndex]),lTime[currIndex^1]) + 1;

			result += timeTaken;
			lPos[currIndex] = toPosition;
			lTime[currIndex] += timeTaken;
		}
		fout<<"Case #"<<tcase++<<": "<<result<<endl;


	}
	fin.close();
	fout.close();
	return 0;
}
