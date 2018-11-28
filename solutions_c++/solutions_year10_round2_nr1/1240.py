//Sat May 22 10:47:57 CDT 2010
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(int argc, char* argv[])
{
	freopen("input.in", "r", stdin);
	freopen("output.out", "w", stdout);
	int T;
	cin >> T;
	for (int ncase = 1; ncase <= T; ncase++)
	{
		vector<pair<int, pair<string, string> > > v;
		int N, M;
		cin >> N >> M;
		for (int i = 0; i < N; i++)
		{
			string s;
			cin >> s;
			int count = 0;
			string temp1;
			string temp2;
			for (int idx = 1; idx < (int) s.size(); idx++)
			{
				if (s[idx] == '/')
				{
					if (temp1.size() > 0)
					{
						if (temp2.size() > 0)
						{
							v.push_back(make_pair(count,
									make_pair(temp1, temp2)));
						}
						else
						{
							v.push_back(make_pair(count, make_pair(temp1, "/")));
						}
						count++;
						temp2 += temp1;
						temp1.clear();
					}
					else
					{
						continue;
					}
				}
				else
				{
					temp1 += s[idx];
				}
			}
			if (temp1.size() > 0)
			{
				if (temp2.size() > 0)
				{
					v.push_back(make_pair(count, make_pair(temp1, temp2)));
				}
				else
				{
					v.push_back(make_pair(count, make_pair(temp1, "/")));
				}
				count++;
				temp2 += temp1;
				temp1.clear();
			}
		}

		set<pair<int, pair<string, string> > > p(v.begin(), v.end());
		int sum = 0;
		for (int i = 0; i < M; i++)
		{
			string s;
			cin >> s;
			int count = 0;
			string temp1;
			string temp2;
			for (int idx = 1; idx < (int) s.size(); idx++)
			{
				if (s[idx] == '/')
				{
					if (temp1.size() > 0)
					{
						if (temp2.size() > 0)
						{
							int sz = p.size();
							p.insert(make_pair(count, make_pair(temp1, temp2)));
							if ((int) p.size() > sz)
								sum++;
						}
						else
						{
							int sz = p.size();
							p.insert(make_pair(count, make_pair(temp1, "/")));
							if ((int) p.size() > sz)
								sum++;
						}
						count++;
						temp2 += temp1;
						temp1.clear();
					}
					else
					{
						continue;
					}
				}
				else
				{
					temp1 += s[idx];
				}
			}
			if (temp1.size() > 0)
			{
				if (temp2.size() > 0)
				{
					int sz = p.size();
					p.insert(make_pair(count, make_pair(temp1, temp2)));
					if ((int) p.size() > sz)
						sum++;
				}
				else
				{
					int sz = p.size();
					p.insert(make_pair(count, make_pair(temp1, "/")));
					if ((int) p.size() > sz)
						sum++;
				}
				count++;
				temp2 += temp1;
				temp1.clear();
			}
		}
		set<pair<int, pair<string, string> > >::iterator it;
//		for (it = p.begin(); it != p.end(); it++)
//		{
//			cout << (*it).first << ", " << (*it).second.first << ","
//					<< (*it).second.second << endl;
//		}
		cout << "Case #" << ncase << ": ";
		cout << sum << endl;
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
