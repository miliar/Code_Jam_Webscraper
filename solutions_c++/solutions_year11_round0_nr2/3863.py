#include <fstream>
#include <iostream>
#include <vector>

using namespace std;

typedef struct
{
	char a;
	char b;
	char c;
} Combine;

typedef struct
{
	char a;
	char b;
} Opposed;

void Process(std::vector < Combine > & combineVector, std::vector < Opposed > & opposedVector,
             std::vector < char > & invocationVector);

int main(void)
{
	char                    invoke       = 0;
	Combine                 combine;
	ifstream                input;
	int                     combinations = 0;
	int                     combination  = 0;
	int                     invocation   = 0;
	int                     invocations  = 0;
	int                     move         = 0;
	int                     moves        = 0;
	int                     opposition   = 0;
	int                     oppositions  = 0;
	int                     testCase     = 0;
	int                     testCases    = 0;
	ofstream                output;
	Opposed                 opposed;
	size_t                  ii;
	std::vector < char >    invocationVector;
	std::vector < Combine > combineVector;
	std::vector < Opposed > opposedVector;

	//----------------------------------------------------------------------------------------------
	//  Open the input file.
	//----------------------------------------------------------------------------------------------
	input.open("B-small.in");
	if (false == input.is_open())
	{
		cout << "Unable to open input file!" << endl;
		return 1;
	}

	//----------------------------------------------------------------------------------------------
	//  Open the output file.
	//----------------------------------------------------------------------------------------------
	output.open("B-small.out");
	if (false == output.is_open())
	{
		cout << "Unable to open output file!" << endl;
		input.close();
		return 2;
	}

	//----------------------------------------------------------------------------------------------
	//  Load the input file.
	//----------------------------------------------------------------------------------------------
	input >> testCases;

	//----------------------------------------------------------------------------------------------
	//  Read all the test cases.
	//----------------------------------------------------------------------------------------------
	for (testCase = 1; testCase <= testCases; testCase++)
	{
		//------------------------------------------------------------------------------------------
		//  Read the combine rules.
		//------------------------------------------------------------------------------------------
		combineVector.erase(combineVector.begin(), combineVector.end());
		input >> combinations;
		for (combination = 0; combination < combinations; combination++)
		{
			input >> combine.a;
			input >> combine.b;
			input >> combine.c;
			combineVector.push_back(combine);
		}

		//------------------------------------------------------------------------------------------
		//  Read the opposed rules.
		//------------------------------------------------------------------------------------------
		opposedVector.erase(opposedVector.begin(), opposedVector.end());
		input >> oppositions;
		for (opposition = 0; opposition < oppositions; opposition++)
		{
			input >> opposed.a;
			input >> opposed.b;
			opposedVector.push_back(opposed);
		}

		//------------------------------------------------------------------------------------------
		//  Read the invocations.
		//------------------------------------------------------------------------------------------
		invocationVector.erase(invocationVector.begin(), invocationVector.end());
		input >> invocations;
		for (invocation = 0; invocation < invocations; invocation++)
		{
			input >> invoke;
			invocationVector.push_back(invoke);
		}

		Process(combineVector, opposedVector, invocationVector);

		output << "Case #" << testCase << ": [";
		for (ii = 0; ii < invocationVector.size(); ii++)
		{
			output << invocationVector[ii];
			if (ii + 1 < invocationVector.size())
				output << ", ";
		}
		output << "]" << endl;
	}

	input.close();
	output.close();

	return 0;
}

void Process(std::vector < Combine > & combineVector, std::vector < Opposed > & opposedVector,
             std::vector < char > & invocationVector)
{
	char   invocations[100] = {0};
	int    jj               = 0;
	int    ll               = 0;
	size_t ii               = 0;
	size_t kk               = 0;

	for (ii = 0; ii < invocationVector.size(); ii++)
	{
		invocations[jj++] = invocationVector[ii];

		ComBine : ;

		if (1 >= jj)
			continue;

		for (kk = 0; kk < combineVector.size(); kk++)
		{
			if ((combineVector[kk].a == invocations[jj - 1] &&
			     combineVector[kk].b == invocations[jj - 2]) ||
			    (combineVector[kk].a == invocations[jj - 2] &&
				 combineVector[kk].b == invocations[jj - 1]))
			{
				invocations[jj - 2] = combineVector[kk].c;
				jj--;
				goto ComBine;
			}
		}

		for (kk = 0; kk < opposedVector.size(); kk++)
		{
			if (opposedVector[kk].a != invocations[jj - 1] &&
			    opposedVector[kk].b != invocations[jj - 1])
			{
				continue;
			}

			for (ll = 0; ll < jj - 1; ll++)
			{
				if ((opposedVector[kk].a == invocations[jj - 1] &&
					 opposedVector[kk].b == invocations[ll]) ||
					(opposedVector[kk].a == invocations[ll] &&
					 opposedVector[kk].b == invocations[jj - 1]))
				{
					jj = 0;
					kk = opposedVector.size();
					break;
				}
			}
		}
	}

	invocationVector.erase(invocationVector.begin(), invocationVector.end());
	for (ll = 0; ll < jj; ll++)
		invocationVector.push_back(invocations[ll]);

	return;
}
