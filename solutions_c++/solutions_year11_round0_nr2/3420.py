#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <sstream>

#include <map>
#include <set>
#include <list>

typedef std::map<char,std::set<char>> OppositionList;
typedef std::pair<char,std::set<char>> OppositionPair;

typedef std::map<char,std::map<char, char>> AssociationList;
typedef std::pair<char,std::map<char, char>> AssociationPair;

typedef std::list<char> InvocationList;

OppositionList gOpposition;
AssociationList gAssociation;

InvocationList gInvocation;
InvocationList gTrash;
InvocationList gResult;

char getAssociation(char aElemToAppend)
{
	AssociationList::iterator elemAssociationsIt=gAssociation.find(aElemToAppend);
	if (elemAssociationsIt!=gAssociation.end())
	{
		std::map<char, char> &innerMap=elemAssociationsIt->second;
		std::map<char, char>::iterator assocIt=innerMap.find(gResult.back());

		if(assocIt!=innerMap.end())
		{
			return assocIt->second;
		}

	}

	return 0;
}

bool pruneOpposition(char aElemToAppend)
{
	OppositionList::iterator currOppositionsIt = gOpposition.find(aElemToAppend);
	if(currOppositionsIt!=gOpposition.end())
	{
		std::set<char> &opposedChars = currOppositionsIt->second;
		for(InvocationList::iterator resultIt=gResult.begin();
			resultIt!=gResult.end();
			++resultIt)
		{
			if(opposedChars.find(*resultIt)!=opposedChars.end())
			{
				//gResult.erase(resultIt, gResult.end());
				gResult.clear();
				return true;
			}
		}
	}
	
	return false;
}


void doTheStuff()
{
	for (InvocationList::iterator invocationIt=gInvocation.begin();
		invocationIt!=gInvocation.end();
		++invocationIt)
	{
		if(gResult.size())
		{
			char assoc(getAssociation(*invocationIt));
			if (assoc)
			{
				gResult.pop_back();
				gResult.push_back(assoc);
			}
			else if(!pruneOpposition(*invocationIt))
			{
				gResult.push_back(*invocationIt);
			}
		}
		else
		{
			gResult.push_back(*invocationIt);
		}
	}

}


void gCleanMethod()
{
	gOpposition.clear();
	gAssociation.clear();
	gInvocation.clear();

	gResult.clear();
	gTrash.clear();
}

int main()
{
	/************************************************************************/
	/* FILE                                                                 */
	/************************************************************************/
	std::ofstream outfile;
	outfile.open ("B.out");

	std::ifstream myfile;
	myfile.open ("B.in", std::ios::in);




	std::string line;
	getline(myfile, line);

	std::istringstream iss(line);

	unsigned int gNbCases;
	iss >> gNbCases;

#ifdef DEBUG
	std::cout << "Nb test cases : " << gNbCases << std::endl;
#endif

	for (unsigned int testId=0;
		testId < gNbCases;
		++testId)
	{
		/************************************************************************/
		/* CASE                                                                 */
		/************************************************************************/
		getline(myfile, line);
		iss = (std::istringstream(line));

		unsigned int combNB;
		iss >> combNB;

		for(unsigned int combId=0;
			combId<combNB;
			++combId)
		{
			char firstCombElem, secondCombElem, CombResultChar;
			iss >> firstCombElem >> secondCombElem >> CombResultChar;

			std::map<char, char> &assoc = gAssociation[firstCombElem];
			assoc[secondCombElem] = CombResultChar;

			std::map<char, char> &assoc2 = gAssociation[secondCombElem];
			assoc2[firstCombElem] = CombResultChar;
		}

		unsigned int oppoNB;
		iss >> oppoNB;

		for(unsigned int oppoId=0;
			oppoId<oppoNB;
			++oppoId)
		{
			char firstOppoElem, secondOppoElem;
			iss >> firstOppoElem >> secondOppoElem;

			gOpposition[firstOppoElem].insert(secondOppoElem);
			gOpposition[secondOppoElem].insert(firstOppoElem);
		}

		unsigned int invocNB;
		iss >> invocNB;

		for(unsigned int invocId=0;
			invocId<invocNB;
			++invocId)
		{
			char elem;
			iss >> elem;

			gInvocation.push_back(elem);
		}

		if(gInvocation.size())
		{
			gResult.push_back(gInvocation.front());
			gInvocation.pop_front();
			doTheStuff();
		}

#ifdef DEBUG
// 		std::cout  << "Case #" << testId+1 << ": [";
// 		if(gResult.size())
// 		{
// 			std::cout << gResult.front();
// 			gResult.pop_front();
// 
// 			for(InvocationList::iterator resultIt=gResult.begin();
// 				resultIt != gResult.end();
// 				++resultIt)
// 			{
// 				std::cout << ", " << *resultIt;
// 			}
// 		}
// 		std::cout << "]" << std::endl;
#endif
		outfile  << "Case #" << testId+1 << ": [";
		if(gResult.size())
		{
			outfile << gResult.front();
			gResult.pop_front();

			for(InvocationList::iterator resultIt=gResult.begin();
				resultIt != gResult.end();
				++resultIt)
			{
				outfile << ", " << *resultIt;
			}
		}
		outfile << "]" << std::endl;

		//Clean code
		gCleanMethod();

		/************************************************************************/
		/* ENDED CASE                                                           */
		/************************************************************************/
	}

	outfile.close();
}