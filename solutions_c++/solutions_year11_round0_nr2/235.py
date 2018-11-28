#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <vector>
#include <string>
using namespace std;

int T;
int C,D,N;
vector<string> a, b;
string pi;
vector<char> o;

bool merge()
{
	if (o.size()<=1)
		return false;
	char c1 = o[o.size()-1], c2 = o[o.size() - 2];
	for (int i=0; i<a.size(); i++)
		if ((a[i][0] == c1 && a[i][1] == c2)||
			(a[i][0]==c2 && a[i][1] == c1))
		{
			char c3 = a[i][2];
			o.pop_back();
			o.pop_back();
			o.push_back(c3);
			return true;
		}
	return false;
}

bool clear()
{
	char c = o[o.size()-1];
	for (int i=0; i<o.size()-1; i++)
		for (int j=0; j<b.size(); j++)
			if (b[j][0] == o[i] && b[j][1] == c)
			{
				o.clear();
				return false;
			}
			else if (b[j][1] == o[i] && b[j][0] == c)
			{
				o.clear();
				return false;
			}
	return false;
}

void solve()
{
	for (int i=0; i<pi.size(); i++)
	{
		o.push_back(pi[i]);
		while (merge());
		while (clear());
	}
}

int main()
{
	freopen("B-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> T;
	for (int i=1; i<=T; i++)
	{
		string tmp;
		a.clear();
		b.clear();
		o.clear();
		cin >> C;
		for (int j=0; j<C; j++)
		{
			cin >> tmp;
			a.push_back(tmp);
		}
		cin >> D;
		for (int j=0; j<D; j++)
		{
			cin >> tmp;
			b.push_back(tmp);
		}
		cin >> N;
		cin >> pi;
		printf("Case #%d: ", i);
		solve();
		printf("[");
		for (int j=0; j<o.size(); j++)
			if (j==0)
				printf("%c", o[j]);
			else
				printf(", %c", o[j]);
		printf("]\n");
	}
}