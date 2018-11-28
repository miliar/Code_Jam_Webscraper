#include <iostream>
#include <fstream>
#include <vector>
#include <map>
#include <string>

using namespace std;

int MAX_L;
vector<int> query;
int eng_num;
vector<int> there;

int main()
{
ifstream myfile ("data.dat");

int cases;
int q_num;

map<string,int> engines;

string label;

getline(myfile,label);
cases=atoi(label.data());

for(int i=0; i<cases; i++)
	{
	MAX_L=10000000;
	int swit=0;
	query.resize(0);
	engines.clear();

	getline(myfile,label);
	eng_num=atoi(label.data());


	for(int e=0; e<eng_num; e++)
		{
		getline(myfile,label) ;
		engines[label]=e;
		}
	there.resize(engines.size());

	for(int j=0; j<engines.size(); j++)
		there[j]=0;
	

	getline(myfile,label);

	q_num=atoi(label.data());

	for(int q=0; q<q_num; q++)
		{
		getline(myfile,label);
		query.push_back(engines[label]);

		there[engines[label]]=1;
		
		int nb=1;
		for(int j=0; j<engines.size(); j++)
			if(there[j]==0)
				nb=0;

		if(nb==1)
			{
			swit++;
			for(int j=0; j<engines.size(); j++)
				there[j]=0;
			there[engines[label]]=1;
			}
		}
	cout << "Case #"<<i+1<<": "<< swit << endl;
	}

return 0;
}
