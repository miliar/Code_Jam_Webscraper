#include <iostream>
#include <iomanip>
#include <fstream>
#include <cmath>
#include <list>
#include <utility>
#include <string>
#include <vector>
#include <map>
#include <boost/lexical_cast.hpp>

using namespace std;

int N;

struct Case{
	vector<string> server;
	vector<string> query;
};

vector<Case> cases;

int searchNextServer(const Case& ca, int start)
{
	map<string, int> count;
	int S = ca.server.size(); // the number of 0

	for(int i=0; i<ca.server.size(); i++)count[ca.server[i]] = 0;

	for(int i=start; i<ca.query.size(); i++)
	{
		if(count[ca.query[i]] == 0)S--;
		if(S == 0)return i;
		count[ca.query[i]]++;
	}

	return ca.query.size();
}

int main(int argc, char **argv){
	string buff;
	ifstream ifs(argv[1]);
	
	getline(ifs, buff);
	N = boost::lexical_cast<int>(buff);
	cases.resize(N);

	for(int n=0; n<N; n++)
	{
		getline(ifs, buff);
		int S = boost::lexical_cast<int>(buff);
		cases[n].server.resize(S);
		for(int s=0; s<S; s++)
		{
			getline(ifs, buff);
			cases[n].server[s] = buff;
		}

		getline(ifs, buff);
		int Q = boost::lexical_cast<int>(buff);
		cases[n].query.resize(Q);
		for(int q=0; q<Q; q++)
		{
			getline(ifs, buff);
			cases[n].query[q] = buff;
		}
	}		

	// START
	for(int n=0; n<N; n++)
	{
		int count=0;
		int Q = cases[n].query.size();
		for(int i=0; i<Q; )
		{
		 	i = searchNextServer(cases[n], i);
		 	if(i<Q)
		 	{
				//cout << "start:" << cases[n].query[i];
				count++;
			}
		}
		cout << "Case #" << n+1 << ": " << count << endl;
	}

	return 0;
}
