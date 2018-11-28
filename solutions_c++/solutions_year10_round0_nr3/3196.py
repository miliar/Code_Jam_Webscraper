//============================================================================
// Name        : test.cpp
// Author      : gunjesh
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <map>
using namespace std;

int main() {
	//read input from file...
	int noOfRound;
	int maxNoOfPeople;
	int noOfGroup;
	vector<int> groupSize;
	int noOfTest;
	int money = 0;
	cin >> noOfTest;
	for(int i=0; i < noOfTest; i++)
	{
		groupSize.clear();
		money = 0;
		int index = 0;
		cin >> noOfRound >> maxNoOfPeople >> noOfGroup;
		int grp = 0;
		for(int j = 0; j < noOfGroup; j++)
		{
			cin >> grp ;
			groupSize.push_back(grp);
		}
		//Resolution
		for(int k =0; k < noOfRound; k++)
		{
			//vector<int> indexUsed;
			 map<int,int> mymap;
			 map<int,int>::iterator it;


			//get people for round
		//	 cout << "Round :" << k << endl;
			int peopleCount = 0;
			for(; ;)
			{
				//it = mymap.find(index);
				if(mymap.find(index) == mymap.end())
				{
					mymap[index]=1;

				}
				else
				{
					//cout << "breaking "<<endl;
					break;

				}
				peopleCount += groupSize[index];
				if(peopleCount > maxNoOfPeople)
				{
					peopleCount -= groupSize[index];
					break;
				}
				//cout << "l :" << index << endl;
				money += groupSize[index];
				index = (1+index) % noOfGroup;
				//Other logic for repetition to be put.

			}
		}






		//output to file
		cout <<"Case #" << i+1 <<": "<< money <<endl;
		//cout << noOfRound << " " <<maxNoOfPeople <<" " << noOfGroup << endl;;
		//for(int j=0; j < (int)groupSize.size(); j++)
		//	cout << groupSize[j]<< endl;
	}

	return 0;


}
