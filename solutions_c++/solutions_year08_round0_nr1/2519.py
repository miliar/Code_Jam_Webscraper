#include <string>
#include <fstream>
#include <iostream>

int FindPath(const std::string& serverName, const int& startPos, const std::string queries[], const int& numQueries);

const std::string INPUT_FILE = "A-large.in";
const std::string OUTPUT_FILE = "A-large.out";

int main()
{
	std::ifstream infile;
	std::ofstream outfile;

	int numTestCases;

	infile.open(INPUT_FILE.data());
	outfile.open(OUTPUT_FILE.data());

	if (!infile || !outfile)
	{
		return 1;
	}	

	//read number of test cases
	infile>>numTestCases;

	
	for (int i=0; i<numTestCases; i++)
	{
		int numSearchEngines;
		std::string* searchEngines = NULL;

		int numQueries = 0;
		std::string* queries = NULL;

		int* results = NULL;
		int numSwitches = 0;

		//build list of search engines for this case
		infile>>numSearchEngines;
		infile.ignore(); //eat newline character

		searchEngines = new std::string[numSearchEngines];

		results = new int[numSearchEngines];  //hold results

		for(int j=0; j<numSearchEngines; j++)
		{
			getline(infile, searchEngines[j]);
		}

		//build list of queues for this case
		infile>>numQueries;
		infile.ignore(); //eat newline character

		if (numQueries > 0)  //if there are no incomming queries then there are no switches required
		{
			queries = new std::string[numQueries];

			for (int j=0; j<numQueries; j++)
			{
				getline(infile, queries[j]);
			}

			if (numQueries >= numSearchEngines)
			{
				//figure out the least possible number of switches needed
				int farthest = 0;
				bool foundGoal = false;

				//decide which search engine to use initially by seeing who will get us the farthest
				for(int s = 0; s<numSearchEngines; s++)
				{
					for (int q = 0; q<numQueries;)
					{
						//if we find a collision, see if it is the closest to the end of the list so far
						if (searchEngines[s] == queries[q])
						{
							if (q > farthest)
								farthest = q;
							break;
						}

						q++;
						
						if (q == numQueries)//we reached the end no switches necessary
							foundGoal = true;
					}

					if (foundGoal) // no need to check further search engines
						break;
				}

				if (!foundGoal) // we need to do some switching
				{
					while (farthest != numQueries)
					{
						numSwitches++;
						int nextFarthest = 0;

						for (int s=0; s < numSearchEngines; s++)
						{
							int result = FindPath(searchEngines[s], farthest,queries,numQueries);

							if (result == numQueries)//this path needs no more switching
							{
								foundGoal = true;
								break;
							}
							else if (result > nextFarthest)//this path brings us closer to the end
								nextFarthest = result;
						}

						if (foundGoal) // finally reached the goal
							break;

						farthest = nextFarthest;//more switching needed
					}


				}
			}
		}
		

		std::cout<<"Case #"<<i+1<<": "<<numSwitches<<std::endl;
		outfile<<"Case #"<<i+1<<": "<<numSwitches<<std::endl;
		

		delete[] searchEngines;
		delete[] results;
		delete[] queries;
	}


	infile.close();
	outfile.close();


	return 0;
}

int FindPath(const std::string& serverName, const int& startPos, const std::string queries[], const int& numQueries)
{
	for (int i = startPos; i < numQueries; i++)
	{
		if (serverName == queries[i])
			return i;
	}

	return numQueries; // reached end of queries
}