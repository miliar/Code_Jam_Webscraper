#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdlib>
#include <algorithm>

using namespace std;

//#define SMALL
#define BIG

#ifdef BIG
	#ifdef SMALL
		#undef SMALL
	#endif
#endif

//#define CASE_INSENSITIVE


const int HASH_SIZE = 12697;
const int MAGIC_NUMBER = 13;
const int INFINITE = 1<<30;

const int MAXS = 100;
const int MAXQ = 1000;

const int LINE_LENGTH = 200;

std::vector<std::string> engines;

std::vector<std::vector<int> > hashTable;

std::vector<int> queries;
std::vector<int> next;
std::vector<int> solution; //solution[i] - the solution of the suproblem starting at i


void strToLow(char* szString)
{
	for (; *szString; ++szString)
	{
		if ((*szString) >= 'A' && (*szString) <= 'Z')
		{
			*szString = (*szString) - 'A' + 'a';
		}
	}
}

int hashCode(char* szString)
{
	int hash = 0; 
	for (; *szString; ++szString)
	{
		hash = (hash * MAGIC_NUMBER + (*szString)) % HASH_SIZE;
	}
	return hash;
}

void solve(std::istream& in, std::ostream& out)
{
	char line[LINE_LENGTH];
	int nTests = 0;
	int nEngines = 0;
	int nQueries = 0;
	
	in.getline(line, LINE_LENGTH);
	nTests = atoi(line);

	for (int testCase = 1; testCase <= nTests; ++testCase)
	{
		//clean the global data
		hashTable.clear();
		queries.clear();
		next.clear();
		solution.clear();
		engines.clear();

		//allocate a new hash table
		hashTable.resize(HASH_SIZE);

		in.getline(line, LINE_LENGTH);
		nEngines = atoi(line);

		next.resize(nEngines);
		
		for (int i = 0; i < nEngines; ++i)
		{
			in.getline(line, LINE_LENGTH);

			#ifdef CASE_INSENSITIVE
				strToLow(line);
			#endif
			int hCode = hashCode(line);

			engines.push_back(std::string(line));

			hashTable[hCode].push_back(i);
		}

		in.getline(line, LINE_LENGTH);
		nQueries = atoi(line);

		solution.resize(nQueries + 1);
		queries.resize(nQueries);

		for (int i = 0; i < nQueries; ++i)
		{
			in.getline(line, LINE_LENGTH);

			#ifdef CASE_INSENSITIVE
				strToLow(line);
			#endif

			int hCode = hashCode(line);
			std::string s(line);
			

			int index = -1;

			std::vector<int>::iterator it;

			for (it = hashTable[hCode].begin(); it != hashTable[hCode].end(); ++it)
			{
				if (s == engines[*it])
				{
					index = *it;
					break;
				}
			}

			if (index == -1)
			{
				std::cout<<"UNEXPECTED!"<<std::endl;
				return;
			}

			queries[i] = index;
		}

		for (int i = 0; i < nEngines; ++i)
		{
			next[i] = nQueries;
		}

		solution[nQueries] = -1;
		if (nQueries == 0)
			solution[nQueries] = 0;

		for (int i = nQueries - 1; i >= 0; --i)
		{
			solution[i] = INFINITE;

			next[queries[i]] = i;
			for (int j = 0; j < nEngines; ++j)
			{
				if (queries[i] != j)
				{
					solution[i] = std::min(solution[i], 1 + solution[next[j]]);
				}
			}
		}

		out<<"Case #"<<testCase<<": "<<solution[0]<<std::endl;
	}
}

int main()
{
	#ifdef SMALL
		std::ifstream in("smallin.txt");
		std::ofstream out("smallout.txt");
		solve(in, out);
		in.close();
		out.close();
	#endif

	#ifdef BIG
		std::ifstream in("bigin.txt");
		std::ofstream out("bigout.txt");
		solve(in, out);
		in.close();
		out.close();
	#endif
	return 0;
}
