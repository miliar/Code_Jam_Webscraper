#include <iostream>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <cassert>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <iomanip>
#include <cmath>
#include <functional>
using namespace std;

//#define TEST
#define USE_FILE

#define pb(x) push_back(x)
#define FOR(i,a,b) for(int i = (a); i < (b); ++i) 
#define RFOR(i,a,b) for(int i = (a); i > (b); --i) 

#define printval(x) cout << #x << " = " << (x) << endl;
#define printarray(x) \
	cout << #x << ": "; \
	for(int idx=0; idx<((x).size()); idx++) { cout << ((x)[idx]) << " "; } cout << endl;
#define printmatrix(x) \
	cout << #x << ": " << endl; \
	for(int idx=0; idx<((x).size()); idx++) { \
		for(int idx2=0; idx2<((x)[0].size()); idx2++) { cout << ((x)[idx][idx2]) << " "; } cout << endl; \
	} 

//string szfile_input = "sample.txt";
//string szfile_output = "sample_output.txt";
string szfile_input = "B-small-attempt0.in";
string szfile_output = "B-small-attempt0.out.txt";
//string szfile_input = "B-large.in";
//string szfile_output = "B-large.out.txt";

class FLY{
public:
	double x, y, z;
	double dx, dy, dz;
};


class B_1 {
protected:
	vector<int> V;

public:
	void Run() {
#ifdef USE_FILE
		ifstream cin(szfile_input.c_str());
		ofstream cout(szfile_output.c_str());

#endif
		int ncase;
		cin >> ncase;

		int nflies;
		pair<double, double> value;
		vector<FLY> FF;
		FOR(i, 0, ncase) {
			FF.clear();
			cin >> nflies;
			FLY f;
			double x, y, z, dx, dy, dz;
			FOR(j, 0, nflies) {
				cin >> x >> y >> z >> dx >> dy >> dz;
				f.x = x; f.y = y; f.z = z;
				f.dx = dx; f.dy = dy; f.dz = dz;
				FF.push_back(f);
			}
			value = getNum(FF);
			cout.precision(8);
			cout << "Case #" << i+1 << ": " << fixed << value.first << " " << value.second << endl;
			printf("Case #%d: %lf %lf\n", i+1, value.first, value.second);
		}
	}

	pair<double, double> getNum(vector<FLY> FF) {
		pair<double, double> ret;

		FLY MF;
		MF.x = 0.0; MF.y = 0.0; MF.z = 0.0;
		MF.dx = 0.0; MF.dy = 0.0; MF.dz = 0.0;
		FOR(i, 0, FF.size()) {
			MF.x += FF[i].x; MF.y += FF[i].y; MF.z += FF[i].z;
			MF.dx += FF[i].dx; MF.dy += FF[i].dy; MF.dz += FF[i].dz;
		}
		double fs = (double)FF.size();
		MF.x /= fs; MF.y /= fs; MF.z /= fs; 
		MF.dx /= fs; MF.dy /= fs; MF.dz /= fs; 

		cout << "MF" << endl;
		cout << MF.x << " " << MF.y << " " << MF.z << endl;
		cout << MF.dx << " " << MF.dy << " " << MF.dz << endl;

		double st = 0.0, dt = 1000000.0;
		FOR(i, 0, 100) {
			double c1 = (st+ (dt-st) / 3.0);
			double c2 = (st+ (dt-st) * 2.0 / 3.0);
			if(getDist(MF, c1) > getDist(MF, c2)) st = c1;
			else dt = c2;		
		}
		ret.first = getDist(MF, st);
		ret.second = st;
		return ret;	
	}

	double getDist(FLY FF, double t) {
		double px, py, pz;
		px = FF.x + t*FF.dx;
		py = FF.y + t*FF.dy;
		pz = FF.z + t*FF.dz;
		return sqrt(px*px + py*py + pz*pz);
	}

};

class ClassTest : public B_1 {
public:
	void Test() {
		//printval(getNextNum("123"));
		//printval(getNextNum("223311"));
		//printval(getNextNum("11111"));
	}
};

int main()
{
#ifdef TEST
	ClassTest cnt;
	cnt.Test();
#else
	B_1 cn;
	cn.Run();
#endif
	return 0;
}
