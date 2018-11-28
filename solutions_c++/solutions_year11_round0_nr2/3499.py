#include <iostream>
#include <string>
#include <math.h>
using namespace std;

#define pb push_back
char abc[26]={'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'};

int hanyadikbetu(char betu)
	{
	for (int i=0;i<26;i++)
		if (abc[i]==betu)
			return i;
	}
int main()
	{
	freopen("be.txt", "rt", stdin);
	freopen("ki.txt", "wt", stdout);
	
	int testcases,t,match,opp;
	string temp,szo;
	cin >> testcases;
	t=testcases;
	while (t--)
		{
		char matchtable[26][26];
		string output;
		for (int i=0;i<26;i++)
			for (int j=0;j<26;j++)
				matchtable[i][j]=0;
				
		int opptable[26][26];
		for (int i=0;i<26;i++)
			for (int j=0;j<26;j++)
				opptable[i][j]=0;
		
		
		cin >> match;
		while (match--)
			{
			cin >>temp;
			matchtable[hanyadikbetu(temp[0])][hanyadikbetu(temp[1])]=temp[2];
			matchtable[hanyadikbetu(temp[1])][hanyadikbetu(temp[0])]=temp[2];
			}
		cin >> opp;
		while (opp--)
			{
			cin >>temp;
			opptable[hanyadikbetu(temp[0])][hanyadikbetu(temp[1])]=-1;
			opptable[hanyadikbetu(temp[1])][hanyadikbetu(temp[0])]=-1;
			}
		cin >> temp;
		cin >> szo;

		for (int i=0;i<szo.size();i++)
			{
			bool flag=false;
			if (output.size()==0)
				{
				output.pb(szo[i]);
				continue;
				}
			if (matchtable[hanyadikbetu(szo[i])][hanyadikbetu(output[output.size()-1])]!=0)
				{		
				output[output.size()-1]=matchtable[hanyadikbetu(szo[i])][hanyadikbetu(output[output.size()-1])];
				continue;
				}
			for (int j=0;j<output.size();j++)
				{
				if (opptable[hanyadikbetu(szo[i])][hanyadikbetu(output[j])]==-1)
					{
					flag=true;
					output.clear();
					break;
					}
				}
			if (!flag)
				output.pb(szo[i]);			
			}
		cout << "Case #"<<testcases-t<<": [";
		if (output.size()!=0)
			{
			for (int i=0;i<output.size()-1;i++)
				cout << output[i]<<", ";
				
				cout <<output[output.size()-1];
			}
		cout << "]"<<endl;
		}
	}
