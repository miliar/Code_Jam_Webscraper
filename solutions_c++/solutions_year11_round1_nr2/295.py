#include <iostream>
#include <list>

using namespace std;

class word
{
public:
	int len;
	char *s;

	void fillapp(bool *app)
	{
		for (int i = 0; i < len; i++)
		{
			app[s[i]] = true;
		}
	}

	bool consistent(bool *uncover, word &other)
	{
		if (len != other.len) return false;

		for (int i = 0; i < len; i++)
		{
			if ((uncover[s[i]] || uncover[other.s[i]]) && (s[i] != other.s[i])) return false;
		}
		return true;
	}

	void load(string &ss)
	{
		len = ss.length();
		s = new char[len+1];
		for (int i = 0; i < len; i++) s[i] = ss[i];
		s[len] = 0;
	}

	word()
	{
		len = 0;
		s = 0;
	}

	~word()
	{
		if (s) delete [] s;
	}
};

int loosingpoints(int N, word *pool, word &w, string &order)
{
	bool uncover[200];
	bool resapp[200];
	
	for (char c = 'a'; c <= 'z'; c++) { resapp[c] = false; uncover[c] = false; }
	w.fillapp(resapp);

	list<word*> l;
	for (int i = 0; i < N; i++) l.push_back(&pool[i]);

	int points = 0;
	for (int i = 0; i < order.length(); i++)
	{
		// filter out
		bool change = false;
		for (list<word*>::iterator ii = l.begin(); ii != l.end(); )
		{
			if (!(*ii)->consistent(uncover, w))
			{
				ii = l.erase(ii);
				change = true;
			} else
			{
				++ii;
			}
		}

		/*
		if (change)
		{
			cout << endl;
			for (list<word*>::iterator ii = l.begin(); ii != l.end(); ++ii)
			{
				cout << (*ii)->s << " ";
			}
		}
		*/

		// appearance
		bool app[200];
		for (char c = 'a'; c <= 'z'; c++) app[c] = false;
		for (list<word*>::iterator ii = l.begin(); ii != l.end(); ++ii) (*ii)->fillapp(app);

		if (l.size() == 1) break;

		if (app[order[i]])
		{
			//cout << order[i];
			if (!resapp[order[i]])
			{
				points++;
				//cout << "!";
			}
			//uncover[order[i]] = true;
		}
		uncover[order[i]] = true;
	}

	return points;
}

int main()
{
	int T;

	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int N, M;

		cin >> N >> M;
		
		string ss;
		word *w = new word[N];
		for (int i = 0; i < N; i++)
		{
			cin >> ss;
			w[i].load(ss);
		}

		cout << "Case #" << t << ":";

		for (int i = 0; i < M; i++)
		{
			cout << " ";
			cin >> ss;
			word *mw;
			int pw = -1;
			for (int j = 0; j < N; j++)
			{
				int p = loosingpoints(N, w, w[j], ss);
				//cout << "[" << w[j].s << "]=" << p << " ";
				if (p > pw)
				{
					mw = &w[j];
					pw = p;
				}
			}
			cout << mw->s;
		}

		delete [] w;
		cout << endl;
	}
}

