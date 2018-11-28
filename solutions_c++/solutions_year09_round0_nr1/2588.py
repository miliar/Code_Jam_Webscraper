//////////////////////////////////////////////////////////////////////////
// Correct for small and large testsets
//////////////////////////////////////////////////////////////////////////
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <fstream>
using namespace std;



int main()
{
	ifstream cin("A-large.in");
	ofstream out("output.txt");
	
	int L,D,N;
	vector<string> dictionary;
	cin>>L>>D>>N;
	string word;
	for(int i=1; i<=D; i++)
	{
		cin>>word;
		dictionary.push_back(word);
	}
	string text;
	for(int i=1; i<=N; i++)
	{
		vector<string> pattern;
		cin>>text;
		string s="";
		bool inter = false;
		for(int j=0; j<text.length(); j++)
		{
			if(text[j] == '(')
			{
				inter = true;
				continue;
			}
			else if(text[j] == ')')
			{
				pattern.push_back(s);
				s="";
				inter = false;
			}
			else
			{
				if(inter)
					s += text[j];
				else
				{
					s = text[j];
					pattern.push_back(s);
				}
			}
		}
		//judge
		int sum = 0;
		for(int j=0; j<D; j++)
		{
			string word = dictionary[j];
			bool flag = true;
			for(int k=0; k<L; k++)
			{
				if( pattern[k].find(word[k]) == -1 )
				{
					flag = false;
					break;
				}
			}
			if(flag)
				sum++;
		}
		out<<"Case #"<<i<<": "<<sum<<endl;
	}

	return 0;
}