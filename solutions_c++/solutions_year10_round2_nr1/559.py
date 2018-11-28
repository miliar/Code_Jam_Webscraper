#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<set>
#include<algorithm>

using namespace std;
int N,M;
set<string> Str;
int Result = 0;

void init(string str)
{
	vector<string> s;
	string t;
	string::size_type last = 0;
	for(string::size_type i = 1; i < str.length() + 1; i++)
	{
		if(i == str.length() || str[i] == '/')
		{
			t = str.substr(last,i - last);
			s.push_back(t);
		}
		else
		{
			continue;
		}
	}
	for(vector<string>::size_type i = 0;  i < s.size(); i++)
	{
		if(!Str.count(s[i]))
			Str.insert(s[i]);
	}
}
void solve(string str)
{
	vector<string> s;
	string t;
	string::size_type last = 0;
	for(string::size_type i = 1; i < str.length() + 1; i++)
	{
		if(i == str.length() || str[i] == '/')
		{
			t = str.substr(last,i - last);
			s.push_back(t);
		}
		else
		{
			continue;
		}
	}
	for(vector<string>::size_type i = 0;  i < s.size(); i++)
	{
		if(!Str.count(s[i]))
		{
			Str.insert(s[i]);
			Result++;
		}
	}
}
int main()
{
	ifstream input("A-large.in");
	ofstream out("test.out");
	int T;
	input >> T;
	string str;
	for(int i = 1; i <= T; i++)
	{
		input >> N >> M;
		Str.clear();
		for(int j = 0; j < N; j++)
		{
			input >> str;
			init(str);
		}
		Result = 0;
		for(int j = 0; j < M; j++)
		{
			input >> str;
			solve(str);
		}
		out << "Case #" << i << ": " << Result << endl;
	}
	return 0;
}