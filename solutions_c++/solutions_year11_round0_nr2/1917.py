#include<iostream>
#include<vector>
#include<string>
using namespace std;

int ntests;

int n,d,c;
vector<string> combine,oppose;
string is;

string combines(char c1, char c2)
{
	for(int i=0;i<combine.size();i++)
	{
		if((combine[i][0]==c1 && combine[i][1]==c2) || (combine[i][0]==c2 && combine[i][1]==c1))
		{
			string ret = combine[i].substr(2,1);
			return ret;
		}
	}
	return "";
}

int opposes(string output)
{
	string refs = output;
	for(int j=0;j<oppose.size();j++)
	{
		if(refs.find_first_of(oppose[j][0]) != string::npos && refs.find_first_of(oppose[j][1]) != string::npos)
			return 1;
	}
	return 0;
}

int main()
{
	cin>>ntests;
	for(int ii=0;ii<ntests;ii++)
	{
		cin>>c;
		combine.clear();
		oppose.clear();
		for(int i=0;i<c;i++)
		{
			char str[200];
			cin>>str;
			string ss=str;
			combine.push_back(ss);
		}
		cin>>d;
		for(int i=0;i<d;i++)
		{
			char str[200];
			cin>>str;
			string ss=str;
			oppose.push_back(ss);
		}
		cin>>n;
		char str[200];
		cin>>str;
		is = str;
		string output;
		
		for(int i=0;i<is.size();i++)
		{
			if(output == "")
			{
				output = is.substr(i,1);
				continue;
			}
			string cs = combines(is[i],output[output.size()-1]);
			if(cs != "")
			{
				output[output.size()-1] = cs[0];
			}
			else if(opposes(output+is[i]))
			{
				output="";
			}
			else output = output + is[i];
		}		
		cout<<"Case #"<<ii+1<<": [";
		if(output.size()==0)
		{
			cout<<"]"<<endl;
			continue;
		}
			
		int o;
		for(o=0;o<output.size()-1;o++)
		{
			cout<<output[o]<<", ";
		}
		cout<<output[o]<<"]"<<endl;
			
	}
	return 0;
}