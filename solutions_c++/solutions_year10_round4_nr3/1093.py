#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <map>
#include <ctype.h>

using namespace std;


int T;
int r;
int x1, y1, x2, y2;
map< pair<int, int>, int > v_to_in;
vector< set< pair<int, int> > > in_to_v;
vector< pair<int, int> > birth_queue, die_queue;
set< pair<int, int> > is_exists;

void Birth(int x, int y)
{
	if (is_exists.find( make_pair(x, y) ) != is_exists.end())
		return;

	is_exists.insert(make_pair(x, y));
	birth_queue.push_back( make_pair(x, y) );
}

void DoBirthes()
{
	int x, y;
	pair<int, int> v;

	for (int i = 0; i < (int)birth_queue.size(); i++)
	{
		x = birth_queue[i].first;
		y = birth_queue[i].second;

		v = birth_queue[i];

		if (v_to_in.find(make_pair(x, y)) == v_to_in.end())
		{
			v_to_in[v] = 0;
			in_to_v[0].insert(v);
		}

		v = make_pair(x + 1, y);

		if (v_to_in.find(v) != v_to_in.end())
			v_to_in[v]++;
		else
			v_to_in[v] = 1;

		in_to_v[v_to_in[v] - 1].erase(v);
		in_to_v[v_to_in[v]].insert(v);

		v = make_pair(x, y + 1);

		if (v_to_in.find(v) != v_to_in.end())
			v_to_in[v]++;
		else
			v_to_in[v] = 1;

		in_to_v[v_to_in[v] - 1].erase(v);
		in_to_v[v_to_in[v]].insert(v);
	}

	birth_queue.clear();
}

void Die(int x, int y)
{
	die_queue.push_back( make_pair(x, y) );
}

void DoDie()
{
	int x, y;
	pair<int, int> v;

	for (int i = 0; i < (int)die_queue.size(); i++)
	{
		v = die_queue[i];

		if (is_exists.find(v) == is_exists.end())
			continue;

		x = v.first;
		y = v.second;

		v_to_in.erase(v_to_in.find(v));
		in_to_v[0].erase(in_to_v[0].find(v));
		is_exists.erase(is_exists.find(v));

		v = make_pair(x + 1, y);
		v_to_in[v]--;

		for (int i = 1; i <= 2; i++)
		{
			if (in_to_v[i].find(v) != in_to_v[i].end())
			{
				in_to_v[i - 1].insert(v);
				in_to_v[i].erase(in_to_v[i].find(v));
				break;
			}
		}

		v = make_pair(x, y + 1);
		v_to_in[v]--;

		for (int i = 1; i <= 2; i++)
		{
			if (in_to_v[i].find(v) != in_to_v[i].end())
			{
				in_to_v[i - 1].insert(v);
				in_to_v[i].erase(in_to_v[i].find(v));
				break;
			}
		}
	}

	die_queue.clear();
}

void Solve(int counter)
{
	long long rez = 0;

	in_to_v.clear();
	in_to_v.resize(3);
	v_to_in.clear();
	birth_queue.clear();
	die_queue.clear();
	is_exists.clear();

	cin >> r;

	for (int i = 0; i < r; i++)
	{
		cin >> x1 >> y1 >> x2 >> y2;

		for (int x = x1; x <= x2; x++)
			for (int y = y1; y <= y2; y++)
				Birth(x, y);
	}

	DoBirthes();

	while ( !is_exists.empty())
	{
		for (set< pair< int, int> >::iterator iter = in_to_v[2].begin(); iter != in_to_v[2].end(); iter++)
		{
			Birth(iter->first, iter->second);
		}

		for (set< pair< int, int> >::iterator iter = in_to_v[0].begin(); iter != in_to_v[0].end(); iter++)
		{
			Die(iter->first, iter->second);
		}

		DoDie();

		DoBirthes();

		rez++;
	}

	cout << "Case #" << counter << ": " << rez << endl;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C.out", "w", stdout);

	cin >> T;

	for (int counter = 0; counter < T; counter++)
	{
		Solve(counter + 1);
	}

	return 0;
}