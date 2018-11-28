#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

ifstream fin("A-large.in");
ofstream fout("A-large.out");
#define cin fin
#define cout fout

struct Tdata {
	int next[26];
};

vector <Tdata> data;

int L, D, N;
int map[20][26];

void getletter(int wh)
{
	char ch;

	cin >> ch;
	while (!((ch >= 'a' && ch <= 'z') || (ch == '(') || (ch == ')'))) cin >> ch;

	if (ch == '(')
	{
		while (ch != ')')
		{
			if (ch >= 'a' && ch <= 'z') map[wh][ch - 'a'] = 1;
			cin >> ch;
		}
	} else
		map[wh][ch - 'a'] = 1;
}

void build(char *s, int now)
{
	for (int i = 0; i < L; i++)
	{
		int j = s[i] - 'a';

		if (data[now].next[j] == -1)
		{
			Tdata temp;
			for (int k = 0; k < 26; k++) temp.next[k] = -1;
			data.push_back(temp);

			data[now].next[j] = data.size()-1;
		}

		now = data[now].next[j];
	}
}

int work()
{
	vector <int> now;
	vector <int> next;

	now.clear(); now.push_back(0);
	
	for (int i = 0; i < L; i++)
	{
		next.clear();
		for (int j = 0; j < 26; j++)
			if (map[i][j] == 1)
			{
				for (int k = 0; k < now.size(); k++)
					if (data[now[k]].next[j] != -1)
						next.push_back( data[now[k]].next[j] );
			}

		now.clear();
		for (int j = 0; j < next.size(); j++)
			now.push_back(next[j]);

		if (now.size() == 0) return 0;
	}

	return now.size();
}

int main()
{
	Tdata head;
	for (int i = 0; i < 26; i++) head.next[i] = -1;

	data.clear();
	data.push_back(head);

	char s[100];
	cin >> L >> D >> N;
	for (int i = 0; i < D; i++)
	{
		cin >> s;
		build(s, 0);
	}

	for (int i = 0; i < N; i++)
	{
		memset(map, 0, sizeof(map));
		for (int j = 0; j < L; j++)
			getletter(j);

		cout << "Case #" << i+1 << ": " << work() << endl;
	}

	return 0;
}