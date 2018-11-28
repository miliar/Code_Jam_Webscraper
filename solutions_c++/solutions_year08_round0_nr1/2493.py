#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

long performCase()
{
	int engineCount;
	cin>>engineCount;
	map<string, bool> engines;
	string dump;
	getline(cin, dump);
	for(int i=0; i<engineCount; i++)
	{
		string engineName;
		getline(cin, engineName);
		engines[engineName] = false;
	}
	int searchCount;
	cin>>searchCount;
	getline(cin, dump);
	vector<string> searchTerms;
	for(int i=0; i<searchCount; i++)
	{
		string engineName;
		getline(cin, engineName);
		searchTerms.push_back(engineName);
	}

	int badCount=0;
	long switchCount = 0;
	for(int i=0; i<searchCount; i++)
	{
		if(!engines[searchTerms[i]])
		{
			engines[searchTerms[i]] = true;
			badCount++;
		}
		if(badCount == engineCount)
		{
			badCount=0;
			switchCount++;
			i--;
			for(map<string, bool>::iterator iter=engines.begin(); iter != engines.end(); iter++)
				(*iter).second = false;
		}
	}
	return switchCount;
}

void main()
{
	int testcasecount;
	cin>>testcasecount;
	vector<long> result;
	for(int i=0; i<testcasecount; i++)
		result.push_back(performCase());
	cout<<"\n\nresults follow\n\n";
	for(int i=0; i<testcasecount; i++)
		cout<<"Case #"<<(i+1)<<": "<<result[i]<<endl;
}
