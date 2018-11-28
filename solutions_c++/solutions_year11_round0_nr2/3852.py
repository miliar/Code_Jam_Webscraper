#include "codejam.h"

void qual_B()
{
	int T;
	cin >> T;
	for (int testCase = 1; testCase <= T; testCase++)
	{
		int C;
		cin >> C;
		vector<Combination> combList;
		for (int i = 1; i <= C; i++)
		{
			string combString;
			cin >> combString;

			Combination comb1;
			comb1.component1 = combString.at(0);
			comb1.component2 = combString.at(1);
			comb1.result = combString.at(2);
			combList.push_back(comb1);

			Combination comb2;
			comb2.component1 = combString.at(1);
			comb2.component2 = combString.at(0);
			comb2.result = combString.at(2);
			combList.push_back(comb2);
		}
		sort(combList.begin(), combList.end());
		
		int D;
		cin >> D;
		vector<Opposition> oppList;
		for (int i = 1; i <= D; i++)
		{
			string oppString;
			cin >> oppString;

			Opposition opp1;
			opp1.element1 = oppString[0];
			opp1.element2 = oppString[1];
			oppList.push_back(opp1);

			Opposition opp2;
			opp2.element1 = oppString[1];
			opp2.element2 = oppString[0];
			oppList.push_back(opp2);
		}
		sort(oppList.begin(), oppList.end());

		int N;
		cin >> N;
		string invocation;
		cin >> invocation;

		list<char> elementList;
		elementList.push_back(invocation.at(0));
		for(int i = 1; i < invocation.length(); i++)
		{
			elementList.push_back(invocation.at(i));
			while (isCombined(&elementList, &combList));

			if(containsOpposite(&elementList, &oppList))
			{
				elementList.clear();
				i++;
				if (i < invocation.length())
				{
					elementList.push_back(invocation.at(i));
				}
			}
		}
		
		int counter = 0;
		int max = elementList.size();
		cout << "Case #" << testCase << ": [";
		for (list<char>::iterator it = elementList.begin(); it != elementList.end(); it++)
		{
			counter++;
			string separator = (counter<max)?(", "):("");
			cout << *it << separator;
		}
		cout << "]\n";
	}
}

bool containsOpposite(list<char>* elements, vector<Opposition>* opposites)
{
	char last = elements->back();
	char opposite;
	bool lastHasOpposite = false;

	if (opposites->size() <= 0)
	{
		return false;
	}

	int start = 0, end = opposites->size() - 1, middle;
	do
	{
		middle = (start + end) / 2;
		if (last == opposites->at(start).element1)
		{
			lastHasOpposite = true;
			opposite = opposites->at(start).element2;
		}
		else if (last == opposites->at(middle).element1)
		{
			lastHasOpposite = true;
			opposite = opposites->at(middle).element2;
		}
		else if (last == opposites->at(end).element1)
		{
			lastHasOpposite = true;
			opposite = opposites->at(end).element2;
		}
		else if (last < opposites->at(middle).element1)
		{
			if (end == middle)
			{
				break;
			}
			end = middle;
		}
		else if (last > opposites->at(middle).element1)
		{
			if (start == middle)
			{
				break;
			}
			start = middle;
		}
	}
	while(end-start > 0 && !lastHasOpposite);

	if (!lastHasOpposite)
	{
		return false;
	}
	else
	{
		for (list<char>::iterator currentElement = elements->begin(); currentElement != elements->end(); currentElement++)
		{
			if (*currentElement == opposite)
			{
				return true;
			}
		}
		return false;
	}	
}

bool isCombined(list<char>* elements, vector<Combination>* combinations)
{
	if (elements->size() < 2)
	{
		return false;
	}

	char last = elements->back();
	elements->pop_back();
	char preLast = elements->back();

	char searchResult;
	if (findComb(last, preLast, combinations, &searchResult))
	{
		elements->pop_back();
		elements->push_back(searchResult);
		return true;
	}
	else
	{
		elements->push_back(last);
		return false;
	}
}

bool findComb(char component1, char component2, vector<Combination>* combinations, char* result)
{
	if (combinations->size() <= 0)
	{
		return false;
	}

	int start = 0, end = combinations->size() - 1, middle;
	do
	{
		middle = (start + end) / 2;
		if (component1 == combinations->at(start).component1)
		{
			for(int i = start; i < combinations->size() && combinations->at(i).component1 == component1; i++)
			{
				if (combinations->at(i).component2 == component2)
				{
					*result = combinations->at(i).result;
					return true;
				}
			}
			return false;
		}
		else if (component1 == combinations->at(middle).component1)
		{
			for(int i = middle; i < combinations->size() && combinations->at(i).component1 == component1; i++)
			{
				if (combinations->at(i).component2 == component2)
				{
					*result = combinations->at(i).result;
					return true;
				}
			}
			return false;
		}
		else if (component1 == combinations->at(end).component1)
		{
			for(int i = end; i < combinations->size() && combinations->at(i).component1 == component1; i++)
			{
				if (combinations->at(i).component2 == component2)
				{
					*result = combinations->at(i).result;
					return true;
				}
			}
			return false;
		}
		else if (component1 < combinations->at(middle).component1)
		{
			if (end == middle)
			{
				break;
			}
			end = middle;
		}
		else if (component1 > combinations->at(middle).component1)
		{
			if (start == middle)
			{
				break;
			}
			start = middle;
		}
	}
	while(end-start > 0);

	return false;
}

