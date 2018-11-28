#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
#include <math.h>

using namespace std;

string reverseString (string str)
{
	string tmp;
	for (int i=0; i<str.length(); i++)
		tmp.push_back(str[str.length()-1-i]);
	return tmp;
}

int getIndex (string eng, vector <string> S)
{
	for (int i=0; i<S.size(); i++)
		if (eng==S[i])
			return i;
	return -1;
}

int getSwitches (vector <string> S, vector <string> Q)
{
	if (Q.size()==0) return 0;
	int switches=0;
	string current=Q[0];
	for (int i=0; i<Q.size(); i++)
	{
		if (current==Q[i]) //time to switch
		{
			vector <int> engines;
			for (int j=0; j<S.size(); j++) engines.push_back(32767);
			
			for (int j=i+1; j<Q.size(); j++)
			{
				int dist=j-i;
				if(dist<engines[getIndex(Q[j],S)])
					engines[getIndex(Q[j],S)]=dist;
			}

			int max=0; string farthestengine="";
			for (int j=0; j<engines.size(); j++)
			{
				if(engines[j]>max && S[j] != current)
				{max=engines[j]; farthestengine=S[j];}
			}
			current=farthestengine;
//			cout<<"Switched to: "<<farthestengine<<" for query number "<<i+1<<", maxdist="<<max<<endl;
			switches++;
		}
	}
			
	return switches-1;
//	cout<<S.size()<<" "<<Q.size()<<endl;return 0;
}

int main()
{
	ifstream fin;
	fin.open ("Desktop/A-large.in");
//	FILE *fp = fopen ("Desktop/A-small.in", "r");
	ofstream fout;
	fout.open("Desktop/A-large.out");

	char abc[10];
	
	int n;
	fin>>n;
	
	
	for (int i=0; i<n; i++)
	{
		vector<string> SearchEngines, Queries;
		string tmp;

		int S;
		//fin>>S; fin.flush(); //fin>>abc; //fflush(stdin);
		fin>>S; fin.getline(abc,10);
		for (int s=0; s<S; s++)
		{
			char temp[110];
			//fgets(temp); fflush(stdin);
			fin.getline(temp, 110);
			tmp=temp;
			SearchEngines.push_back(tmp);
			//cout<<tmp<<endl;
		}
		int Q;
		fin>>Q; fin.getline(abc,10);
		for (int q=0; q<Q; q++)
		{
			char temp[110];
//			fgets(temp); fflush(stdin);
			fin.getline(temp, 110);
			tmp=temp;
			Queries.push_back(tmp);
		}
		
		fout<<"Case #"<<i+1<<": "<<getSwitches(SearchEngines, Queries)<<endl;
		cout<<"Case #"<<i+1<<": "<<getSwitches(SearchEngines, Queries)<<endl; 
	}			
	
	getchar();
}
