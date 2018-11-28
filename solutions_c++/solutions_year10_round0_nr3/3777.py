// CodeJamming.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;


int _tmain(int argc, _TCHAR* argv[])
{

	long int Cases, Groups, Capacity, Rounds, G;
	long int Money=0;
	long int sum=0;
	vector <int> All_Groups;
	vector<int>::iterator it;

	cin>>Cases;

	for(int c=0;c<Cases;c++)
	{// Cases loop
		cin >> Rounds;
		cin >> Capacity;
		cin >> Groups;
		All_Groups.clear();
		Money=0;
		sum=0;

		/// read groups
		for (int g=0;g<Groups;g++)
		{
			cin>>G;
			All_Groups.push_back(G);
		}
		

		// Rounds loop

		for (int r=0;r<Rounds;r++)
		{
			// initialize number of ppl in the game
			sum=0;

			int s=0;
			for (s=0;s<All_Groups.size();s++)
			{
				
				if( (sum+All_Groups[s])<=Capacity)
					sum=sum + All_Groups[s];
				else
					break;
			}
			// find maximum included index
			//s--;

			// rotate queue
			rotate(All_Groups.begin(),All_Groups.begin()+s,All_Groups.end());
			
			Money = Money + sum;

		}

		cout<<"Case #"<<c+1<<": "<<Money<<"\n";

	}// end of cases loop
	

	cin>>Groups;
	return 0;
}

