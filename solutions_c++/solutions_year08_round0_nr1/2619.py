#include <stdio.h>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <deque>

using namespace std;
int main()
{

	typedef struct search_Engine
	{
		string engineName;
		bool alreadyAppeared;
	} SearchEngine;

	unsigned int numberOfCase = 0;
	string temp;
	
	ifstream inFile;
	ofstream outFile;
	inFile.open ("A-large.in");
	outFile.open ("output.txt");
	
	if (inFile.is_open()&&outFile.is_open())
	{ 
		getline (inFile,temp);
		numberOfCase = atoi(temp.c_str());
		for(unsigned int i=1;i<=numberOfCase;++i)
		{
			vector<SearchEngine> searchEngines;
			deque<string> queries;
			SearchEngine searchEngine;
			string query;
			
			bool nameMatched = false;
			unsigned int numberOfSearchEngine = 0;
			unsigned int numberOfQuery = 0 ;
			unsigned int numberOfSwitch = 0;
			getline(inFile,temp);
			numberOfSearchEngine = atoi(temp.c_str());
			for(unsigned int j=0;j<numberOfSearchEngine;++j)
			{
				getline(inFile,searchEngine.engineName);
				searchEngine.alreadyAppeared = false;
				searchEngines.push_back(searchEngine);
			}
			getline(inFile,temp);
			numberOfQuery = atoi(temp.c_str());
			for(unsigned int k=0;k<numberOfQuery;++k)
			{
				getline(inFile,query);
				queries.push_back(query);
			}

			for(unsigned int t=0;t<numberOfSearchEngine;++t)
			{
				nameMatched = false;
				for(unsigned int j=0;j<numberOfQuery;++j)
				{
					if(!searchEngines[t].engineName.compare(queries[j]))
					{
						nameMatched =true;
						break;
					}
				}
				if(!nameMatched)
				{
					break;
				}
					
			}

			if(!nameMatched)
			{
				numberOfSwitch=0;
			}
			else
			{
				unsigned int count=0;
				string currentQuery;
				while(!queries.empty())
				{
					currentQuery = queries.front();
					queries.pop_front();
					for(unsigned int s=0;s<numberOfSearchEngine;++s)
					{
						if(!currentQuery.compare(searchEngines[s].engineName))
						{
							if(!searchEngines[s].alreadyAppeared)
							{
								++count;
							}
							searchEngines[s].alreadyAppeared = true;
						}
					}
					if(count==numberOfSearchEngine)
					{
						++numberOfSwitch;
						count=0;
						for(unsigned int y=0;y<numberOfSearchEngine;++y)
						{
							searchEngines[y].alreadyAppeared = false;
						}

						for(unsigned int s=0;s<numberOfSearchEngine;++s)
						{
							if(!currentQuery.compare(searchEngines[s].engineName))
							{
								if(!searchEngines[s].alreadyAppeared)
								{
									++count;
								}
								searchEngines[s].alreadyAppeared = true;
							}
						}


					}
				}
				
			}
			if(!searchEngines.empty())
			{
				searchEngines.clear();
			}
			
			outFile<<"Case #"<<i<<": "<<numberOfSwitch<<endl;
		}				     
	}
    inFile.close();
	outFile.close();
	return true;

}