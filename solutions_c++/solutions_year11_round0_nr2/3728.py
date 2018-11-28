#include <iostream>
#include <vector>
#include <map>
#include <utility>

using namespace std;

template <class T>
bool contains(const vector<T> &vec, const T &val)
{
	for (unsigned int i=0; i<vec.size(); ++i)
		if (vec[i]==val) return true;
	return false;
}

void addchar(vector<char> &magicks, char c, map<pair<char,char>,char> &replace, map<char,char> remove)
{
	if (magicks.size()==0)
	{
		magicks.push_back(c);
		return;
	}
	char tmp;
	tmp=replace[make_pair(c,magicks.back())];
	if (tmp!='\0')
	{
		magicks.pop_back();
		addchar(magicks, tmp, replace, remove);
		return;
	}
	tmp=remove[c];
	if (contains(magicks, tmp))
	{
		magicks.clear();
		return;
	}
	magicks.push_back(c);
}

template <class T>
ostream &operator<<(ostream &out, const vector<T> &v)
{
	out << '[';
	if (v.size()!=0)
		out << v.front();
	for (unsigned int i=1; i<v.size(); ++i)
		out << ", " << v[i];
	return out << ']';
}

int main()
{
	int n;
	cin >> n;
	for (int casenum=1; casenum<=n; ++casenum)
	{
		int j;
		map<pair<char,char>,char> replace;
		cin >> j;
		while (j--)
		{
			char in1, in2, out;
			cin >> in1 >> in2 >> out;
			replace[make_pair(in1,in2)]=out;
			replace[make_pair(in2,in1)]=out;
		}
		map<char,char> remove;
		cin >> j;
		while (j--)
		{
			char c1, c2;
			cin >> c1 >> c2;
			remove[c1]=c2;
			remove[c2]=c1;
		}
		vector<char> magicks;
		cin >> j;
		while (j--)
		{
			char c;
			cin >> c;
			addchar(magicks, c, replace, remove);
		}
		cout << "Case #" << casenum << ": " << magicks << endl;
	}
}
