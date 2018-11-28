#include <vector>
#include <string>
#include <map>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <list>
#include <set>
#include "math.h"

using namespace std;

#define pb push_back
#define fori(i, n) for ( int i = 0; i < (n); i++ )
#define forr(i, a, b) for ( int i = (a); i <= (b); i++ )
#define size(a) int((a).size())
#define all(x) (x).begin(),(x).end()
#define sorting(x) sort(all(x))
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end()
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define print_m(m) for(int i = 0;i<(int) m.size();i++) print_v(m[i]); cout << endl;
#define print_v(v) { for(int j = 0;j<(int) v.size();j++) cout << v[j] << " "; cout << endl; }
#define trace(x...)
#define PRINT(x...) trace(printf(x))
#define watch(x) trace(cout << #x " = " << x << "\n")

#define GRANDE 6000

const int INF = 0x3FFFFFFF;
const double EPS = 1e-10;
const double PI = 3.14159265;
const double EXP = 2.71828183;

int main()
{
	int teste, T, N;
	scanf("%d\n", &T);
	for(teste=1; teste<=T; teste++){
		scanf("%d\n", &N);
		//average center of mass position and speed
		long double pos_x, pos_y, pos_z;
		int p_x, p_y, p_z;
		long double vel_x, vel_y, vel_z;
		int v_x, v_y, v_z;
		pos_x = pos_y = pos_z = 0.0;
		vel_x = vel_y = vel_z = 0.0;
		//Watch for precision
		fori(i,N){
			scanf("%d %d %d %d %d %d\n", &p_x, &p_y, &p_z, &v_x, &v_y, &v_z);
			pos_x = ((i)*pos_x + p_x)/(i+1);
			pos_y = ((i)*pos_y + p_y)/(i+1);
			pos_z = ((i)*pos_z + p_z)/(i+1);
			vel_x = ((i)*vel_x + v_x)/(i+1);
			vel_y = ((i)*vel_y + v_y)/(i+1);
			vel_z = ((i)*vel_z + v_z)/(i+1);
// 			pos_x += p_x;
// 			pos_y += p_y;
// 			pos_z += p_z;
// 			vel_x += v_x;
// 			vel_y += v_y;
// 			vel_z += v_z;
		}
// 		pos_x /= 1.0 * N;
// 		pos_y /= 1.0 * N;
// 		pos_z /= 1.0 * N;
// 		vel_x /= 1.0 * N;
// 		vel_y /= 1.0 * N;
// 		vel_z /= 1.0 * N;
		
		PRINT("Average(%d) pos (%.2f,%.2f,%.2f), avg vel (%.2f,%.2f,%.2f)\n",N,pos_x, pos_y, pos_z,vel_x, vel_y, vel_z);
		
		//Contas....
// 		//Point Q on the line = <pos_x, pos_y, pos_z>. P = <0,0,0>. QP = <0-pos_x,...>
// 		double qp_x = -pos_x;
// 		double qp_y = -pos_y;
// 		double qp_z = -pos_z;
		double t = -(pos_x*vel_x + pos_y*vel_y  + pos_z*vel_z) / (vel_x*vel_x + vel_y*vel_y + vel_z*vel_z);
		double temp = (vel_x*vel_x + vel_y*vel_y + vel_z*vel_z);
		if(temp < EPS) t = 0.0;
		if(t < EPS) t = 0.0;
		double distance = sqrt( pow(pos_x + vel_x*t,2) + pow(pos_y + vel_y*t,2) + pow(pos_z + vel_z*t,2) );
		PRINT(" %.3f + %.3f + %.3f \n", pow(pos_x + vel_x*t,2), pow(pos_y + vel_y*t,2), pow(pos_z + vel_z*t,2));
		
		if(distance < EPS) distance = 0.0;
		if(t < EPS) t = 0.0;
		printf("Case #%d: %.8f %.8f\n", teste, distance, t);
		//d = sqrt( (dx + vx*t)^2 + (y-1)^2 + (z-1)^2 )
		
	}
	return 0;
}