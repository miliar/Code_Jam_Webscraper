#include <fstream>
#include <vector>
#include <string>
#include <algorithm>
#include <memory.h>
using namespace std;
typedef long long lint;
int main(){
	ifstream in("A-large.in");
	ofstream out("output.txt");
	int N;
	in >> N;
	for(int t = 0; t<N; ++t){
		lint n,A,B,C,D,M,x0,y0;
		in >> n >> A >> B >> C >> D  >> x0 >> y0 >>M;
		int X = x0;
		int Y = y0;
		lint V[3][3];
		memset(V,0,sizeof(V));
		for( int i = 0; i<n; ++i){
			++V[X%3][Y%3];
			X = (A * X + B) % M;
			Y = (C * Y + D) % M;
		}
		lint ans = V[0][0]*(V[0][0]-1)*(V[0][0]-2)/6;
		ans += V[0][0]*V[0][1]*V[0][2];
		ans += V[0][1]*(V[0][1]-1)*(V[0][1]-2)/6;
		ans += V[0][2]*(V[0][2]-1)*(V[0][2]-2)/6;

		ans += V[0][0]*V[1][0]*V[2][0];

		ans += V[0][0]*V[1][1]*V[2][2];
		ans += V[0][0]*V[1][2]*V[2][1];
		ans += V[0][1]*V[1][2]*V[2][0];
		ans += V[0][1]*V[1][0]*V[2][2];
		ans += V[0][2]*V[1][1]*V[2][0];
		ans += V[0][2]*V[1][0]*V[2][1];

		ans += V[0][1]*V[1][1]*V[2][1];
		ans += V[0][2]*V[1][2]*V[2][2];

		ans += V[1][0]*(V[1][0]-1)*(V[1][0]-2)/6;
		ans += V[1][0]*V[1][1]*V[1][2];
		ans += V[1][1]*(V[1][1]-1)*(V[1][1]-2)/6;
		ans += V[1][2]*(V[1][2]-1)*(V[1][2]-2)/6;

		ans += V[2][0]*(V[2][0]-1)*(V[2][0]-2)/6;
		ans += V[2][0]*V[2][1]*V[2][2];
		ans += V[2][1]*(V[2][1]-1)*(V[2][1]-2)/6;
		ans += V[2][2]*(V[2][2]-1)*(V[2][2]-2)/6;

		out<<"Case #"<<t+1<<": "<<ans<<endl;
	}
	return 0;
}