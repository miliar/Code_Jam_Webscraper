#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cmath>
#include <bitset>
#include <cctype>
using namespace std;

#define f(i, n)							for(int i = 0; i < n; i ++)
#define pb								push_back
#define sz(a)							int(a.size())

typedef vector<int> VI;
typedef vector<VI> VVI;

class Graph_Flow
{
public:

int max_flow(VVI capacity, const int &source, const int &sink)
{
int path_capacity, ret = 0;
	
	while(path_capacity = find_path(capacity, source, sink)) ret += path_capacity;
	
	return ret;
}

int min_cut_sum_of_edges(const VVI &capacity)
{
int N = sz(capacity);
int ret = INT_MAX;
	
	f(i, N) if(i != 0) ret = min(ret, max_flow(capacity, 0, i));
	
	return ret;
}

VI min_cut_nodes(VVI capacity)
{
int N = sz(capacity), sum_of_edges;
bool used[N];
VI ret;
	
	memset(used, false, sizeof(used));
	
	sum_of_edges = min_cut_sum_of_edges(capacity);
	
	f(i, N) if(i != 0 && max_flow(capacity, 0, i) == sum_of_edges)
	{
		while(find_path(capacity, 0, i));
		
		ret.pb(0);
		used[0] = true;
		
		f(j, sz(ret)) f(k, N) if(capacity[ret[j]][k] && !used[k])
		{
			ret.pb(k);
			
			used[k] = true;
		}
		
		break;
	}
	
	return ret;
}

private:

int find_path(VVI &capacity, const int &source, const int &sink)
{
int N = sz(capacity);
bool used[N];
int from[N], q[N], size, now;
int path_capacity = INT_MAX;
	
	
	size = 0;
	memset(from, -1, sizeof(from));
	memset(used, false, sizeof(used));
	
	q[size ++] = source;
	used[source] = true;
	
	f(top, size)
	{
		now = q[top];
		
		f(next, N) if(capacity[now][next] && !used[next])
		{
			q[size ++] = next;
			from[next] = now;
			used[next] = true;
			
			if(next == sink) goto augment;
		}
	}
	
	return 0;
	
	augment:
	
	for(now = sink; 0 <= from[now]; now = from[now])
	{
		path_capacity = min(path_capacity, capacity[from[now]][now]);
	}
	
	for(now = sink; 0 <= from[now]; now = from[now])
	{
		capacity[from[now]][now] -= path_capacity;
		capacity[now][from[now]] += path_capacity;
	}
	
	return path_capacity;
}

};


const int MAX_N = 100;
const int MAX_M = 100;
const int dx[4] = {- 1,   0, - 1,   0};
const int dy[4] = {- 1, - 1, + 1, + 1};

int N, M, id[MAX_N][MAX_M], ans;
char a[MAX_N][MAX_M];
VVI capacity;
Graph_Flow G;


void Read()
{
	scanf("%d %d", & N, & M);
	
	for(int i = 0; i < N; i ++)
	{
		scanf("%s", a[i]);
	}
}

void Solve()
{
int flow, nodes = N * M + 2, s = 0, t = N * M + 1, temp = 0, all = 0;
	
	capacity = VVI(nodes, VI(nodes, 0));
	
	for(int x = 0; x < N; x ++)
	{
		for(int y = 0; y < M; y ++)
		{
			if(a[x][y] == '.') all ++;
			
			id[x][y] = ++ temp;
//			printf("%d  ", id[x][y]);
		}
//		printf("\n");
	}
//	system("pause");
	
	for(int x = 0; x < N; x ++)
	{
		for(int y = 0; y < M; y ++)
		{
			if(a[x][y] == 'x') continue;
			
			int n1 = id[x][y];
			
			if(y & 1) capacity[n1][t] = 1;
			else capacity[s][n1] = 1;
			
			for(int i = 0; i < 4; i ++)
			{
				int new_x = x + dx[i];
				int new_y = y + dy[i];
				
				if(!(0 <= new_x && new_x < N)) continue;
				if(!(0 <= new_y && new_y < M)) continue;
				
				int n2 = id[new_x][new_y];
				
				if(y & 1) capacity[n2][n1] = 1;
				else capacity[n1][n2] = 1;
			}
		}
	}
	
/*
	for(int i = 0; i < nodes; i ++)
	{
		for(int j = 0; j < nodes; j ++)
		{
			printf("%d  ", capacity[i][j]);
		}
		printf("\n");
	}
	system("pause");
*/
	
	flow = G.max_flow(capacity, s, t);
	
//	printf("flow = %d\n", flow);
//	system("pause");
	
	ans = all - flow;
}

void Write(const int test_case)
{
	printf("Case #%d: %d\n", test_case, ans);
}

int main()
{
int TESTS;
	
	scanf("%d", & TESTS);
	
	for(int i = 1; i <= TESTS; i ++)
	{
		Read();
		
		Solve();
		
		Write(i);
	}
	
	return 0;
}
