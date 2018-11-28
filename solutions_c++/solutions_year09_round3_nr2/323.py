#pragma region MyTemplate
#include <iostream>
#include <iomanip>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <utility>
#include <algorithm>
#include <numeric>
#include <cmath>
#include <cstdio>
#include <cstdlib>
using namespace std;

typedef long long ll;
typedef long double ld;
typedef vector<int> ivec;
typedef vector<string> svec;
typedef vector<double> dvec;
typedef pair<int,int> ipair;

#define For(i,a,b) for (int i(a),_b(b); i <= _b; ++i)
#define Ford(i,a,b) for (int i(a),_b(b); i >= _b; --i)
#define Rep(i,n) for (int i(0),_n(n); i < _n; ++i)
#define Repd(i,n) for (int i((n)-1); i >= 0; --i)
#define Fill(a,c) memset(&a, c, sizeof(a))
#define MP(x, y) make_pair((x), (y))
#define All(v) (v).begin(), (v).end()
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define PRECISION(fout, caseid, obj, i) fout<<"Case #"<<caseid<<": "<<setw(i)<<setprecision(i)<<left<<setfill('0')<<showpoint<<obj<<endl

#define MAXCHILD 10
class TREE{
public:
	TREE():p(NULL),childno(0){
		chi = new TREE*[MAXCHILD];
	}
	int childno;
	TREE *p;
	TREE **chi;
	//other data member:
};
#pragma endregion

int T, N;
ifstream fin;
ofstream fout;
ld cx,cy,cz, cvx,cvy,cvz;

ld dist(ld a, ld b, ld c){
	return sqrt(a*a + b*b +c*c);
}

pair<ld, ld> cal(ld caseid){
	ld a, b, c;
	a = cvx*cvx + cvy*cvy + cvz*cvz;
	b = 2.0*( cvx*cx + cvy*cy + cvz*cz );
	c = cx*cx + cy*cy + cz*cz;
	if(a<1E-12){
		return MP(dist(cx, cy, cz), 0);
	}

	ld t, d;
	t = -b/(2.0*a);
	if(t<0) t=0;
	d = a*t*t + b*t +c;
	if(d<0) d=0;
	return MP(sqrt(d), t);
}


int main(){
	fin.open("B-large.in");
//	fout.open("small-result.txt");
	fout.open("large-result.txt");

	fin>>T;
	For(caseid,1,T){
		//Read Input Data:
		fin>>N;
		cx = cy = cz = cvx = cvy = cvz = 0;
		ld x,y,z, vx,vy,vz;
		Rep(i,N){
			fin>>x>>y>>z>>vx>>vy>>vz;
			cx += x;
			cy += y;
			cz += z;
			cvx += vx;
			cvy += vy;
			cvz += vz;
		}
		cx = cx/N;
		cy = cy/N;
		cz = cz/N;
		cvx = cvx/N;
		cvy = cvy/N;
		cvz = cvz/N;

		//Compute:

		pair<ld, ld> ans=cal(caseid);
		if(fabs(ans.first) < 1E-6) ans.first=0;
		if(fabs(ans.second)< 1E-6) ans.second=0;
		//Output:
		fout<<"Case #"<<caseid<<": "<<fixed<<ans.first<<" "<<ans.second<<endl;
	}
	fin.close();
	fout.close();
}
