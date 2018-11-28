#include <fstream>
#include <iostream>
#include <vector>
#define _max 16
#define _max_table 65536
using namespace std;

string data;
int graph[_max][_max];
int n, m;

long long table[_max_table][_max][_max];
long long solution;

void generate_graph()
{
	int i, j, k;
	for(i = 0; i < n; i++)
	{
		for(j = i + 1; j < n; j++)
		{
			graph[i][j] = 0;
			for(k = 0; k < m; k+= n)
			{
				if(data[k + i] != data[k + j])
				{
					graph[i][j]++;
				}
			}
//			cout << i << " " << j << " : " << graph[i][j] << endl;
			graph[j][i] = graph[i][j]; // symmetric
		}
	}
}

void init()
{
	int i, j, k;
	int i_max;
	
	i_max = 1 << n;
	for(i = 0; i < i_max; i++)
		for(j = 0; j < n; j++)
			for(k = 0; k < n; k++)
				table[i][j][k] = -1; // inf
}

void Backtracking(int s, int e, int point, long long dist)
{
	int i;
	if(table[point][s][e] == - 1 || table[point][s][e] > dist)
	{
		table[point][s][e] = dist;
		for(i = 0; i < n ;i++)
		{
			if(point & (1 << i)) continue;
			point += (1 << i);
			Backtracking(s, i, point, dist + (long long)graph[e][i]);
			point -= (1 << i);
		}
	}
}

void find_solution()
{
	int i, j, k;
	long long value;
	int full_point;
	solution = -1;
	full_point = (1 << n) - 1;
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < n; j++)
		{
			if(i == j) continue;
			
			value = table[full_point][i][j] + 1;
			
			for(k = 0; k < (m - n); k+= n)
			{
				if(data[k + j] != data[k + n + i]) value++;
			}
			if(solution == -1 || value < solution)
			{
//				cout << n << "case: " << i << " " << j << " " << table[full_point][i][j] << " " << value << endl;
				solution = value;
			}
		}
	}
}

int main()
{
	ifstream fin("problemD.in");
	ofstream fout("problemD.out");
	
	int test_case;
	int num_test_cases;
	
	int i;
	
	fin >> num_test_cases;
	for(test_case = 1; test_case <= num_test_cases; test_case++)
	{	
		fin >> n;
		fin >> data;
		m = data.length();
		generate_graph();
		init();
		for(i = 0; i < n; i++)
		{
			Backtracking(i, i, (1<<i), 0); 	
		}
		find_solution();
		fout << "Case #" << test_case << ": " << solution << endl;
	}
	
	fin.close();
	fout.close();
	return 0;
}