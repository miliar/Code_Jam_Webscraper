// zzz.cpp: определяет точку входа для консольного приложения.
//
// Microsoft Visual C++ 2008 Express Edition
//
// Google Code Jame 2009
//
// Pavel Yakimenko
//

#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

#define DEBUG_DATA

typedef long dataType;

bool isHappy(const dataType dig, const int base)
{
	int counter = 0;
	char digits[10];
	vector<dataType> wasHere;
	itoa(dig, digits, base);
	wasHere.push_back(dig);
	do
	{
		dataType squared = 0;
		for(int i=0; i<strlen(digits); i++)
		{
			char d[2] = {digits[i], '\0'};
			squared += (atoi(d) * atoi(d));
		}
		if(squared == 1)
			return true;
		itoa(squared, digits, base);
		counter++;
		for(int i=0; i<wasHere.size(); i++)
		{
			if(squared == wasHere[i])
				return false;
		}
		wasHere.push_back(squared);
	}
	while(true);//counter<500);
	return false;
}

dataType GetHappines(vector<dataType> &va)
{
	vector<dataType> happy;
	int digit = 2;
	while(true)//for(int digit=2; digit<500; digit++)
	{
		bool fullHappy = true;
		for(int i=0; i<va.size(); i++)
		{
			if(!isHappy(digit, va[i]))
			{
				fullHappy = false;
				break;
			}
		}
		if(fullHappy)
		{
			return digit;
		}
		digit++;
	}
}

void CoutVector(vector<dataType> &vec)
{	
#ifdef DEBUG_DATA
	for(unsigned int i=0; i<vec.size(); i++)
	{
		printf(" %d", vec[i]);
	}
	printf("\n");
#endif
}

void ReadVector(ifstream &file, vector<dataType> &vec)
{
  string s;
  getline(file, s);
  istringstream iss(s);
  copy( istream_iterator<dataType>(iss), istream_iterator<dataType>(), back_inserter(vec));

#ifdef DEBUG_DATA
	printf("Vector unsorted = ");
	CoutVector(vec);
#endif
}

bool IntSortPredicateToMax(const dataType& d1, const dataType& d2)
{
	return d1 < d2;
}

bool IntSortPredicateToMin(const dataType& d1, const dataType& d2)
{
	return d1 > d2;
}

void SortVector(vector<dataType> &vec, bool (*func)(const dataType&,const dataType&))
{
	// Sort the vector using predicate and std::sort
	std::sort(vec.begin(), vec.end(), func);
	
#ifdef DEBUG_DATA
	printf("Vector sorted = ");
	CoutVector(vec);
#endif
}

int main(int argc, char* argv[])
{
	char inFileName[1000];
	char outFileName[1000];
	
	if(argc <= 2)
	{
		strcpy_s(inFileName, "sample.in.txt");	// file name not found
		strcpy_s(outFileName, "sample.out.txt");
	}
	else
	{	
		strcpy_s(inFileName, argv[1]);
		strcpy_s(outFileName, argv[2]);
	}
#ifdef DEBUG_DATA
	printf("In = %s\n", inFileName);
	printf("Out= %s\n", outFileName);
#endif
	
	ifstream fileSamples(inFileName);
	ofstream fileResults(outFileName, ios::trunc);

	int caseCount = 0;	// test cases count
	vector<dataType> testCasesCount;
	ReadVector(fileSamples, testCasesCount);
	//fileSamples >> caseCount;
	caseCount = testCasesCount[0];
#ifdef DEBUG_DATA
	printf("Cases count = %d\n", caseCount);
#endif
	if(caseCount < 1)
		return 1;	// incorrect test cases count

	for(int caseID=1; caseID<=caseCount; caseID++)	// loop through each test
	{
#ifdef DEBUG_DATA
		printf("Case %d\n", caseID);
#endif
		vector<dataType> va;	// first vector

		// Getting vectors data from file
		ReadVector(fileSamples, va);
		
		dataType happyNumber = GetHappines(va);

		fileResults << "Case #" << caseID << ": " << happyNumber << "\n";
	}
	
	fileSamples.close();
	fileResults.close();
    return 0;
}
