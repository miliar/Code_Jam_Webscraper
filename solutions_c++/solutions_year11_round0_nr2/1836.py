#include <iostream>
#include <xutility>
#include <vector>

using namespace std;

void SolveTest();

void main()
{
	int numTests;
	cin >> numTests;

	for(int i = 0; i < numTests; ++i)
	{
		SolveTest();
	}
}

bool IsBaseElement(char e)
{
	switch(e)
	{
	case 'Q':
	case 'W':
	case 'E':
	case 'R':
	case 'A':
	case 'S':
	case 'D':
	case 'F':
		return true;
	default:
		return false;
	}
}

typedef pair<char, char> ElementPair;
typedef pair<ElementPair, char> ElementRecipe;

bool DoesPairCombine(const vector<ElementRecipe>& combiningElements, char e1, char e2, char* result)
{
	for(vector<ElementRecipe>::const_iterator i = combiningElements.begin(); i != combiningElements.end(); ++i)
	{
		const ElementPair& bases = i->first;

		if((e1 == bases.first && e2 == bases.second) || (e1 == bases.second && e2 == bases.first))
		{
			*result = i->second;
			return true;
		}
	}
	return false;
}

bool DoesElementOpposeList(const vector<ElementPair>& opposingElements, const vector<char>& elemList, char newElem)
{
	for(vector<ElementPair>::const_iterator i = opposingElements.begin(); i != opposingElements.end(); ++i)
	{
		ElementPair opposingPair = *i;

		//Is newElem a member of this opposing element?
		char oppositeElem; //Sentinel char hack

		if(i->first == newElem)
			oppositeElem = i->second;
		else if(i->second == newElem)
			oppositeElem = i->first;
		else
			continue;

		//Seek for opposite elem
		for(vector<char>::const_iterator j = elemList.begin(); j != elemList.end(); ++j)
		{
			if(*j == oppositeElem)
				return true;
		}
		
	}

	return false;
}

void SolveTest() 
{
	static int testNum = 0;
	++testNum;


	int num;

	//Combinations
	vector<ElementRecipe> combiningElements;
	cin >> num;
	for(int i = 0; i < num; ++i)
	{
		char e1, e2, r;
		cin >> e1;
		cin >> e2;
		cin >> r;

		combiningElements.push_back(ElementRecipe(ElementPair(e1, e2), r));
	}

	//Opposing elements
	vector<ElementPair> opposingElements;
	cin >> num;
	for(int i = 0; i < num; ++i)
	{
		char e1, e2;
		cin >> e1;
		cin >> e2;

		opposingElements.push_back(ElementPair(e1, e2));
	}

	//Instructions
	vector<char> elemList;
	cin >> num;
	for(int i = 0; i < num; ++i)
	{
		char nextElem;
		cin >> nextElem;

		//Check if it combines with last element
		if(elemList.size() > 0 && DoesPairCombine(combiningElements, elemList.back(), nextElem, &nextElem))
		{
			//Get rid of last element, we'll insert in as part of normal loop
			elemList.pop_back();
		}

		//Check for opposing
		if(DoesElementOpposeList(opposingElements, elemList, nextElem))
			elemList.clear();
		else
			elemList.push_back(nextElem);
	}


	cout << "Case #" << testNum << ": [";
	for(vector<char>::const_iterator i = elemList.begin(); i != elemList.end(); ++i)
	{
		if(i != elemList.begin())
			cout << ", ";

		cout << *i;
	}
	cout << ']' << endl;
}
