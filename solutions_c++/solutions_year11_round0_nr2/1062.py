#include <iostream>
#include <fstream>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

int main()
{
	ifstream input("B-large.in");
	ofstream output("outputl.txt");

	int T;
	input >> T;

	for(int caseID = 1; caseID <= T; caseID++)
	{
		//read data
		map<string, char> combineMap;
		map<char,vector<char> > deleteMap;
		int C,D,N;
		input >> C;
		string combinelist;

		for (int i = 0; i != C; i++)
		{
			input >> combinelist;
			string base = combinelist.substr(0,2);
			char compound = combinelist[2];
			combineMap[base] = compound;
		}

		input >> D;

		string deleteList;
		for (int i = 0; i != D; i++)
		{
			input >> deleteList;
			//deleteMap[ deleteList[0] ] = deleteList[1];
			//deleteMap[ deleteList[1] ] = deleteList[0];
			deleteMap[ deleteList[0] ].push_back(deleteList[1]);
			deleteMap[ deleteList[1] ].push_back(deleteList[0]);
		}

		input >> N;


		//solve
		vector <char> Ret;
		map<char,int> listMap;
		char temp;
		//input >> temp;
		for (int i = 0; i != N; i++)
		{
			input >> temp;
			//change last
			if (Ret.size() == 0)
			{
				Ret.push_back(temp);
				//listSet.insert(temp);
				listMap[temp] = 1;
				continue;
			}
			string toCombineA, toCombineB;
			//toCombineA = Ret[Ret.size()-1]+temp;
			toCombineA.push_back(Ret[Ret.size()-1]);
			toCombineA.push_back(temp);

			//toCombineB = temp + Ret[Ret.size()-1];
			toCombineB.push_back(temp);
			toCombineB.push_back(Ret[Ret.size()-1]);


			if (combineMap.find(toCombineA) != combineMap.end())
			{
				listMap[ Ret[Ret.size()-1] ]--;
				if (listMap[ Ret[Ret.size()-1] ] == 0)
				{
					listMap.erase(Ret[Ret.size()-1]);
				}

				Ret[Ret.size()-1] = combineMap[toCombineA];

				if (listMap.find( Ret[Ret.size()-1] ) == listMap.end())
				{
					listMap[Ret[Ret.size()-1]] = 1;
				}
				else
				{

					listMap[Ret[Ret.size()-1]]++;
				}
				//listSet.insert(Ret[Ret.size()-1]);
				continue;

			}
			else if (combineMap.find(toCombineB) != combineMap.end())
			{
				listMap[ Ret[Ret.size()-1] ]--;
				if (listMap[ Ret[Ret.size()-1] ] == 0)
				{
					listMap.erase(Ret[Ret.size()-1]);
				}

				Ret[Ret.size()-1] = combineMap[toCombineB];

				if (listMap.find(Ret[Ret.size()-1]) == listMap.end())
				{
					listMap[Ret[Ret.size()-1]] = 1;
				}
				else
				{

					listMap[Ret[Ret.size()-1]]++;
				}
				continue;
			}
			//delete
			if (deleteMap.find(temp) == deleteMap.end())
			{
				Ret.push_back(temp);
				if (listMap.find(temp) == listMap.end())
				{
					listMap[temp] = 1;
				}
				else
				{

					listMap[temp]++;
				}
				continue;

			}
			vector<char> enemy = deleteMap[temp];
			bool flag = false;
			if (!enemy.empty())
			{
				for (int i = 0; i != enemy.size();i++)
				{
					if ( listMap.find(enemy[i]) != listMap.end() )
					{
						flag = true;
						break;
					}
					
				}
				//if flag = true, clear vector, empty set
				if (flag == true)
				{
					Ret.clear();
					listMap.clear();
					continue;
				}
			}

			Ret.push_back(temp);
			if (listMap.find(temp) == listMap.end())
			{
				listMap[temp] = 1;
			}
			else
			{

				listMap[temp]++;
			}
			

			
			

			
				

			
		}

		//output result
		output << "Case #" << caseID << ": [";
		if (Ret.size() == 0)
		{
			output << "]" << endl;
			continue;
		}
		int i;
		
		for ( i = 0; i != Ret.size() -1; i++)
		{
			output << Ret[i]<<", ";
		}
		output << Ret[i] <<"]" << endl;
		//output << endl;
	}
}