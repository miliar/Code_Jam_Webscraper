
#include <iostream>
#include <set>
#include <list>

using namespace std;

const int MAX = 1000001;

int sizex, sizey;

int bleft;

#define is_in(a, b) ((b).find(a) != (b).end())
#define DEBUG(a) { }

struct sparse
{
	typedef set<int> trow;

	trow mat[MAX];
	int m;

	sparse()
	{
		m = 0;
	}

	bool get(int x, int y)
	{
		if (y > m || y <= 0 || x <= 0) return false;
		return (mat[y].find(x) != mat[y].end());
	}

	bool vset(int x, int y)
	{
		if (y > m) m = y;
		pair<trow::iterator, bool> r = mat[y].insert(x);
		return r.second;
	}

	bool unset(int x, int y)
	{
		if (y > m || y <= 0 || x <= 0) return false;
		trow::iterator i = mat[y].find(x);
		if (i != mat[y].end())
		{
			mat[y].erase(i);
			return true;
		}
		return false;
	}

	void clear()
	{
		for (int i = 0; i <= m; i++) mat[i].clear();
		m = 0;
	}

	int nonnull()
	{
		int res = 0;
		for (int i = 0; i <= m; i++) res += mat[i].size();
		return res;
	}
	void p()
	{
		for (int x = 0; x < 100; x++)
		{
			for (int y = 0; y < 100; y++)
			{
				if (get(x,y)) cout << '1'; else cout << '0';
			}
			cout << endl;
		}
	}
};

struct A
{
	int x, y;
	bool cred;

	A(bool _cred, int _x, int _y)
	{
		cred = _cred;
		x = _x;
		y = _y;
	}
};

sparse s;
list<A> a, b;

void perform()
{
	for (list<A>::iterator i = b.begin(); i != b.end(); ++i)
	{
		if (i->cred)
		{
			if (s.vset(i->x, i->y)) bleft++;
		} else
		{
			if (s.unset(i->x, i->y)) bleft--;
		}
	}
	
	b.swap(a);
	b.clear();
}

void updateA()
{
	set<long long int> added, removed;
	
	b.clear();

	for (list<A>::iterator i = a.begin(); i != a.end(); ++i)
	{
		if (i->cred)
		{
			DEBUG(cout << "created: " << i->x << ", " << i->y << endl;)

			long long int zz = (i->y+1) * MAX + i->x;
			if (i->y < sizey && !is_in(zz, added))
			{
				if (s.get(i->x - 1, i->y + 1) && !s.get(i->x, i->y+1))
				{
					DEBUG(cout << "push: true " << i->x << " " << (i->y+1) << endl;)
					b.push_back(A(true, i->x, i->y+1));
					added.insert(zz);
				}
			}
			zz = i->y * MAX + i->x + 1;
			if (i->x < sizex && i->y >= 1 && !is_in(zz, added))
			{
				if (s.get(i->x + 1, i->y - 1) && !s.get(i->x+1, i->y))
				{
					DEBUG(cout << "push: true " << (i->x+1) << " " << i->y << endl;)
					b.push_back(A(true, i->x+1, i->y));
					added.insert(zz);
				}
			}
		} else
		{
			DEBUG(cout << "removed: " << i->x << ", " << i->y << endl;)

			long long int zz = (i->y+1) * MAX + i->x;
			if (i->y < sizey && !is_in(zz, removed))
			{
				if (!s.get(i->x - 1, i->y + 1) && (s.get(i->x, i->y + 1) || is_in(zz, added)))
				{
					DEBUG(cout << "push: false " << i->x << " " << (i->y+1) << endl;)
					b.push_back(A(false, i->x, i->y+1));
					removed.insert(zz);
				}
			}
			zz = i->y * MAX + i->x + 1;
			if (i->x < sizex && i->y >= 1 && !is_in(zz, removed))
			{
				if (!s.get(i->x + 1, i->y - 1) && (s.get(i->x + 1, i->y) || is_in(zz, added)))
				{
					DEBUG(cout << "push: false " << (i->x+1) << " " << i->y << endl;)
					b.push_back(A(false, i->x+1, i->y));
					removed.insert(zz);
				}
			}
		}
	}

	DEBUG(cout << "update done, |a| = " << a.size() << ", |b| = " << b.size() << endl;)
	perform();
}

void addrect(int minx, int maxx, int miny, int maxy)
{
	for (int x = minx; x <= maxx; x++)
	{
		for (int y = miny; y <= maxy; y++)
		{
			if (s.vset(x, y))
			{
				bleft++;
				a.push_back(A(true, x, y));
			}
		}
	}
	if (maxx > sizex) sizex = maxx;
	if (maxy > sizey) sizey = maxy;
}

void finishrect()
{
	for (int x = 0; x <= sizex; x++)
	{
		for (int y = 0; y <= sizey; y++)
		{
			if (!s.get(x, y) && (s.get(x+1,y) || s.get(x, y+1)))
			{
				a.push_back(A(false, x, y));
			}
		}
	}
}

int main()
{
	int N, R;
	cin >> N;

	for (int c = 1; c <= N; c++)
	{
		s.clear();
		a.clear();
		b.clear();
		bleft = 0;
		sizey = 0;
		sizex = 0;

		cin >> R;
		for (int r = 0; r < R; r++)
		{
			int x1, x2, y1, y2;
			cin >> x1 >> y1 >> x2 >> y2;
			addrect(x1, x2, y1, y2);
		}
		finishrect();

		int time = 0;
		while (bleft > 0)
		{
			updateA();
			time++;
			DEBUG(cout << "time = " << time << ", left = " << bleft << ", control = " << s.nonnull() << endl;)
			//DEBUG(s.p();)
		}

		cout << "Case #" << c << ": " << time << endl;
	}
	return 0;
}










