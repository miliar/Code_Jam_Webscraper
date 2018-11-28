// saving the universe

#include <iostream>
#include <vector>
#include <cstring>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <sstream>

using namespace std;

vector <string> engines;
vector <string> queries;
int factor = 1000;

void print()
{
	for(vector<string> :: iterator it = engines.begin(); it != engines.end(); it++)
		cout << setw(2) << *it << endl;

	//cout << " queries " << endl;
	
	//for(vector<string> :: iterator l = queries.begin(); l != queries.end(); l++)
		//cout << setw(2) << *l << endl;

}
void read()
{
	int num_engines;
	string engine;
	string query;
	int num_query;
	
	engines.clear();
	queries.clear();
	cin >> num_engines;
	
	//cout << " engines " << num_engines << endl;
	getline(cin,engine);
	for(int k = 1; k <= num_engines; k++)
	{
		//istringstream ss(engine);
		getline(cin,engine);
		//cout << "e = " << engine << endl;
		engines.push_back(engine);
	}
	
	cin >> num_query;
	//cout << " num q" << num_query << endl;
	//cout << " query " << num_query << endl;
	getline(cin,query);
	for(int k = 1; k <= num_query; k++)
	{
		//istringstream ss1(query);
		getline(cin,query );
		//cout << "q = " << query << endl;
		queries.push_back(query);
	}
	return;
}

int newlook(int a, string eng)
{
	int newloc = a;

	//cout << " eng " << eng << endl;
	while( (newloc < queries.size()) && (queries[newloc] != eng) )
	{	
		newloc++;
	}
	//cout << " <-newloc " << newloc << endl;
	return newloc;
}
void solution(int i, int loc)
{
	int newloc;
	int best = 0;
	int bestk;
		
	//cout << "solution(" << i << "," << loc << ")" << endl;	
	// do the dfs
		for(int k = 0; k < engines.size(); k++)
		{
			//cout << " k option = " << k << " . " << engines[k] << endl;
			if (engines[k] != queries[loc] ){
				//cout << " oh nooo " << endl;
				newloc = newlook(loc, engines[k]);
				//cout << " oh noo " << newloc << endl;
				if(newloc == queries.size() )
				{	factor = i; 
					return; 
				}
				else{
					if(newloc > best){
						best = newloc;
						bestk = k;
					}
				}
			}
		} // for
		solution(i+1,best);
}
void process()
{
	int test;
	cin >> test;
	//cout << " hello " << endl;
	for(int k = 1; k <= test; k++)
	{
		read();
		if(queries.size() == 0)
		{
			cout << "Case #"<< k <<": 0" << endl;
			
		}
		else {
			//factor = 1000;
			solution(0,0);
			cout << "Case #"<< k <<": "<< factor << endl;
		}
	}

}

int main()
{
	

	process();

	return 0;

}

