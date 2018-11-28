#include <iostream>
#include <string>
#include <algorithm>
#include <map>

using namespace std;

map <string, int> name2id;
int m[1010][110];
int N, S, Q;

int run()
{
	string name;
	cin >> S;
	getline(cin, name);
	for(int i = 0; i < S; i ++)
	{
		getline(cin, name);
		name2id[name] = i;
		m[0][i] = 0;
	}
	cin >> Q;
	int small;
	getline(cin, name);
	for(int i = 1; i <= Q; i ++)
	{
		getline(cin, name);
		int t = name2id[name];
		if(t == 0) small = m[i-1][1];
		else small = m[i-1][0];
		for(int j = 1; j < S; j ++)
		{
			if(j == t) continue;
			small = min(small, m[i-1][j]);
		}
		for(int j = 0; j < S; j ++)
		{
			if(j == t)
			{
				m[i][j] = small + 1;
			}
			else
			{
				m[i][j] = m[i-1][j];
			}
		}
	}
	small = m[Q][0];
		for(int j = 1; j < S; j ++)
		{
			small = min(small, m[Q][j]);
		}
	return small;
}

int main()
{
	cin >> N;
	for(int i = 1; i <= N; i ++)
	{
		name2id.clear();
		cout << "Case #" << i << ": " << run() << endl;
	}
}
