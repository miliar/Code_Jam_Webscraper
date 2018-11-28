#include <iostream>
#include <fstream>
#include <list>


//A: crying kid
//B: mean brother 
struct Node
{
	Node()
	{
		valueB = 0;
		A = 0;
		B = 0;
	}
	Node(int initA, int initB, int initValueB)
	{
		valueB = initValueB;
		A = initA;
		B = initB;
	}
	int valueB;
	int A;
	int B;
};


int main()
{
	std::ifstream input("input.txt");

	int TestCasesNumbers;
	input >> TestCasesNumbers;

	std::ofstream output("output.txt");

	for (int i = 0; i < TestCasesNumbers; i++)
	{
		int numberCandies = 0;
		input >> numberCandies;
		std::list<int> listCandy;
		listCandy.clear();

		for (int j = 0; j < numberCandies; j++)
		{
			int curCandy = 0;
			input >> curCandy;
			listCandy.push_back(curCandy);
		}
		std::list<Node> List1;
		std::list<Node> List2;
		std::list<Node> *curList = &List1;
		std::list<Node> *nextList = &List2;
		std::list<Node> *tmpList = 0;

		curList->push_back(Node());

		for (std::list<int>::const_iterator iterCandy = listCandy.begin(); iterCandy != listCandy.end(); iterCandy++)
		{
			nextList->clear();
			for(std::list<Node>::const_iterator iterCurNode = curList->begin(); iterCurNode != curList->end(); iterCurNode++)
			{
				// Give the candy to crying kid
				nextList->push_back(Node(iterCurNode->A ^ *iterCandy, iterCurNode->B, iterCurNode->valueB));
				// Give the candy to mean brother
				nextList->push_back(Node(iterCurNode->A, iterCurNode->B ^ *iterCandy, iterCurNode->valueB + *iterCandy));
			}
			tmpList = nextList;
			nextList = curList;
			curList = tmpList;
		}

		int maxB = -1;

		for(std::list<Node>::const_iterator iterCurNode = curList->begin(); iterCurNode != curList->end(); iterCurNode++)
		{
			if (iterCurNode->A == iterCurNode->B && iterCurNode->A != 0 && iterCurNode->valueB > maxB)
				maxB = iterCurNode->valueB;
		}
		if (maxB == -1)
			output << "Case #" << i + 1 << ": NO" << std::endl;
		else
			output << "Case #" << i + 1 << ": " << maxB << std::endl;
	}
	return 0;
}