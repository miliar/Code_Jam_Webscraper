#include <vector>
#include <string>
#include <map>
#include <iostream>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <set>
#include <numeric>

using namespace std;

/*Defines*/
#define SZ(A) (A).size()
#define ALL(A) (A).begin(), (A).end()
#define SORT(A) sort(ALL(A))
#define REP(I,N) for(int I=0 ; I<N ; I++)
#define PB push_back
#define sqr(A) ((A)*(A))

#define ISS istringstream
#define OSS ostringstream
#define INT_INF (0x7fffffff)
#define LL_INF (0x7fffffffffffffffLL)
#define MSG(A) cout << #A << " = " << (A) << endl

/*Types*/
typedef long long un64;
typedef unsigned long long s64;
typedef vector<int> vi;
typedef vector<vi> vii;


int main(){

	int T;
	cin >> T;
	for(int t=1 ; t<=T ; t++){

		int n;
		cin >> n;

		vii pl(n, vi(3,0));
		for(int i=0 ; i<n ; i++)
			REP(j,3) cin >> pl[i][j];

		cout <<"Case #"<<t<<": ";
		if(n == 1)
			printf("%.5f\n", (double)pl[0][2]);
		if(n==2)
			printf("%.5f\n", (double)max(pl[0][2],pl[1][2]));

		if(n== 3){
			double mn=9999999999999.;

			for(int i=0 ; i<3 ; i++){
				for(int j=i+1 ; j<3 ; j++){
					double c = sqrt(sqr(pl[i][0]-pl[j][0])+sqr(pl[i][1]-pl[j][1]));
					c = (c+pl[i][2]+pl[j][2])/2.;
					int k=0;
					if((i==0 && j==1) || (i==1 && j==0)) k=2;
					if((i==2 && j==0) || (i==0 && j==2)) k=1;
					if((i==2 && j==1) || (i==1 && j==2)) k=0;
					mn = min(mn, max(c, (double)pl[k][2]));
				}
			}
			printf("%.7f\n", mn);
		}

	}

	return 0;
}
