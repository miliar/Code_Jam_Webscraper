#include <iostream>
using namespace std;
#include <fstream>
#include <string>
#include <vector>
#include <map>

int numFound;

void LoadStrings(vector<string> &tbl){
	ifstream fin("C-small-attempt0.in");
	string temp;
	getline(fin, temp, '\n');
	int t = atoi(temp.c_str());
	for(int i=0;i<t;++i)
	{
		getline(fin, temp, '\n');
		tbl.push_back(temp);
	}
}

void searchForString(string target,string searchArea)
{
	for(unsigned int i=0;i<searchArea.size();++i)
	{
		if(target[0] == searchArea[i])
		{
			if(target.size()==1)numFound++;
			else searchForString(target.substr(1),searchArea.substr(i));
		}
	}
	
}

int main(void)
{

	numFound=0;
	vector<string> strings;
	LoadStrings(strings);
	string target="welcome to code jam";

	ofstream fout("C-small-attempt0.out");
	for(unsigned int i=0;i<strings.size();++i)
	{
		searchForString(target,strings[i]);
		char out[20];
		sprintf_s (out, "Case #%d: %04d\n", i+1, numFound);
		fout << out;
		numFound=0;

	}
	
	return 0;
}
