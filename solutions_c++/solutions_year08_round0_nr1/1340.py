#include <fstream>
#include <string>
using namespace std;

#define INFINITY 65535

int FindIndexOfMax(int* a, int n)
{
	int max = 0;
	for(int i=1;i<n;i++)
	{
		if(a[i]>a[max])
			max=i;
	}
	return max;
}

void main(int argc, char* argv[])
{
	ifstream fin;
	ofstream fout;
	int N;	//#test cases

	fin.open(argv[1], ios::in);
	fout.open(argv[2], ios::out);

	fin>>N;

	for(int index=1;index<=N;index++)
	{
		int searchEngineCount, queryCount;
		char **searchEngines, **queries;
		int *nextQueryIndex;

		//read input
		fin>>searchEngineCount;
		if(searchEngineCount==0)
		{
			//write output
			fout<<"Case #"<<index<<": 0"<<"\n";
			continue;
		}
		
		fin.seekg(2, ios_base::cur);

		searchEngines = new char*[searchEngineCount];
		for(int i=0;i<searchEngineCount;i++)
			searchEngines[i] = new char[100];
		for(int i=0;i<searchEngineCount;i++)
			fin.getline(searchEngines[i],100);

		fin>>queryCount;
		if(queryCount==0)
		{
			//write output
			fout<<"Case #"<<index<<": 0"<<"\n";
			continue;
		}

		fin.seekg(2, ios_base::cur);

		queries = new char*[queryCount];
		for(int i=0;i<queryCount;i++)
			queries[i] = new char[100];
		for(int i=0;i<queryCount;i++)
			fin.getline(queries[i],100);

		//process
		nextQueryIndex = new int[searchEngineCount];
		
		int curEngine = -1;
		int result = -1;

		for(int i=0;i<queryCount;i++)
		{
			if( (curEngine != -1) && (strcmp(searchEngines[curEngine], queries[i])!=0) )
				continue;

			result++;

			//conflict; find next searchEngine to be chosen
			//that engine should have been queried farthest from now
			for(int j=0;j<searchEngineCount;j++)
				nextQueryIndex[j] = INFINITY;	//initialize

			for(int j=i;j<queryCount;j++)
			{
				for(int k=0;k<searchEngineCount;k++)
				{
					if( (strcmp(queries[j], searchEngines[k]) == 0)
						&& nextQueryIndex[k] == INFINITY )
					{
						nextQueryIndex[k] = j;
						break;
					}
				}
			}

			curEngine = FindIndexOfMax(nextQueryIndex, searchEngineCount);
		}
		
		//write output
		fout<<"Case #"<<index<<": "<<result<<"\n";
	}

	fin.close();
	fout.close();
}