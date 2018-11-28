#include <fstream>
#include <iostream>
#include <sstream>
#include <math.h>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
using namespace std;

vector<string> engines;
vector<string> queries;

int displacement(int cmp, string avoid)
{
		int size = static_cast<int>(engines.size());
		int sizeQueries = static_cast<int>(queries.size());

		int max = cmp;
		
		for (int ii = 0; ii < size; ii++)
		{
			string val = engines.at(ii);
			if (val != avoid)
			{
				bool bFound = false;
				int jj = cmp + 1;
				while (jj < sizeQueries && !bFound)
				{
					if (queries.at(jj) == val)
					{ 
						bFound = true;
						break;
					}
					jj++;
				}
				if (bFound)
				{
					if (max < jj)
						max = jj;
				}
				else 
				{
					max = sizeQueries;
					return max;
				}
			}
		}
		return max;
}

int main()
{
    ifstream file("C:\\Benoit\\code jam\\Universe\\A-large.in");
		ofstream fileOut("C:\\Benoit\\code jam\\Universe\\A-large.out");
		string line;
		
		getline(file, line);
    int N = atoi(line.c_str());
    

    vector<string>::iterator it_engines;
		engines.reserve(100);    

    vector<string>::iterator it_queries;
		queries.reserve(1000);
			
    int results = -1;
    
    for (int ii = 1 ; ii <= N ; ii++)
		{
					getline(file, line);
			    int S = atoi(line.c_str());
				
					engines.clear();
					for (int jj = 1; jj <= S ; jj++)
					{
						getline(file, line);	
						engines.push_back(line);
					}

					getline(file, line);
			    int Q = atoi(line.c_str());	
					string slast("");
					queries.clear();
					
					for (int zz = 1; zz <= Q ; zz++)
					{
						getline(file, line);	
						queries.push_back(line);
					}

					int queriesSize = static_cast<int>(queries.size());
					int cmp = 0;
					results = -1;
					
					while (cmp <  queriesSize)
					{
						int disp = 0;
						cmp = displacement(cmp, queries.at(cmp));
						results++; 
					}
					if (results == -1) results = 0;
					fileOut << "Case #" << ii << ": " << results;
					fileOut << "\n";
		  }
		  
		  file.close();
		  fileOut.close();
      return 0;
}