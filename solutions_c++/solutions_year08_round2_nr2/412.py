#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <cmath>
#include <cstdio>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <numeric>

using namespace std;

bool isprime(int x)
{
	int i;

	for(i = 2; i * i <= x; ++i)
		if (x % i == 0) return false;
	return true;
}

void prfactor(int x, int p, vector <int> & pr)
{
	int i;
	
	for(i = p; i <= x; ++i)
		if (isprime(i) && x % i == 0) pr.push_back(i);
}

int main()
{
	int T, N;
	ifstream fin("b.in");
	ofstream fout("b.out");
	
	fin >> N;

	for(T = 1; T <= N; ++T)
	{
		fout << "Case #" << T << ": ";
		int a, b, p, j, i, res = 0, n, k;
		fin >> a >> b >> p;

		vector <int> pos(1001);

		n = 0;
		for(i = a; i <= b; ++i)		
			pos[i] = n++;

		vector <set <int> > adj(n);

		for(i = a; i <= b; ++i)
		{
			vector <int> pr;
			prfactor(i, p, pr);
			for(j = i + 1; j <= b; ++j)
			{
				for(k = 0; k < pr.size(); ++k)
					if (j % pr[k] == 0)
					{
						adj[pos[i]].insert(pos[j]);
						adj[pos[j]].insert(pos[i]);
					}
			}
		}


		vector <bool> check(n ,false);

		k = n;

		while(k)
		{
			for(i = 0; i < n; ++i)
				if (!check[i]) break;

			queue <int> q;
			q.push(i);
			--k;
			check[i]= true;
			
			while(!q.empty())
			{
				int u = q.front();
				set <int>::iterator si;

				for(si = adj[u].begin(); si != adj[u].end(); ++si)
				{
					if (!check[*si])
					{
						check[*si] = true;
						q.push(*si);
						--k;
					}
				}
				q.pop();
			}
			++res;
		}

		fout << res << endl;
	}
}