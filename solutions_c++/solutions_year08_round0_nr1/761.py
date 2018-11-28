#include <iostream>
#include <string>
using namespace std;

#define INPUTFILENAME "A-large.in.txt"
#define OUTPUTFILENAME "output.txt"

const int MAXS = 100;

class Object
{
public:
	string name;
	int hashvalue;

	void init(string &st)
	{
		name = st;
		hashvalue = (int)st.size() * 10000000;
		for (int i = 0; i < st.size(); i++)
			hashvalue += (i + 1) * st[i];
	}

	int same(Object x)
	{
		if (x.hashvalue != hashvalue)
			return 0;
		for (int i = 0; i < name.size(); i++)
			if (name[i] != x.name[i])
				return 0;
		return 1;
	}

} engine[MAXS], query;

int s, q;

void init()
{
	string st;
	cin >> s;
	getline(cin, st);
	for (int i = 0; i < s; i++)	
	{
		getline(cin, st);
		engine[i].init(st);
	}
}

void solve(int testnumber)
{
	string st;
	cin >> q;
	getline(cin, st);

	int ans = 0;
	int count = 0;
	int mark[MAXS];
	memset(mark, 0, sizeof(mark));

	for (int i = 0; i < q; i++)	
	{
		getline(cin, st);
		query.init(st);
		for (int j = 0; j < s; j++)
			if (mark[j] == 0 && query.same(engine[j]))
			{
				mark[j] = 1;
				count++;
				if (count == s)
				{
					ans++;
					memset(mark, 0, sizeof(mark));
					mark[j] = 1;
					count = 1;
				}
			}
	}
	cout << "Case #" << testnumber << ": " << ans << endl;
}	

int main()
{
	int n;
	freopen(INPUTFILENAME, "r", stdin);
	freopen(OUTPUTFILENAME, "w", stdout);
	cin >> n;
	for (int i = 0; i < n; i++)
	{
		init();
		solve(i + 1);
	}
	return 0;
}