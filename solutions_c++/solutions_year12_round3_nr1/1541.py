#include <string>
#include <vector>
#include <stdint.h>
#include <cstring>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <cassert>
#include <cstdio>
#include <list>
#include <cmath>
#include <climits>
#include <stack>

#define ASSERT(statement, obj) { typeof(obj) x=(statement); if(x!=(obj)){std::cout<<x<<std::endl;assert(false);}}
#define FOR(index, from, to) for (typeof(to) index=from; index<(to); ++index)
#define VFOR(index, v) for (typeof(v.size()) index=0; index<(v.size()); ++index)
#define ITER(it, list) for(typeof(list.begin()) it=list.begin(); it!=list.end();++it)
#define PRINT_VECTOR_INT(v) FOR(i, 0, v.size())cout<<v[i]<<" "
#define PBK push_back
#define MEMSET(mem) memset(mem, 0, sizeof(mem))

using namespace std; 
int N;
int M[1000];
int dig[1000][100];

void dfs(int f, map<int,int>&m)
{
	FOR(j, 0 ,N)if (dig[f][j])
	{
		if (m.find(j) == m.end())
		   m[j] = 1;
		else
		  m[j]++;
		dfs(j ,m);
	}
}

bool exist()
{
	FOR(i, 0 ,N)if (M[i] >= 2)
	{
		//cout<<i<<endl;
		map<int,int> m;
		FOR(j, 0, N)if (dig[i][j])
		{
			if (m.find(j) == m.end())
			  m[j] = 1;
			else
  			  m[j]++;
			dfs(j ,m);
		}
		ITER(it ,m)if (it->second >=2)
		{
			//cout<<it->first<<"====\n";
			return true;
		}
	}
	return false;
}

int main()
{
	string line;
	int T=0;
	getline(cin, line);
	{
		stringstream ss(line);
		ss >> T;
	}

	FOR(t, 0, T)
	{
		{
			getline(cin, line);
			stringstream ss(line);
			ss >> N;
		}
		MEMSET(dig);
		MEMSET(M);

		FOR(n, 0, N)
		{
			getline(cin, line);
			stringstream ss(line);
			ss >> M[n];
			FOR(m, 0, M[n])
			{
				int to;
				ss >> to;
				dig[n][to-1]=1;
			}
		}


		bool has = exist();
		if (has)
  		  printf("Case #%d: Yes\n", t+1);
		else
		  printf("Case #%d: No\n", t+1);
	}
}

