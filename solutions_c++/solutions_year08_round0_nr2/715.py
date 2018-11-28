#include <fstream>
#include <iostream>
#include <sstream>
#include <math.h>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

typedef struct 
{
	bool bAtoB;
	int departure; // in mn
	int arrival; // in mn
} T_TRIP;
	
vector<T_TRIP> vTrip;
vector<int> everUsed;

void DetermineMinTrain(int& Amin, int& Bmin, int T)
{
		
		vector<T_TRIP>::iterator itMain = vTrip.begin();		
		vector<T_TRIP>::iterator itComp = vTrip.begin();
				
		everUsed.clear();
		
		// for a given trip
		while (itMain != vTrip.end())
		{
			int cur_dep = itMain->departure;
			int cur_arr = itMain->arrival;
			bool cur_AB = itMain->bAtoB;
			
			itComp = vTrip.begin();
			int cmp = 0;
			int minDifference = -1;
			int indiceMinDifference = -1;
			
			while (itComp != vTrip.end() )
			{
				int  comp_dep = itComp->departure;
				int  comp_arr = itComp->arrival;
				bool comp_AB = itComp->bAtoB;
			
				if (comp_AB == !(cur_AB))
				{
						if (cur_dep >= comp_arr)
						{
								vector<int>::iterator it = find(everUsed.begin(), everUsed.end(), cmp);
								if (it == everUsed.end())
								{
									int difference = cur_dep - comp_arr;
									
									if (minDifference == -1) 
										minDifference = difference;
									
									if (minDifference >= difference)
									{
										minDifference = difference;
										indiceMinDifference = cmp;	
									}		 
								}						
						}			
				}
				itComp++; cmp++;
			}

			if (indiceMinDifference != -1)
			{
				if (cur_AB) 
					Amin--; 
				else 
					Bmin--;
		
				everUsed.push_back(indiceMinDifference);
			}
			
			itMain++;
		}
			
}	


int main()
{
    ifstream file("C:\\Benoit\\code jam\\Train\\B-large.in");
		ofstream fileOut("C:\\Benoit\\code jam\\Train\\B-large.out");
		string line;
		
		getline(file, line);
    int N = atoi(line.c_str());
    int NA, NB, T;
    
    for (int kk = 1 ; kk <= N ; kk++)
		{
					// T
					getline(file, line);
					T = atoi(line.c_str());
					
					// NA , NB
					getline(file, line);
					
					int posBegin = 0;
					int posSpace = 0;
					int lineSize = static_cast<int>(line.length());
					posSpace = static_cast<int>( line.find(" ", posBegin) );
					
					string word = line.substr( posBegin, posSpace - posBegin);
					NA = atoi(word.c_str());
					
					word = line.substr( posSpace + 1, lineSize - posSpace - 1);
					NB = atoi(word.c_str());
					
					// trip
					vTrip.reserve(NA + NB);
					vTrip.clear();
					
					//A to B					
					for (int ii = 0; ii < NA; ii++)
					{
						T_TRIP tt;
						tt.bAtoB = true;

						getline(file, line);
						posSpace = static_cast<int>( line.find(" ", posBegin) );
						
						// departure
						string word = line.substr( posBegin, posSpace - posBegin);
						int posSep = static_cast<int>( word.find(":", 0) );
						string hours = word.substr( 0, posSep - 0);
						string mns = word.substr( posSep + 1, static_cast<int>(word.size()) - posSep - 1);
						tt.departure = atoi(hours.c_str()) * 60 + atoi(mns.c_str());
						
						// arrival 
						word = line.substr( posSpace + 1, static_cast<int>(line.size()) - posSpace - 1);
						posSep = static_cast<int>( word.find(":", 0) );
						hours = word.substr( 0, posSep - 0);
						mns = word.substr( posSep + 1, static_cast<int>(word.size()) - posSep - 1);
						tt.arrival = atoi(hours.c_str()) * 60 + atoi(mns.c_str()) + T;
					
						vTrip.push_back(tt);
					}

					//B to A					
					for (int ii = 0; ii < NB; ii++)
					{
						T_TRIP tt;
						tt.bAtoB = false;

						getline(file, line);
						posSpace = static_cast<int>( line.find(" ", posBegin) );
						
						// departure
						string word = line.substr( posBegin, posSpace - posBegin);
						int posSep = static_cast<int>( word.find(":", 0) );
						string hours = word.substr( 0, posSep - 0);
						string mns = word.substr( posSep + 1, static_cast<int>(word.size()) - posSep - 1);
						tt.departure = atoi(hours.c_str()) * 60 + atoi(mns.c_str());
						
						// arrival 
						word = line.substr( posSpace + 1, static_cast<int>(line.size()) - posSpace - 1);
						posSep = static_cast<int>( word.find(":", 0) );
						hours = word.substr( 0, posSep - 0);
						mns = word.substr( posSep + 1, static_cast<int>(word.size()) - posSep - 1);
						tt.arrival = atoi(hours.c_str()) * 60 + atoi(mns.c_str()) + T;
						
						vTrip.push_back(tt);		
					}
	
					int Amin, Bmin;
					Amin = NA;
					Bmin = NB;
					DetermineMinTrain(Amin, Bmin, T);

					fileOut << "Case #" << kk << ": " << Amin << " " << Bmin << "\n";
		}
		  
		file.close();
		fileOut.close();
    return 0;
}