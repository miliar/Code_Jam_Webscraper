#include <iostream>
#include <fstream>
#include <string>
using namespace std;

class A
{
private:
	int minimum_case;
	void find_longest_searcher(string searchers[], int which_searcher, int numberSearcher, 
							string queries[], int which_query, int numberQuery)
	{
		int which_max_searcher;
		int which_max_query = which_query;

		for(int j = 0;j < numberSearcher;++j)
		{
			if(j == which_searcher)
				continue;

			for(int i = which_query;i < numberQuery + 1;++i)
			{
				if(i == numberQuery)
					return;

				if(searchers[j] == queries[i])
				{
					if(i > which_max_query)
					{
						which_max_searcher = j;
						which_max_query = i;
					}
					break;
				}
			}
		}

		++minimum_case;
		find_longest_searcher(searchers, which_max_searcher, numberSearcher, 
							queries, which_max_query, numberQuery);
	}
public:
	void make_result(char* input)
	{
		int cases;
		int numberSearcher;
		int numberQuery;
		char buf[100];
		string* searchers;
		string* queries;
		ifstream fin;
		ofstream fout;

		fin.open(input);
		if(fin.fail())
		{
			exit(1);
		}

		fout.open("output.txt");

		fin >> cases;

		for(int i = 0;i < cases;++i)
		{
			fin >> numberSearcher;
			fin.get();
			searchers = new string[numberSearcher];
			for(int a = 0;a < numberSearcher;++a)
			{
				fin.getline(buf, 100);
				searchers[a] = buf;
			}
			
			fin >> numberQuery;
			fin.get();
			queries = new string[numberQuery];
			for(int a = 0;a < numberQuery;++a)
			{
				fin.getline(buf, 100);
				queries[a] = buf;;
			}
			minimum_case = 0;
			
			find_longest_searcher(searchers, numberSearcher, numberSearcher, 
							queries, 0, numberQuery);

			fout << "Case #" << i + 1 << ": " << minimum_case << endl;

			delete [] searchers;
			delete [] queries;
		}
		fin.close();
		fout.close();
	}
};

void main()
{
	A a;
	a.make_result("A-large.in");
}