#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

#define lint long long
#define uint usigned long long

int main (int argc, char * const argv[]) {
    
	ifstream inFile("../../input.txt");
	ofstream outFile("../../output.txt");
	int numCases;
	inFile >> numCases;
	for(int caseNum =1; caseNum <=numCases; caseNum++)
	{
		int numButtons;
		inFile>>numButtons;
		vector<int> ObutList, BbutList;
		char orderList[101];
		
		for(int cntr=0; cntr< numButtons; cntr++)
		{
			inFile>>orderList[cntr];
			int tmpInt;
			inFile>>tmpInt;
			if(orderList[cntr] == 'O')
				ObutList.push_back(tmpInt);
			else
				BbutList.push_back(tmpInt);
			
		}
			BbutList.push_back(1);
			ObutList.push_back(1);
		
		
		int stepNum =0, butNum=0;
		int Bpos=1, Opos=1;
		int BbutNum=0, ObutNum=0;
		while(butNum < numButtons)
		{
			stepNum++;
			//cout<<stepNum<<" | ";
			bool buttonPushed=false;
			if(orderList[butNum] == 'O' && Opos == ObutList[ObutNum])
			{
				ObutNum++;
				buttonPushed=true;
			//	cout<<"pushed button "<<Opos;
			}
			else if(Opos > ObutList[ObutNum])
			{
				Opos--;
			//	cout<<"moved to button "<<Opos;
			}
			else if(Opos < ObutList[ObutNum])
			{
				Opos++;
			//	cout<<"moved to button "<<Opos;
			}
			//else
			///	cout<<"stay at button "<<Opos;
			
			
			//cout<<"  | ";
			
			if(orderList[butNum] == 'B' && Bpos == BbutList[BbutNum])
			{
				BbutNum++;
				buttonPushed=true;
			//	cout<<"pushed button "<<Bpos;
			}
			else if(Bpos > BbutList[BbutNum])
			{
				Bpos--;
			//	cout<<"moved to button "<<Bpos;
			}
			else if(Bpos < BbutList[BbutNum])
			{
				Bpos++;
			//	cout<<"moved to button "<<Bpos;
			}
		///	else
			//	cout<<"stay at button "<<Bpos;

			//cout<<"\n";
			if(buttonPushed)
				butNum++;
		}
		
		outFile<<"Case #"<<caseNum<<": "<<stepNum<<"\n";
		cout<<"Case #"<<caseNum<<": "<<stepNum<<"\n";
		
	}
	inFile.close();
	outFile.close();
	std::cout << "Done!\n";
    return 0;
}
