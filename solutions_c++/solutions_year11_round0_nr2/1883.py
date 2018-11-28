#include "stdafx.h"
#include <iostream>
#include <map>
#include <vector>
#include <set>
#include <string>
using namespace std;

// Usage: Magicka < input.in > output.out
// TODO: more validity checks on input file

// Read a relation (combination or opposition)
string readRelation(istream &in)
{
	string relation;
	in >> relation;

	// Sort in alphabetical order the 2 first character of the string
	// Those are elements and all relations are symmetric, so it is easier to store it that way
	// (else we would have to handle both possibilities)
	if(relation[0] > relation[1])
	{
		// Switch s[0] and s[1]
		relation[0] ^= relation[1];
		relation[1] ^= relation[0];
		relation[0] ^= relation[1];
	}

	return relation;
}

// Return string "e1e2" or "e2e1", whichever is alphabetically sorted, and so can be used
// to search a relation
string sortedString(char e1, char e2)
{
	char pair[2];
	if(e1 < e2)
	{
		pair[0] = e1; pair[1] = e2;
	}
	else
	{
		pair[0] = e2; pair[1] = e1;
	}
	return string(pair, 2);
}

// Return the result of combination of e1 and e2, or \'0' if they ar not combinable
char combine(char e1, char e2, map<string, char> &combinations)
{
	map<string, char>::iterator it = combinations.find(sortedString(e1,e2));
	if(it != combinations.end())
	{
		// Found combination
		return it->second;
	}

	// No combination found
	return '\0';
}

// Return true if e is oposed to any element in elements
bool oppose(char e, vector<char> &elements, set<string> opposites)
{
	for(vector<char>::iterator it = elements.begin(); it!=elements.end(); ++it)
	{
		if(opposites.count(sortedString(e, *it)) > 0)
		{
			return true;
		}
	}

	return false;
}


int main(int argc, char* argv[])
{
	int T; // Number of test cases
	cin >> T;
	
	// For each test case / line in file
	for(int t=0; t<T; t++)
	{
		// Read combinations
		int C; // Number of combinations
		cin >> C;
		map<string, char> combinations;
		for(int i=0; i<C; i++)
		{
			string combination = readRelation(cin);
			combinations[combination.substr(0, 2)] = combination[2];
		}
		
		// Read opposite pairs
		int D; // Number of opposite couple
		cin >> D;
		set<string> opposites;
		for(int i=0; i<D; i++)
		{
			opposites.insert(readRelation(cin));
		}

		// Reazd invoked elements series
		int N; // Number of elements in series
		cin >> N;
		vector<char> elements;
		for(int i=0; i<N; i++)
		{
			char element;
			cin >> element;

			if(elements.empty())
			{
				elements.push_back(element);
			}
			else
			{
				char c = combine(element, elements.back(), combinations);
				if(c != '\0')
				{
					// Combinable
					elements.back() = c;
				}
				else if(oppose(element, elements, opposites))
				{
					// Opposition
					elements.clear();
				}
				else
				{
					elements.push_back(element);
				}
			}
		}

		cout << "Case #" << t+1 << ": [";
		for(vector<char>::iterator it = elements.begin(); it != elements.end(); ++it)
		{
			if(it != elements.begin()) cout << ", ";
			cout << *it;
		}
		cout << "]" << endl;
	}

	return 0;
}

