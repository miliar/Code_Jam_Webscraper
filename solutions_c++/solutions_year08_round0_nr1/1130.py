#include <stdio.h>
#include <iostream>
#include <map>
#include <string.h>
#include <string>

using namespace std;

struct se
{
	string name;
	int ctr;
};

map<string,int> data;
se myarray[101];
int max, searchengines;

void cleararray()
{
	for(int i = 0; i < searchengines; i++)
		myarray[i].ctr = 0;
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int cases, queries, ctr = 1, result, i, ubah, max;
	string name;

	scanf("%i", &cases);
	while(cases--)
	{
		result = 0;
		scanf("%i\n", &searchengines);
		data.clear();

		for(i = 0; i < searchengines; i++)
		{
			getline(cin, name);
			data.insert(pair<string,int>(name, i));
			myarray[i].name = name;
			myarray[i].ctr = 0;
		}

		scanf("%i\n", &queries);

		ubah = 0;
		for(i = 0; i < queries; i++)
		{
			getline(cin, name);
			myarray[ data[name] ].ctr++;
			if(myarray[ data[name] ].ctr == 1)
			{
				ubah++;
			}
			if(ubah == searchengines)
			{
				result++;
				cleararray();
				myarray[ data[name] ].ctr = 1;
				ubah = 1;
			}
		}
		printf("Case #%i: %i\n", ctr, result);
		ctr++;
	}

	return 0;
}