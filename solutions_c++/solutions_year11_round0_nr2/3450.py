#include <string>
#include <sstream>
#include <fstream>
#include <vector>
#include <algorithm>
using namespace std;



int C;
char** Combinations;
int D;
char** Oppositions;
int N;
char* Invocations;

vector<char> FinalInvocations;



void FindFinalInvocations();



int main()
{
	ifstream inputFileReader("input.txt");
	ofstream outputFileWriter("output.txt");

	if (!inputFileReader || !outputFileWriter)
	{
		return 1;
	}

	// Load number of test cases.

	string inputLine;
	stringstream inputLineReader;

	getline(inputFileReader, inputLine);
	inputLineReader << inputLine;

	int T;
	inputLineReader >> T;

	// For each testcase...

	for (int testCaseIndex = 0; testCaseIndex < T; testCaseIndex++)
	{
		// ...load combinations,...

		inputLineReader.clear();
		getline(inputFileReader, inputLine);
		inputLineReader << inputLine;

		inputLineReader >> C;

		Combinations = new char* [C];

		for (int combinationIndex = 0; combinationIndex < C; combinationIndex++)
		{
			char* combination = new char [3];
			Combinations[combinationIndex] = combination;

			inputLineReader >> combination[0] >> combination[1] >> combination[2];
		}

		// ...oppositions,...

		inputLineReader >> D;

		Oppositions = new char* [D];

		for (int oppositionIndex = 0; oppositionIndex < D; oppositionIndex++)
		{
			char* opposition = new char [2];
			Oppositions[oppositionIndex] = opposition;

			inputLineReader >> opposition[0] >> opposition[1];
		}

		// ...invocations,...

		inputLineReader >> N;

		Invocations = new char [N];

		for (int invocationIndex = 0; invocationIndex < N; invocationIndex++)
		{
			inputLineReader >> Invocations[invocationIndex];
		}

		// ...calculate result and...

		FindFinalInvocations();

		delete [] Invocations;

		for (int oppositionIndex = 0; oppositionIndex < D; oppositionIndex++)
		{
			delete [] Oppositions[oppositionIndex];
		}

		delete [] Oppositions;

		for (int combinationIndex = 0; combinationIndex < C; combinationIndex++)
		{
			delete [] Combinations[combinationIndex];
		}

		delete [] Combinations;

		// ...save it to file.

		outputFileWriter << "Case #" << (testCaseIndex + 1) << ": [";

		for (int invocationIndex = 0; invocationIndex < FinalInvocations.size(); invocationIndex++)
		{
			outputFileWriter << FinalInvocations[invocationIndex];

			if (invocationIndex < FinalInvocations.size() - 1)
			{
				outputFileWriter << ", ";
			}
		}

		outputFileWriter << "]" << endl;
	}

	inputFileReader.close();
	outputFileWriter.close();

	return 0;
}



void FindFinalInvocations()
{
	FinalInvocations.clear();

	for (int invocationIndex = 0; invocationIndex < N; invocationIndex++)
	{
		char invocation = Invocations[invocationIndex];
		
		if (FinalInvocations.empty())
		{
			FinalInvocations.push_back(invocation);
			continue;
		}

		int lastFinalInvocationIndex = FinalInvocations.size() - 1;
		char lastFinalInvocation = FinalInvocations[lastFinalInvocationIndex];

		bool combined = false;

		for (int combinationIndex = 0; combinationIndex < C; combinationIndex++)
		{
			char* combination = Combinations[combinationIndex];

			if ((invocation == combination[0] && lastFinalInvocation == combination[1]) ||
				(invocation == combination[1] && lastFinalInvocation == combination[0]))
			{
				FinalInvocations[lastFinalInvocationIndex] = combination[2];
				combined = true;
				break;
			}
		}

		if (combined)
		{
			continue;
		}

		bool opposed = false;

		for (int oppositionIndex = 0; oppositionIndex < D; oppositionIndex++)
		{
			char* opposition = Oppositions[oppositionIndex];

			if ((invocation == opposition[0] &&
				find(FinalInvocations.begin(), FinalInvocations.end(), opposition[1]) != FinalInvocations.end()) ||
				(invocation == opposition[1] &&
				find(FinalInvocations.begin(), FinalInvocations.end(), opposition[0]) != FinalInvocations.end()))
			{
				FinalInvocations.clear();
				opposed = true;
				break;
			}
		}

		if (opposed)
		{
			continue;
		}

		FinalInvocations.push_back(invocation);
	}
}