#include <cstdio>
#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
using namespace std;

int main(){
  int C;
  scanf("%d", &C);
  for(int c = 1; c <= C; ++c){
	int N;
	scanf("%d", &N);
	int x, y, z, vx, vy, vz;
	long long sum_x= 0, sum_y= 0, sum_z= 0, sum_vx= 0, sum_vy= 0, sum_vz = 0;
	for(int i = 0; i < N; ++i){
		scanf("%d%d%d%d%d%d", &x,&y,&z, &vx, &vy, &vz);
		sum_x += x;
		sum_y += y;
		sum_z += z;
		sum_vx += vx;
		sum_vy += vy;
		sum_vz += vz;
	}
	long long up = sum_x*sum_vx + sum_y*sum_vy + sum_z*sum_vz;
	long long down = sum_vx*sum_vx + sum_vy*sum_vy + sum_vz*sum_vz;
	long double t_min = ((long double)-up)/((long double)down);
	long double first_sq = (sum_x + t_min*sum_vx)*(sum_x + t_min*sum_vx);
	long double second_sq = (sum_y + t_min*sum_vy)*(sum_y + t_min*sum_vy);
	long double third_sq = (sum_z + t_min*sum_vz)*(sum_z + t_min*sum_vz);
	long double d_min;
	if (t_min == t_min && t_min >= 0) { //not nan and pos
		d_min = sqrt(first_sq + second_sq + third_sq)/((long double) N);
		printf("Case #%d: %.8llf %.8llf\n", c, d_min, t_min);
	} else {
		d_min = sqrt(sum_x*sum_x + sum_y*sum_y + sum_z*sum_z)/((long double) N);
		printf("Case #%d: %.8llf %.8llf\n", c, d_min, 0.0);
	}
  }
  return 0;
}
