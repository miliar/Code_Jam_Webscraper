#include <vector>
#include <fstream>
#include <iostream>
#include <string>
#include <map>

#define MAXLEN 1000

using namespace std;

typedef pair<string, unsigned int> Int_Pair;

int main (int argc, char *argv[])
{
	if (!argc) return 1;
	ifstream file(argv[1]);
	if (!file) return 2;
	unsigned int num;
	file >> num;
//	cout << num;
	unsigned int caseNum = 1;
	unsigned int s=0, q=0;
	while ( caseNum <= num )
	{
		vector<string> query;
		map<string, unsigned int> engine;
		char anEngine[MAXLEN], aQuery[MAXLEN];
		cout <<"Case #" <<caseNum <<": ";
		file >>s;
		file.get();
//		cout <<s <<endl;
		for (unsigned int i = 0; i < s; i++)
		{
			file.getline(anEngine, MAXLEN, '\n');
//			cout <<anEngine <<endl;
			engine.insert(Int_Pair(anEngine, i));
		}
		file >>q;
//		cout <<q <<endl;
		file.get();
		for (unsigned int i = 0; i < q; i++)
		{
			file.getline(aQuery, MAXLEN, '\n');
//			cout <<aQuery <<endl;
			query.push_back(aQuery);
		}
		int sw = 0;
		int searchEngine[100] = {0};
		int used = 0;
		for (unsigned int curQ =0; curQ < q; curQ++)
		{
			map <string, unsigned int> :: const_iterator iter;
			iter = engine.find(query.at(curQ));
			if (!searchEngine[iter->second])
			{
				if (used == s - 1){
					for (int t=0; t < 100; t++)	searchEngine[t]=0;
					used = 0;
					sw++;
				}
				searchEngine[iter->second] = 1;
				used++;
			}
		}
		cout <<sw <<endl;
		caseNum++;
	}
	return 0;
}