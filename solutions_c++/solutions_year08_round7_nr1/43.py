#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <set>
#include <map>
#include <iterator>
#include <functional>
#include <algorithm>
#include <string>

using namespace std;

::std::ifstream testCasesStream("input.in");
::std::ofstream outputCasesStream("output.txt");

::std::string getWord()
{
	::std::string word;
	while(testCasesStream.peek() == ' '
		|| testCasesStream.peek() == '\n') testCasesStream.get();
	while (!testCasesStream.eof() && testCasesStream.peek() != ' '
		 && testCasesStream.peek() != '\n')
	{
		word.push_back(testCasesStream.get());
	}
	return word;
}

map<string, vector<string>> mixtures;
map<string, int> mixturesBowls;
string firstMixture;

int calc(string const& aMixtureName)
{
	if (islower(aMixtureName[0])) return 0;
	vector<int> cost;
	vector<string> const& ings = mixtures[aMixtureName];
	for (unsigned int i = 0; i < ings.size(); i++)
	{
		cost.push_back(calc(ings[i]));
	}

	::std::sort(cost.rbegin(), cost.rend());
	int total = ings.size() + 1;
	for (unsigned int i = 0; i < cost.size(); ++i)
	{
		int temp;
		temp = cost[i] + i;
		if (total < temp)
		{
			total = temp;
		}
	}
	return total;
}

int calcAll()
{
	return calc(firstMixture);
}

int main(int /*argc*/, char* /*argv*/[])
{

	unsigned int numberOfCases;
	testCasesStream >> numberOfCases;
	for (unsigned int caseIndex = 1; caseIndex <= numberOfCases; ++caseIndex)
	{
		mixtures.clear();
		mixturesBowls.clear();
		unsigned int mixtureCount;
		testCasesStream >> mixtureCount;
		for (unsigned int mixtureIndex = 0; mixtureIndex < mixtureCount; ++mixtureIndex)
		{
			::std::string mixtureName = getWord();
			if (mixtureIndex == 0)
			{
				firstMixture = mixtureName;
			}
			unsigned int ingredientesCount;
			testCasesStream >> ingredientesCount;
			vector<string> ingredients;
			for (unsigned int ingredientIndex = 0; ingredientIndex < ingredientesCount; ++ingredientIndex)
			{
				string lala = getWord();
				if (!islower(lala[0]))				ingredients.push_back(lala);
			}
			mixtures[mixtureName] = ingredients;
		}
		if (islower(firstMixture[0]))
		{
			outputCasesStream << "Case #" << caseIndex <<  ": 1\n";
		}
		else
		{
			int solution = calcAll();
			outputCasesStream << "Case #" << caseIndex <<  ": " << solution << "\n";
		}
	}
	return 0;
}