#include<iostream>
#include<fstream>
#include<algorithm>
#include<iomanip>
#include<cmath>
#include<set>
#include<string>
using namespace std;
ifstream in("A-large.in");
ofstream out("res.txt");

set<string> S;
int T, N, M;
int res;

void input()
{
	S.clear();
	int i;
	string dir;
	for(i = 0; i < N; i++)
	{
		in>>dir;
		S.insert(dir);
	}
}

int solve()
{
	res = 0;
	int i;
	string dir;
	for(i = 0; i < M; i++)
	{
		in>>dir;
		string tmp;
		int j;
		for(j = 1; j < dir.size(); j++)
		{
			if(dir[j] == '/')
			{
				int k;
				char str[101];
				for(k = 0; k < j; k++)
					str[k] = dir[k];
				str[k] = '\0';
				if(S.find(string(str)) == S.end())
				{
					S.insert(string(str));
					res++;
				}
			}
		}
		if(S.find(dir) == S.end())
		{
			S.insert(dir);
			res++;
		}
	}
	return res;
}

int main()
{
	while(in>>T)
	{
		int count;
		for(count = 1; count <= T; count++)
		{
			in>>N>>M;
			input();
			out<<"Case #"<<count<<": "<<solve()<<endl;
		}
	}
	return 0;
}
