#include <iostream>
#include <string>
#include <stdio.h>
using namespace std;

int N, S, Q;
int* queries; 
char* query = new char[128];

bool* foundNames = new bool[1024];

int CountSwitches(int position)
{
	int invalidatedSearchEngines = 0;
	for(int i = 0; i < S; i++)
	{
		foundNames[i] = false;
	}
	
	for(int i = position; i < Q; i++)
	{
		if(foundNames[queries[i]] == false)
		{
			foundNames[queries[i]] = true;
			invalidatedSearchEngines++;
			if(invalidatedSearchEngines == S)
			{
				return CountSwitches(i) + 1;
			}
		}
	}

	return 0;
}

int main()
{
	cin >> N;
	for(int ca = 0; ca < N; ca++)
	{
		cin >> S;

		char** ses = new char*[S];
		cin.getline(query, 128);
		for(int i = 0; i < S; i++)
		{
			ses[i] = new char[128];
			//fscanf(stdin, "%s", ses[i]);
			cin.getline(ses[i], 128, '\n');
		}

		cin >> Q;
		queries = new int[Q];
		cin.getline(query, 128);
		for(int i = 0; i< Q; i++)
		{
			cin.getline(query, 128, '\n');
			for(int j = 0; j < S; j++)
			{
				if(strcmp(query, ses[j]) == 0)
				{
					queries[i] = j;
					break;
				}
			}
		}

		

		cout << "Case #" << ca + 1 << ": " << CountSwitches(0) << endl;

		delete[] queries;

		for(int i = 0; i < S; i++)
			delete[] ses[i];
		delete ses;
	}

	return 0;
}
