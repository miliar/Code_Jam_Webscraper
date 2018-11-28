#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <map>
#include <hash_set>
#include <exception>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>

using namespace std;
using namespace stdext;

bool CreateCharSet(const string& q, hash_set<char>* qq, const int& L)
{
	for (int i=0; i<L; i++)
		qq[i].clear();

	bool open = false;
	char c;
	char* s = (char*) q.data();
	int index = -1;
	for (int i=0; i<q.length(); i++)
	{
		c = *s++;

		if (!open && c == '(')
		{
			open = true;
			index++;
			continue;
		} else if (open && c == ')')
		{
			open = false;
			continue;
		}

		if (!open)
			index++;

		if (index >= L)
			return false;

		qq[index].insert(c);
	}

	if (index != L - 1)
		return false;

	return true;	
}

long long Count(hash_set<char>* qq, const int& L, string* ss, const int& D)
{
	string s;
	long long count = 0;
	char* cc;
	int i,j;
	bool state;
	for (i = 0; i<D; i++)
	{
		s = ss[i];
		cc = (char*) s.data();
		state = true;
		for (j = 0; j<s.length(); j++)
		{
			hash_set<char>& h = qq[j];
			if (h.find(*cc++) == h.end())
			{
				state = false;
				break;
			}
		}
		if (state == true)
			count++;
	}
	return count;
}

int L, D, N;
string ss[5000];
string q;
hash_set<char> qq[15];


int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	cin >> L >> D >> N;
	for (int i=0; i<D; i++)
		cin >> ss[i];
		
	int count;
	for (int i=0; i<N; i++)
	{
		cin >> q;
		count = 0;
		if (CreateCharSet(q, qq, L))
		{
			count = Count(qq, L, ss, D);
		}
			
		cout << "Case #" << i+1 << ": " << count << "\n";
	}

	return 0;
}