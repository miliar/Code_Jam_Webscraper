// Jai Mata Di
#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;
int main()
{
	ifstream ip;
	ip.open ("ip.txt");
	
	ofstream op;
	op.open ("op.txt");
	
	vector<vector<char> > mapping;

	vector<char> v;
	for(int i=0;i<26;i++)
	{
		v.push_back('.');
	}
	mapping.push_back(v);
	mapping.push_back(v);

	string G = "ejpmysljylckdkxveddknmcrejsicpdrysirbcpcypcrtcsradkhwyfrepkymveddknkmkrkcddekrkdeoyakwaejtysrreujdrlkgcjv";
	string E = "ourlanguageisimpossibletounderstandtherearetwentysixfactorialpossibilitiessoitisokayifyouwanttojustgiveup";

	for(int i=0;i<G.size();i++)
	{
		int p = G[i]-'a';
		mapping[0][p]=G[i];
		if(mapping[1][p] != '.' && mapping[1][p] != E[i])
		{
			op<<"Discrepancy!";
		}
		mapping[1][p]=E[i];
	}
	
	mapping[0]['q'-'a']='q';
	mapping[1]['q'-'a']='z';
	
	mapping[0]['z'-'a']='z';
	mapping[1]['z'-'a']='q';
	
	/*for(int i=0;i<26;i++)
	{
		cout<< mapping[0][i];
	}
	cout<<endl;
	for(int i=0;i<26;i++)
	{
		cout<< mapping[1][i];
	} */

	int noOfTestCases;
	ip>>noOfTestCases;
	getline(ip,G);
	for(int testCase=1;testCase<=noOfTestCases;testCase++)
	{
		string s;
		getline(ip,s);

		op<<"Case #"<<testCase<<": ";
		for(int i=0;i<s.size();i++)
		{	
			if(s[i] == ' ')
				op<<' ';
			else
			{
				op << mapping[1][s[i]-'a'];
			}
		}
		if(testCase != noOfTestCases)
			op<<endl;
	}
	
	ip.close();
	op.close();
}