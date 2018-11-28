#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <ctime>
using namespace std;

#define all(x) (x).begin(), (x).end()
#define foreach(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define sz(x) ((int)(x).size())
#define init(st) memset(st, 0, sizeof(st)) 
#define ll long long

template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);

	int L,D,N;
	cin >> L >> D >> N;
	vector<string> vs;

	for(int q = 0; q < D; q++)
	{
		string temp;
		cin >> temp;
		vs.push_back(temp);
	}
	
	for(int q = 0; q < N; q++)
	{
		string word;
		cin >> word;
		ll result = 0;
		for(int i = 0; i < vs.size(); i++)
		{
			int cur = 0;
			bool match = true;
			for(int j = 0; j < word.size(); j++)
			{
				if(word[j] == '(')
				{
					bool flag = false;
					while(word[j] != ')')
					{
						if(word[j] == vs[i][cur])
						{
							flag = true;
						}
						j++;
					}

					if(!flag)
					{
						match = false;
						break;
					}
				}
				else if(word[j] != vs[i][cur])
				{
					match = false;
					break;
				}
				cur++;
			}
			if(match)
				result++;
		}
		printf("Case #%d: %d\n", q+1, result);
	}

	return 0;
}