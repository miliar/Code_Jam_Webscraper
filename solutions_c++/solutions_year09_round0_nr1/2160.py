#include<iostream>
#include<vector>
#include<map>
#include<string>
using namespace std;

bool my_find(char a,string& b)
{
	bool found=false;
	for(int i=0;i<b.size();i++)
		found=(found | a==b[i]);
	return found;
}
int answers(vector<string>&,string&);
int main()
{
	int L,N,D,X=1;
	cin>>L>>D>>N;
	
	vector<string> words;
	string input;
	getchar();
	for(int i=0;i<D;i++)
	{
		getline(cin,input);
		words.push_back(input);
	}
	vector<string> testers;
	for(int i=0;i<N;i++)
	{
		getline(cin,input);
		cout<<"Case #"<<X<<": "<<answers(words,input)<<endl;
		X++;
	}
	return 0;
}

int answers(vector<string>&words,string&tester)
{
	vector<bool> ans(words.size(),true);
	bool open=false;
	int loc=0;
	string hold="";
	for(int i=0;i<tester.size();i++)
	{			
		if(tester[i] == '(' )
		{
			open=true;
			continue;
		}
		else if(tester[i] == ')')
		{
			open=false;
		}
		else
		{
			hold.push_back(tester[i]);
		}
		if(!open)
		{
			for(int j=0;j<words.size();j++)
			{
				if(!ans[j])
					continue;
				else
					ans[j]=my_find(words[j][loc],hold);
			}
			loc++;
			hold="";
		}
	}
	int count=0;
	for(int i=0;i<ans.size();i++)
		if(ans[i])
			count++;
	return count;
}
