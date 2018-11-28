// topcoder.cpp : Defines the entry point for the console application.
//

#include <vector>
#include <sstream>
#include <iostream>
#include <algorithm>

#define LARGE

static const unsigned int MAX_LINE = 2048;

struct FindCombination
{
	char c1;
	char c2;

	FindCombination(char _c1,char _c2):c1(_c1),c2(_c2) {}

	bool operator()(std::pair<std::pair<char,char>,char> combination)
	{
		std::pair<char,char> pairSubs = combination.first;

		return (((pairSubs.first == c1) && (pairSubs.second == c2)) ||
					((pairSubs.first == c2) && (pairSubs.second == c1)));
	}
};

struct FindOpposed
{
	char c1;
	char c2;

	FindOpposed(char _c1,char _c2):c1(_c1),c2(_c2) {}

	bool operator()(std::pair<char,char> pairOpposed)
	{
		return (((pairOpposed.first == c1) && (pairOpposed.second == c2)) ||
					((pairOpposed.first == c2) && (pairOpposed.second == c1)));
	}
};

class Problem
{
	std::string elementList;
	std::vector<std::pair<char,char> > opposites;
	std::vector<std::pair<std::pair<char,char>,char> > combinations;

	typedef std::vector<std::pair<char,char> >::iterator OppositesIterator;
	typedef std::vector<std::pair<std::pair<char,char>,char> >::iterator CombinationsIterator;

	char combineElements(char c1, char c2)
	{
		FindCombination find(c1,c2);

		CombinationsIterator it = std::find_if(combinations.begin(),combinations.end(),find);

		if (it == combinations.end())
			return 0;

		return (*it).second;
	}

	bool isOpposedToSomeElement(const std::string &elements,char element)
	{
		for (unsigned int i = 0; i < elements.size(); i++) {
			OppositesIterator it = std::find_if(opposites.begin(),opposites.end(),FindOpposed(element,elements[i]));

			if (it != opposites.end())
				return true;
		}

		return false;
	}

public:

	void setString(const std::string &str)
	{
		elementList = str;
	}

	void addOpposites(char c1, char c2)
	{
		opposites.push_back(std::pair<char,char>(c1,c2));
	}

	void addSubstitution(char c1,char c2, char s)
	{
		std::pair<char,char> chars(c1,c2);

		combinations.push_back(std::pair<std::pair<char,char>,char>(chars,s));
	}

	std::string solve()
	{
		std::string tempSolution;

		for (unsigned int i = 0; i < elementList.size(); i++) {

			char element = elementList.at(i);

			if (tempSolution.empty()) {
				tempSolution.append(1,element);
			} else {
				char combination = combineElements(element,*tempSolution.rbegin());

				if (!combination) {

					if (isOpposedToSomeElement(tempSolution,element)) {
						tempSolution = "";
					} else {
						tempSolution.append(1,element);
					}

				} else {
					tempSolution[tempSolution.size()-1] = combination;
				}

			}
		}

		std::string solution = "[";

		for (unsigned int i = 0; i < tempSolution.size(); i++) {
			solution.append(1,tempSolution[i]);

			if (i < (tempSolution.size()-1))
				solution+= ", ";
		}

		solution+= "]";

		return solution;
	}

};

static Problem parseProblem(const char *line);

int main(int argc, char* argv[])
{
	//freopen("exb.in","rt",stdin);

#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif


	char line[MAX_LINE];
	unsigned int cases;

	std::cin.getline(line,MAX_LINE);

	cases = std::atoi(line);

	for (unsigned int i = 1; i <= cases; i++) {
		std::cin.getline(line,MAX_LINE);

		Problem p = parseProblem(line);

		std::cout << "Case #" << i << ": " << p.solve() << std::endl;
	}

	return 0;
}

Problem parseProblem(const char *line)
{
	Problem problem;
	std::stringstream ss;

	ss.write(line,std::strlen(line));

	unsigned int substitutions;
	ss >> substitutions;

	for (unsigned int i = 0; i < substitutions; i++) {
		ss.get(); //discard ' '

		char temp[3];
		ss.read(temp,3);

		problem.addSubstitution(temp[0],temp[1],temp[2]);
	}

	ss.get(); //discard ' '

	unsigned int opposites;
	ss >> opposites;

	for (unsigned int i = 0; i < opposites; i++) {
		ss.get(); //discard ' '

		char temp[2];
		ss.read(temp,2);

		problem.addOpposites(temp[0],temp[1]);
	}

	ss.get(); //discard ' '

	unsigned int strSize;
	ss >> strSize;

	ss.get(); //discard ' '

	char *temp = new char[strSize+1];
	ss.read(temp,strSize);
	temp[strSize] = 0;

	problem.setString(temp);

	delete [] temp;

	return problem;
}

