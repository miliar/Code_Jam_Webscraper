#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>
#include <fstream>
#define SZ(a) a.size()
#define PB push_back
#define FOR(i,s,n) for(int i=s; i<n; i++)
#define FORI(i,n) for(int i=0; i<n; i++)
#define FORSZ(i,n) for(int i=0; i<SZ(n); i++)
#define ALL(x) x.begin(),x.end()

int main(int argc, char* argv[])
{
	int ninp;
	string s,s2;
	ifstream fin(argv[1]);
	fin >> ninp;
	getline(fin,s);
	for (int prob=1; prob <= ninp; prob++)
	{
		int S,Q;
		fin >> S;
		getline(fin,s);
		vector <string> se;
	
		FORI(i,S)
		{
			getline(fin,s);
			se.push_back(s);
		}

		fin >> Q;
		getline(fin,s);
		vector<string> qu;
		FORI(i,Q)
		{
			getline(fin,s);
			qu.push_back(s);
		}

		int nswitch=0;
		int seen=0;
		set<string> st;
	
		for (int i=Q-1; i>=0; i--)
		{
			if (st.find(qu[i]) == st.end())
			{
				seen++;
				if (seen == S)
				{
					st.clear();
					seen=1;
					nswitch++;
				}
				st.insert(qu[i]);
			}

		}

		printf("Case #%d: %d \n", prob, nswitch);
	
	}



	return 0;
}

