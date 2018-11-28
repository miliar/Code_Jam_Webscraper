#include <iostream>
#include <set>
#include <vector>
#include <algorithm>
#include <cmath>
#include <vector>
#include <cstring>
#include <map>
#include <queue>
#include <string>
#include <sstream>

using namespace std;

#define FOR(i,a,b) for (int (i)=(a);(i)<(b);++(i))
#define FORE(i,a,b) for (int (i)=(a);(i)<=(b);++(i))
#define FOREACH(it,v) for (typeof((v).begin()) it=(v).begin();(it)!=(v).end();++(it))
#define ALL(v) v.begin(),v.end()
#define MSET(v,x) memset((v),(x),sizeof((v)))

typedef double D;
typedef pair<int,int> PII;
typedef pair<double,double> PDD;
typedef set<int> SI;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<double> VD;
typedef map<int,int> MII;
typedef long long ll;
typedef vector<PII> VP;
typedef queue<PII> QP;

VVI world;
VVI world2;

int main () {
	int C;
	cin >> C;
	FORE(t,1,C) {
		world=VVI(100,VI(100,0));
		int R;
		cin >> R;
		if (R==0) {
			cout << "Case #"<<t<<": "<<0<<endl;
			break;
		}
		FOR(k,0,R) {
			int x1,x2,y1,y2;
			cin >> x1 >> y1 >> x2 >> y2;
			x1--;y1--;x2--;y2--;
			FORE(i,x1,x2) {
				FORE (j,y1,y2) {
					world[i][j]=1;
				}
			}
		}
		world2=world;
		int live;
		for (live=1;;++live) {
			bool someone=false;
			FOR (i,0,100) {
				FOR (j,0,100) {
					if (i && j && world[i-1][j] && world[i][j-1]) world2[i][j]=1;
					else if ((i && world[i-1][j]) || (j&&world[i][j-1]));
					else world2[i][j]=0;
					someone|=world2[i][j];
				}
			}
			if (!someone) break;
			swap(world,world2);
		}
		cout << "Case #"<<t<<": "<<live<<endl;
	}
}
