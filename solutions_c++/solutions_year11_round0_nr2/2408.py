#include <stdio.h>
#include <stdlib.h>
#include <new>
#include <limits.h>
#include <iostream>
#include <string>
#include <map>
#include <stack>
#include <set>
#include <vector>
#include <algorithm>

#include <iterator>

using namespace std;
int compare (const void * a, const void * b)
{
  return ( *(int*)a - *(int*)b );
}

void sortIt(int *anArray, int aCount)
{
  qsort (anArray, aCount, sizeof(int), compare);
}

int main()
{
	int nrCases;	
	cin >> nrCases;
	
	for (int caseNr = 0; caseNr < nrCases; caseNr++)
	{
		int C;
		
		
		cin >> C;
		
		map<string, char> combinations;
		
		for (int i = 0; i < C; i++)
		{
			string combination;
			
			cin >> combination;
			
			char result = combination[2];
			combination.erase(2);
			string combination2;
			combination2.append(1, combination[1]).append(1, combination[0]);
			
			combinations[combination] = result;
			combinations[combination2] = result;
			

			
	//		cout << "combo: " << combination << "," << combination2 << " => " << result << endl;
		}
		
		map<char, set<char> > oppositions;
		
		int D;
		
		
		cin >> D;
		
		for (int i = 0; i < D; i++)
		{
			string opposition;
			
			cin >> opposition;
			
	//		cout << "opposition : " <<opposition << endl;

			oppositions[opposition[1]].insert(opposition[0]);
			oppositions[opposition[0]].insert(opposition[1]);
	//		ostream_iterator< char > output( cout, " " );
	//		copy( oppositions[opposition[1]].begin(), oppositions[opposition[1]].end(), output );

			
		//	cout <<endl;
		}
		

		
		int N;
		cin >> N;
		string target;
		cin >> target;
		
	//	cout << "target: " << target << endl;
		
		map<char, bool> haveInStack;
		vector<char> currentStack;
		
		for (int i = 0; i < N ; i ++)
		{
			char next = target[i];
			
	//		cout << " next : " << next << endl;
			
			if (currentStack.size() > 0)
			{
				string pair;
				pair.append(1, next);
				pair.append(1, currentStack[currentStack.size() -1 ]);
			//	cout << "pair : " << pair << " combination : " << combinations[pair] << endl;
				if (combinations[pair])
				{
					currentStack.pop_back();
					next = combinations[pair];
				}
			//	string pair = 
			}
			

		//	cout << "checking oppositions for " << next;
			
			set<char> currentOpposition = oppositions[next];
			bool opposed = false;
			
			for (int j = 0; j < currentStack.size(); j++)
			{
				if (currentOpposition.find(currentStack[j]) != currentOpposition.end())
				{
					opposed = true;
					break;
				}
			}
			
			//set_intersection( currentStack.begin(), currentStack.end(), oppositions[next].begin(), oppositions[next].end(), 
				//inserter(intersection,intersection.begin()) );
			
			if (opposed)
			{
				currentStack.clear();
			}
			else 
			{
	//		else
		//	{
			//}

				currentStack.push_back(next);
			}
			
			
//			cout << "Stack size : " << currentStack.size() << endl;
		}
		
		
		cout << "Case #" << caseNr + 1 << ": [" ;
		bool first = true;
		for (int i = 0; i < currentStack.size(); i++)
		{
			if (!first)
			{
				cout << ", ";
			}
			
			first = false;
			
			cout << currentStack[i];
		}
		
		cout << "]" << endl;
		
	}
}
