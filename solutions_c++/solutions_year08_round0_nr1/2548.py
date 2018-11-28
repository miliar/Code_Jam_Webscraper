// As you will notice this will not have any comments...so ENJOY!
#include <iostream>
#include <string>
#include <map>

using namespace std;

map<string, int> My_servers;
static const int MAX_QUERY_LIMIT = 1001;
static int varq, varn, vars;
string My_query[MAX_QUERY_LIMIT];

int findNextIndex(int SI);

int main()
{
    cin >> varn;

    for(int i = 0; i < varn; i++)
		{
			cin >> vars;
			string my_string;
			
			// i cheated..see this is a comment..though it servers no purpose except for 
			// dissipating some coding exhaustion 

			getline(cin, my_string);
			for(int j = 0; j < vars; j++)
			{
					getline(cin, my_string);
					My_servers[my_string] = -1;
			}

			cin >> varq;
			getline(cin, my_string);
			for(int j = 0; j < varq; j++)
			{
					getline(cin, my_string);
					My_query[j] = my_string;
			}
			
			int indicator = -1;
			if(varq == 0) indicator = 0;
			for(int j = 0; j < varq; )
			{
					j = findNextIndex(j);
					indicator++;
			}
			cout << "Case #" << i+1 << ": " << indicator << endl;
		}

    return 0;
}
int findNextIndex(int SI)
{
		int total = vars;

    for(map<string, int>::iterator it = My_servers.begin(); it != My_servers.end(); it++)
        it->second = -1;

		for(int i = SI; i < varq; i++)
		{
				map<string, int>::iterator it = My_servers.find(My_query[i]);
				if(it->second == -1)
				{
						it->second = 0;
						total--;
						if(total == 0)
								return i;
				}
		}
		return varq;
}
