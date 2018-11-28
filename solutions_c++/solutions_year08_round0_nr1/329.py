#include <iostream>
#include <vector>
#include <string>
#include <map>

using namespace std;

static int N;
static int S;
static int Q;
static const int MAX_QUERIES = 1001;
map<string, int> servers;
string queries[MAX_QUERIES];

void initializeServers()
{
	for(map<string, int>::iterator iter = servers.begin(); iter != servers.end(); iter++)
	{
		iter->second = -1;
		//cout << iter->first << "    " << iter->second << endl;
	}
}

void printServers()
{
	for(map<string, int>::iterator iter = servers.begin(); iter != servers.end(); iter++)
	{
		cout << iter->first << "    " << iter->second << endl;
	}
}
void printQueries()
{
	for(int i = 0; i < Q; i++)
		cout << queries[Q] << endl;
}

int findServer(int SI)
{
	int count = S;
	initializeServers();
	for(int i = SI; i < Q; i++)
	{
		map<string, int>::iterator it = servers.find(queries[i]);
		if(it->second == -1)
		{
			it->second = 0;
			count--;
			if(count == 0)
				return i;
		}
	}
	return Q;
}

int main()
{
	cin >> N;

	for(int i = 0; i < N; i++)
	{
		cin >> S;
		string str;
		getline(cin, str);
		for(int j = 0; j < S; j++)
		{
			getline(cin, str);
			servers[str] = -1;
		}
		//printServers();

		cin >> Q;
		getline(cin, str);
		for(int j = 0; j < Q; j++)
		{
			getline(cin, str);
			queries[j] = str;
		}
		
		int switches = -1;
		for(int j = 0; j < Q; )
		{
			j = findServer(j);
			//cout << j << " ";
			switches++;
		}
		//cout << endl;
		if(Q == 0) switches = 0;
		cout << "Case #" << i+1 << ": " << switches << endl;
	}

	return 0;
}
