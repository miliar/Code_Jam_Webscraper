#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
#include<cmath>

using namespace std;

class SavingTheUniverse
{
public:
	int minSwitches(int numEngines, vector<int> queries)
	{
		if(queries.size() == 0)
		{
			return 0;
		}

		int memo[1001][101];

		memset(memo, 0, sizeof(int)*1001*101);

		for(int i=0;i<(int)queries.size();i++)
		{
			for(int j=0;j<numEngines;j++)
			{
				if(j == queries[i])
				{
					memo[i][j] = 1000;
				}
				else if(i==0)
				{
					memo[i][j] = 0;
				}
				else
				{
					int minOther = 1000;
					for(int k=0;k<numEngines;k++)
					{
						if(k != j && minOther > memo[i-1][k])
						{
							minOther = memo[i-1][k];
						}
					}

					//cout<<"min("<<memo[i-1][j]<<","<<minOther + 1<<") = ";
					memo[i][j] = min(memo[i-1][j], minOther + 1);
					//cout<<memo[i][j]<<endl;
				}
			}
		}

		int minSwitch = 1000;
		for(int j=0;j<numEngines;j++)
			if(minSwitch > memo[queries.size()-1][j])
				minSwitch = memo[queries.size()-1][j];

		return minSwitch;
	}
};

int main()
{
	SavingTheUniverse stu;
	char line[1000];	
	int n;

	cin.getline(line, 1000);
	istringstream iss(line);
	iss>>n;

	//cout<<"N = "<<n<<endl;
	
	for(int i=0;i<n;i++)
	{
		int numEngines, numQueries;
		int engineNumber = 0;
		string engine, query;
		
		map<string, int> engineToNumberMap;
		vector<int> queries;

		cin.getline(line, 1000);
		istringstream iss2(line);
		iss2>>numEngines;
		//cout<<"# engines = "<<numEngines<<endl;

		for(int j=0;j<numEngines;j++)
		{
			cin.getline(line, 1000);
			engine = string(line);
			//cout<<"engine #"<<j<<" = "<<engine<<endl;
			engineToNumberMap[engine] = engineNumber++;
		}

		cin.getline(line, 1000);
		istringstream iss3 = istringstream(line);
		iss3>>numQueries;
		//cout<<"# queries = "<<numQueries<<endl;

		for(int j=0;j<numQueries;j++)
		{
			cin.getline(line, 1000);
			query = string(line);
			//cout<<"query #"<<j<<" = "<<engineToNumberMap[query]<<endl;
			queries.push_back(engineToNumberMap[query]);
		}

		cout<<"Case #"<<i+1<<": "<<stu.minSwitches(engineNumber, queries)<<endl;
	}
}