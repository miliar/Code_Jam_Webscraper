#include <math.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <sstream>
#include <iomanip>

using namespace std;
#define x first
#define y second.first
#define r second.second
#define INF 1000000

typedef pair<double,double> PII;
typedef pair<double,PII> PIII;

double dist(PIII p1,PIII p2){
	return sqrt((p1.x-p2.x)*(p1.x-p2.x) + (p1.y-p2.y)*(p1.y-p2.y));
}

int main(){
	int Tc;
	cin >> Tc;
	for(int tc=1;tc<=Tc;tc++){
		int N;
		cin >> N;
		
		vector<PIII> p(N);
		for(int i=0;i<N;i++) cin >> p[i].x >> p[i].y >> p[i].r;

		cout << "Case #" << tc << ": ";
		if(N == 1) cout << fixed << setprecision(6) << p[0].r << endl;
		else if(N==2) cout << fixed << setprecision(6) << max(p[0].r, p[1].r) << endl;
		else if(N==3){
			double R=INF;
			for(int i=0;i<3;i++) for(int j=0;j<3;j++) for(int k=0;k<3;k++) if(i!=j && i!=k && j!=k){
				double pR = p[k].r;
				pR = max(pR, (dist(p[i],p[j]) + p[i].r + p[j].r)/2);
				R = min(R, pR);
			}
			cout << fixed << setprecision(6) << R << endl;
		}
	}
}




















