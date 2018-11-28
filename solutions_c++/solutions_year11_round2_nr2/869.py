#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
//#include <iostream>
#include <fstream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <climits>
using namespace std;

ifstream cin("B-small-attempt1.in");
ofstream cout("Bsmall1.out");


//ifstream cin("B-Large.in");
//ofstream cout("B-Large.out");

bool isFeasible(vector <double> &vp, vector <double> &vv, double D, double tm){
	double leftx = vp[0]-tm;
	//if(vp[0]-leftx < D) return false;
	double rightx = leftx+D*(vv[0]-1); //need to check this formula later
	//check if there is time to go to the right
	if(tm<rightx-vp[0]) return false;
	//there is time to place the first batch starting at leftx and ending at rightx;
	for(int i=1;i<vp.size();i++){
		double prevleftx = leftx;
		double prevrightx = rightx;
		leftx = vp[i] - tm;
		if(leftx <prevrightx + D) leftx = prevrightx + D;
		rightx = leftx + D*(vv[i]-1);
		if(tm < rightx - vp[i]) return false;
	}
	return true;
}

int main(){
	int T;
	cin >> T;
	for(int i=0;i<T;i++){
		int C;
		double D;
		cin >> C >> D;
		vector <double> vp;
		vector <double> vv;
		for(int j=0;j<C;j++){
			double P,V;
			cin >> P >> V;
			vp.push_back(P);
			vv.push_back(V);
		}
		double Tmx = 1E10;
		double Tmin = 1E-9;
		double Tmid;
		for(int k=0;k<200;k++){
			Tmid = (Tmx + Tmin)/2.0;
			if(isFeasible(vp,vv,D,Tmid)){
				Tmx = Tmid;
			}
			else Tmin = Tmid;
		}
		cout <<fixed << setprecision(9) << "Case #" << i+1 << ": " << Tmid << endl;

	}
	system("pause");
	return 0;

}