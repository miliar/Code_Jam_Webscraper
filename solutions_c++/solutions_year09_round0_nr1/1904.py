#include <vector>
#include <string>
#include <fstream>
#include <algorithm>

using namespace std;

bool comp(const string &lhs, const string &rhs)
{
	for(int i = 0; i < min(lhs.size(), rhs.size()); i++)
	{
		if(lhs[i] < rhs[i])
			return true;
		else if(lhs[i] > rhs[i])
			return false;
	}
	return false;
}

int gogo(const vector<string> &w, const string &s, string cur, int c)
{
	if(c >= s.size())
	{
		return 1;
	}
	else if(s[c] != '(')
	{
		if(binary_search(w.begin(), w.end(), cur + s[c], comp))
			return gogo(w, s, cur + s[c], c + 1);
		else
			return 0;
	}
	else
	{
		int ret = 0;
		c++;
		int t = c;
		while(s[c] != ')')
			c++;
		c++;
		for(t; t < c - 1; t++)
		{
			if(binary_search(w.begin(), w.end(), cur + s[t], comp))
				ret += gogo(w, s, cur + s[t], c);
		}
		return ret;
	}
}

int main()
{
	int N, L, D;
	vector<string> w;
	vector<string> s;
	string t;
	ifstream f;
	f.open("A.txt");
	f >> L >> D >> N;
	for(int i = 0; i < D; i++)
	{
		f >> t;
		w.push_back(t);
	}
	sort(w.begin(), w.end());
	for(int i = 0; i < N; i++)
	{
		f >> t;
		s.push_back(t);
		
	}
	f.close();
	ofstream o;
	o.open("Aout.txt");
	for(int i = 0; i < N; i++)
	{
		o << "Case #" << (i+1) << ": " << gogo(w, s[i], "", 0) << endl;
	}
	o.close();
	return 0;
}