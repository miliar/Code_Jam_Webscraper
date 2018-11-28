#include<cstdio>
#include<algorithm>
#include<iostream>
#include<sstream>
#include<string>
#include<vector>
#include<set>
#include<map>
#include<numeric>
#include<cmath>
#include<stdio.h>
#include<stdlib.h>
#include<math.h>
#include <ctype.h>

using namespace std;

typedef vector<int> vi;
typedef unsigned long long uint64;
typedef long long int64;

#define FOR(i,a,b) for(int i=(a),_b=(b);i<=_b;i++)
#define REP(i,n) FOR(i,0,(n)-1)
#define FORD(i,a,b) for(int i=(a),_b=(b);i>=_b;i--)
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)

#define ALL(x) (x).begin(),(x).end()
#define SORT(x) sort(ALL(x))
#define REVERSE(x) reverse(all(x))
#define CLEAR(x,c) memset(x,c,sizeof(x)) 



int main() {

	
	int64 C;
	cin >> C;

	double Mx, My, Mz, Mvx, Mvy, Mvz;
	int X, Y, Z, Vx, Vy, Vz;
	double Tmin, Xmin, Ymin, Zmin, Dmin;

	FOR(c,1,C){

		int N ;
		cin >> N;

		Mx = My = Mz = Mvx = Mvy = Mvz = 0;

		for (int i=0; i<N; i++){
			cin >> X >> Y >> Z >> Vx >> Vy >> Vz;

			Mx += X;
			My += Y;
			Mz += Z;
			Mvx += Vx;
			Mvy += Vy;
			Mvz += Vz;
		}

		Mx /= N; My /= N; Mz /= N;
		Mvx /= N; Mvy /= N; Mvz /= N;

		double Mvel = Mvx*Mvx + Mvy*Mvy + Mvz*Mvz;

		if (Mvel){
			Tmin = (-1)*(Mx*Mvx + My*Mvy + Mz*Mvz) / Mvel;
			if (Tmin<0) Tmin = 0;
		}
		else {
			Tmin = 0;
		}

		

		Xmin = Mx + Mvx*Tmin;
		Ymin = My + Mvy*Tmin;
		Zmin = Mz + Mvz*Tmin;
		Dmin = sqrt(Xmin*Xmin + Ymin*Ymin + Zmin*Zmin);
		
		printf("Case #%d: %.8f %.8f\n",c,Dmin, Tmin);
		//cout <<"Case #"<<c<<": "<< cnt <<endl;
	}
		
	return 0;
}
