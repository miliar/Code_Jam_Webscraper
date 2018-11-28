#include <algorithm>
#include <cctype>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <iostream>
#include <sstream>
#include <string>
#include <utility>
#include <map>
#include <vector>
#include <cstring>
using namespace std;

#define rev(x) reverse((x).begin(), (x).end())
#define sor(x) sort(x.begin(), x.end())
#define sz size()
#define pb push_back
#define vi vector<int>
#define vvi vector<vi>
#define vs vector<string>
#define ll long long
#define fill(var,val) memset(var, val, sizeof(var))
#define rep(i, n) for(i = 0; i < n; i++)
#define repa(i, a, n) for(i = a; i < n; i++)
#define s(n) scanf("%d", &n);
#define p(n) printf("%d\n", n);

int main()
{
	int t; s(t);
	int k = 0;
	while(t--)
	{
		k++;
		int n, i; s(n);
		int moves[110][2];
		fill(moves, 0);
		rep(i,n)
		{
			char c; cin>>c; 
			int b; s(b);
			moves[i][0] = (c == 'O' ? 0 : 1);
			moves[i][1] = b; 
		}
		int total_time = 0;
		
		int cur_loc[] = { 1, 1 };
		int cur_mover = moves[0][0];
		int prev_mover = -1;
		int time_elapsed_by[] = { 0, 0 };
		
		time_elapsed_by[cur_mover] = abs(moves[0][1] - cur_loc[cur_mover]) + 1;
		total_time += time_elapsed_by[cur_mover];
		cur_loc[cur_mover] = moves[0][1];
		
		repa(i,1,n)
		{
			prev_mover = cur_mover;
			cur_mover = moves[i][0];
			int time_optimizable = abs(moves[i][1] - cur_loc[cur_mover]);
			if(prev_mover != cur_mover)
			{
				time_optimizable -= min(time_optimizable, time_elapsed_by[prev_mover]);
				time_elapsed_by[prev_mover] = 0;
			}
			cur_loc[cur_mover] = moves[i][1];
			time_elapsed_by[cur_mover] += time_optimizable + 1;
			total_time += time_optimizable + 1;
			//cout << total_time << endl;
		}
		cout << "Case #" << k << ": " << total_time << endl;
	}
	return 0;
}
