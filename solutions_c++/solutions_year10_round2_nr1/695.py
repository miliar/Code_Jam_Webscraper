#include <iostream>
#include <set>
#include <string>
#include <cstdlib>

using namespace std;

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T;
	cin >> T;

for ( int t = 1; t <= T; t++)
{
	int N, M;
	cin >> N >> M;
	string s, l;
	set<string> now;
	for ( int i = 0; i < N; i++)
	{
		cin >> s;
		l.clear();
		unsigned int j = 0;
		while ( j < s.size())
		{
			l += s[j];
			j++;
			while ( j < s.size() && s[j] != '/')
			{
				l += s[j];
				j++;
			}
			now.insert(l);
		}
	}

	int mk_dir = 0;
	for ( int i = 0; i < M; i++) 
	{
		cin >> s;
		l.clear();
		unsigned int j = 0;
		while ( j < s.size())
		{
			l += s[j];
			j++;
			while (j < s.size() && s[j] != '/')
			{
				l += s[j];
				j++;
			}

			if ( now.find(l) == now.end())
			{
				now.insert(l);
				mk_dir++;
			}
		}
	}
	cout << "Case #" << t << ": " << mk_dir << endl;
}
}