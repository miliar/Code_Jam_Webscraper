#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

struct info{
	string name;
	vector<int> occurences;
};

void getParameters(ifstream &inFile, vector<info>& servers, vector<string>& queries)
{
	int serverC, queryC;
	char tmp[100];
	inFile>>serverC;
	inFile.getline(tmp,100);

	for(int i=0; i<serverC; i++)
	{
		info temp;
		inFile.getline(tmp,100);
		temp.name = tmp;
		servers.push_back(temp);
	}

	inFile>>queryC;
	inFile.getline(tmp,100);

	for(int i=0; i<queryC; i++)
	{
		string temp;
		inFile.getline(tmp,100);
		temp = tmp;
		queries.push_back(temp);
	}
}

int findFirst(string server, vector<string>& queries)
{
	for(int i=0; i<queries.size(); i++)
	{
		if(strcmp(queries[i].c_str(),server.c_str())==0)
			return i;
	}

	return -2;
}

int findFurthest(vector<info>& servers, vector<string>& queries)
{
	int furthest = 0;
	int index = -1;

	for(int i=0; i<servers.size(); i++)
	{
		int temp = findFirst(servers[i].name,queries);
		
		if(temp==-2)
			return i;

		if(temp>furthest)
		{
			furthest=temp;
			index = i;
		}
	}

	return index;
}

bool executeQueries(int currentS, vector<info>& servers, vector<string>& queries)
{
	string currSname = servers[currentS].name;

	for(int i=0; queries.size()>0;)
	{	
		if(strcmp(queries[i].c_str(),servers[currentS].name.c_str())!=0)
			queries.erase(queries.begin());
		else
			return true;
	}

	return false;
}

int main()
{
	vector<string> queries;
	vector<info> servers;

	int cases;
	int switches = -1;
	int currentS = -1;
	int next = -1;
	char name[100];

	string ifname, ofname;

	cout<<"Name of the input file (without '.in' e.g. 'A-small' ) : ";
	cin.getline(name,100);
	
	ifname.assign(name);
	ofname.assign(name);

	ifname+= ".in";
	ofname+= ".out";

	ifstream inFile(ifname.c_str());
	ofstream outFile(ofname.c_str());

	if(!inFile.is_open())
	{
		cout<<"Wrong input file";
		return 0;
	}

	inFile>>cases;

	for(int i=0; i<cases; i++)
	{
		getParameters(inFile,servers,queries);
		
		do{
			switches++;
			next = findFurthest(servers,queries);
			if(next==-1) break;
		}while(executeQueries(next,servers,queries));

		cout<<"Case #"<<i+1<<": "<<switches<<endl;
		outFile<<"Case #"<<i+1<<": "<<switches<<endl;

		switches=-1;
		servers.clear();
		queries.clear();
		currentS = -1;
	}

	return 0;
}