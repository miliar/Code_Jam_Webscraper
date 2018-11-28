#include<iostream>
#include<fstream>
#include<algorithm>
#include<iomanip>
#include<cmath>
#include<set>
#include<string>
using namespace std;
//ifstream in("B.in");
ifstream in("B-large.in");
ofstream out("res.txt");

int C, N, K, B, T;
int xi[51];
int vi[51];
void input()
{
	int i;
	for(i = 0; i < N; i++)
	//	cin>>xi[i];
		in>>xi[i];
	for(i = 0; i < N; i++)
	//	cin>>vi[i];
		in>>vi[i];
}

int solve()
{
	int res = 0;
	int num = 0;
	int prenot = 0;
	int i;
	for(i = N-1; i >= 0; i--)
	{
		if(num == K)
			break;
		if(B-xi[i] <= T * vi[i])
		{
			num++;
			res += prenot;
		}
		else
			prenot++;
	}
	if(num == K)
		return res;
	else
		return -1;
}

int main()
{
	while(in>>C)
	{
		int count;
		for(count = 1; count <= C; count++)
		{
			in>>N>>K>>B>>T;
			input();
			int res = solve();
			if(res != -1)
				out<<"Case #"<<count<<": "<<res<<endl;
			else
				out<<"Case #"<<count<<": "<<"IMPOSSIBLE"<<endl;
		}
	}
	return 0;
}





/*
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
*/