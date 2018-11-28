#include <iostream>
#include <cstdio>
#include <vector>
#include <utility>
#include <cmath>
using namespace std;

// double solve(double D, int A, int N, vector< pair<double, double> >pos, double acc)
// {
// 	double t = 0.0000000;
// 	double v = 0.0000000;
// 	double other_curr_pos = pos[0].second; 
// 	double me_curr_pos = 0.0000000;
// 	for(int i = 1; i < N && me_curr_pos; i++)
// 		{
// 			double ti, other_next_pos, me_next_pos, next_t, vi;
// 			other_next_pos = pos[i].second;
// 			if(other_next_pos > D)
// 				{
// 					vi = (other_next_pos - other_curr_pos) / ti;
// 					other_next_pos = D;
// 					ti = (D - other_curr_pos) / vi;
// 					next_t = t + ti;
// 					me_next_pos = v*ti + 0.5*a*(ti * ti);
// 					if(me_next_pos > other_next_pos)
// 						{
// 							me_next_pos = other_next_pos;
// 							v = (other_next_pos - other_curr_pos) / ti;
// 						}
// 					else 
// 						{
// 							me_curr_pos = me_next_pos;
// 							v = v + a*ti;
// 						}
					
// 					other_curr_pos = other_next_pos;
// 					t = next_t;
// 					break;
// 				}
// 			else
// 				{
// 					next_t = pos[i].first;
// 					ti = next_t - t;
					
// 					me_next_pos = v*ti + 0.5*a*(ti * ti);
// 					if(me_next_pos > other_next_pos)
// 						{
// 							me_next_pos = other_next_pos;
// 							v = (other_next_pos - other_curr_pos) / ti;
// 						}
// 					else 
// 						{
// 							me_curr_pos = me_next_pos;
// 							v = v + a*ti;
// 						}
					
// 					other_curr_pos = other_next_pos;
// 					t = next_t;
// 				}
// 		}
// 	if(me_curr_pos == D) return t;
// 	else
// 		{
// 			double toD = D - me_curr_pos;
// 			to
// }

double solve(double D, int N, vector< pair<double, double> >pos, double a)
{
	double final_time, vi;
	double t = sqrt(2 * D / a);
	if(N == 2)
		{
			vi = (pos[1].second - pos[0].second) / pos[1].first;
			final_time = (D - pos[0].second) / vi;
			t = max(t, final_time);
		}
	return t;
}

int main()
{
	int T;

	cin >> T;
	double D;
	int A, N;
	double x, t, a;
	vector< pair<double, double> > pos; 
	for(int i = 0; i < T; i++)
		{
			scanf("%lf %d %d", &D, &N, &A);
			pos.clear();
			for(int j = 0; j < N; j++)
				{
					scanf("%lf %lf", &t, &x);
					pos.push_back(make_pair(t, x));
				}
			printf("Case #%d:\n", i+1);
			for(int j = 0; j < A; j++)
				{
					scanf("%lf", &a);
					printf("%0.7lf\n", solve(D, N, pos, a));
				}
		}
	
	return 0;
}
