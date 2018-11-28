#include <iostream>
#include <string>
using namespace std;
int main()
{
	int n, i , j, s, q, count, m;
	string *engine, *query;
	char *visited;
	int result, use, begin;
	cin>>n;
	for (i=0;i<n;i++)
	{
		result = 0;
		cin>>s;
		visited = new char[s];
		memset(visited, 0, s*sizeof(char));
		engine = new string[s];
		do   
		{   
			cin.ignore();   
		}while(cin.bad());   
		cin.clear();
		for (j=0;j<s;j++)
		{
			getline(cin,engine[j]);
		}
		
		cin>>q;
		query = new string[q];
		do   
		{   
			cin.ignore();   
		}while(cin.bad());   
		cin.clear();
		for (j=0;j<q;j++)
		{
			getline(cin, query[j]);
		}

		count = 0;
		for (j=0;j<q;j++)
		{
			for (m=0;m<s;m++)
			{
				if (!query[j].compare(engine[m]) && visited[m] == 0)
				{
					count++;
					visited[m] = 1;
					if (count == s)
					{
						use = m;
						begin = j;
						count = 1;
						result++;
						memset(visited, 0, s*sizeof(char));
						visited[m] = 1;
					}

				}
			}
		}


		cout<<"Case #"<<i+1<<": "<<result<<endl;
		//free(engine);
		//free(query);
		//free(visited);
	}
}