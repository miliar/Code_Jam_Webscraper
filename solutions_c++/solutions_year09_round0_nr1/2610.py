/*
Language:C++
*/

#include<string>
#include<sstream>
#include<fstream>
#include<vector>
#include<iostream>

using namespace std;

vector<string> StrSplit(const string &str)
{
	vector<string> result;
	string temp;
	unsigned int i=0,j=0;

	while(i<str.length())
	{
		temp="";
		if(str[i]=='(')
		{
			j=i+1;
			while( j<str.length() && str[j]!=')') //split words.
			{
				temp=temp+str[j];
				j++;
			}

			result.push_back(temp);
			i=j;
		}else{
			temp+=str[i];
			result.push_back(temp);
		}
		i++;
	}
	return result;
}

int main()
{
	ofstream fout("A-small.out");
	ifstream fin("A-small-attempt0.in");

	int l,d,n;
	fin>>l>>d>>n;
	
	vector<string> v;

	for(int i=0;i!=d;i++)
	{
		string word;
		fin>>word;

		v.push_back(word);
	}
	
	for(int i=0;i!=n;i++)
	{
		string line;
		fin>>line;
		
		vector<string> split=StrSplit(line);
		vector<string> cp=v;

		for(int j=0;j!=split.size();j++)
		{
			string s=split[j];

			for(int l=0;l!=cp.size();l++)
			{
				bool test=false;
				for(int k=0;k!=s.length();k++)
				{
					if(cp[l][j]==s[k])
					{
						test=true;
						break;
					}
				}
				
				if(!test)
				{
					cp.erase(cp.begin()+l);
					l--;
				}
			}
		}
		
		fout<<"Case #"<<i+1<<": "<<cp.size()<<endl;
	}

	return 0;
}