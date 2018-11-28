// prob31.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <vector>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

class ListEntry
{
public:
	ListEntry* next;
	int	value;
	int count;

	ListEntry(int v) : value(v){ next = NULL; count = 0; }
	void Append(ListEntry* entry)
	{ entry->next = next; next = entry; }
};

typedef ListEntry* PListEntry;

int _tmain(int argc, _TCHAR* argv[])
{
	int T, R, k, N;
	
	ifstream from("input.txt");
	ofstream to("output.txt");

	string input;
	getline(from, input);
	T = atoi(input.c_str());
	vector<int> queue;

	for(int i = 0; i < T; i++)
	{
		queue.clear();
		input.clear();
		getline(from, input);
		istringstream ist(input);
		ostringstream ost;

		ist >> R >> k >> N;
		input.clear();
		getline(from, input);
		istringstream ist2(input);
		for(int j = 0; j < N; j++)
		{
			int num;
			ist2 >> num;
			queue.push_back(num);
		}
	
		PListEntry roundRobin;
		if(queue.size())
			roundRobin = new ListEntry(*(queue.begin()));

		roundRobin->next = roundRobin;
		PListEntry entry = roundRobin, entry2;

		vector<int>::iterator iter = queue.begin();
		for(iter++; iter != queue.end(); iter++)
		{
			entry2 = new ListEntry(*iter);
			entry->Append(entry2);
			entry = entry2;
		}

		int accounting = 0;

		for(int j = 0; j < R; j++ )
		{
			int payload = 0;
			while(true)
			{
				entry = roundRobin;
				if(entry->count > j) break;
				if(payload + entry->value <= k)
				{
					entry->count++;
					payload += entry->value;
					roundRobin = entry->next;
				}
				else break;
			}
			accounting += payload;
		}

		for(size_t l = 0; l < queue.size(); l++)
		{
			entry = roundRobin->next;
			free(roundRobin);
			roundRobin = entry;
		}     

		ost<<"Case #"<< i+1 <<": "<< accounting <<'\n';
		to << ost.str();
	}

	from.close();
	to.close();

	return 0;
}

