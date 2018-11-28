#include <fstream>
#include <iostream>
#include <string>
#define _INF 10000 
#define _S 100
#define _Q 1000

using namespace std;

int main()
{
	ifstream fin("input.txt");
	ofstream fout("output.txt");
	int num_datasets;
	int dataset;
	int i, j, k;
	int n, m;
	string engine[_S];
	string query[_Q];
	int table[_Q][_S], answer;
	
	
	fin >> num_datasets;
	for(dataset = 1; dataset <= num_datasets; dataset++)
	{
		fin >> n; // number of search engines;
		for(i = 0; i < n; i++)
		{
			do
				getline(fin, engine[i]);	
			while(engine[i].length() == 0);
		}
		
		fin >> m; // number of queries;
		for(i = 0; i < m; i++)
		{
			do
				getline(fin, query[i]);
			while(query[i].length() == 0);
		}
		
		for(i = 0; i < m; i++) // query
		{
			for(j = 0; j < n; j++) // search engine
			{
				if(query[i] == engine[j])
				{
					table[i][j] = _INF;
				}
				else 
				{
					if(i == 0) 
					{
						table[i][j] = 0;
					}
					else 
					{
						table[i][j] = _INF;
						for(k = 0; k < n; k++) // previous engine
						{
							if(table[i-1][k] + (k != j) < table[i][j])
							{
								table[i][j] = table[i-1][k] + (k != j);
							}
						}	
					}					
				}
			}
		}
		if(m == 0) 
		{
			answer = 0;
		}
		else
		{
			answer = _INF;
			for(i = 0; i < n; i++)
			{
				if(table[m - 1][i] < answer)
				{
					answer = table[m-1][i];
				}
			}
		}
		
		fout << "Case #" << dataset << ": " << answer << endl;
	}
	fin.close();
	fout.close();
	return 0;
}

