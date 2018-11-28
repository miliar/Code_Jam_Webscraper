#include<iostream>
#include<fstream>
#include<vector>
#include<string>
using namespace std;
vector<string> dict;
int validate(string s, int start, string ss, int depth)
{
	if(start>=s.length())
	{
		for(int i = 0; i<dict.size();i++)
		{
			if(ss == dict[i])
				return 1;
		}
		return 0;
	}
	else
	{
		bool found = false;
		for(int i=0; i<dict.size();i++)
		{
			if(ss == dict[i].substr(0,ss.length()))
				found = true;
		}
		if(!found) return 0;
	}
	if(s[start]=='(')
	{
		int next,i=start+1;
		while(true)
		{
			if(s[i]==')')
			{
				next = i;
				break;
			}
			i++;
		}
		int sum = 0;
		for(int i=start+1;i<next;i++)
		{
			sum += validate(s,next+1,ss+s[i],depth+1);
		}
		return sum;
	}
	else
	{
		return validate(s,start+1,ss+s[start],depth+1);
	}
}
int main()
{
	ifstream fin("A-small-attempt1.in");
	ofstream fout("output");
	int l,d,n;
	fin>>l>>d>>n;
	for(int i=0;i<d;i++)
	{
		string s;
		fin>>s;
		dict.push_back(s);
	}
	for(int i=1;i<=n;i++)
	{
		string s;
		fin>>s;
		fout<<"Case #"<<i<<": "<<validate(s,0,"",0)<<endl;
	}
	return 0;
}