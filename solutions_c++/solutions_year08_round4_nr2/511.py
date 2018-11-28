#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
typedef vector<int> vi;
typedef vector<string> vs;
typedef stringstream sst;
#define fri(a,i) for(typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)
#define fr(i,n) for(int i=0; i<(int)(n); i++)
#define zer(a) memset((a),0,sizeof(a));
#define all(a) (a).begin(), (a).end()
#define pb push_back

int area(int x1, int y1, int x2, int y2){
	int ret;
	ret=x2*y1-x1*y2;
	if(ret<0) ret=-ret;
	return ret;

}

int main(){
    int N;
	cin>>N;
    for(int l=1; l<=N; l++){
		int n,m,a;
		cin>>n>>m>>a;
		int X1=-1,Y1,X2,Y2,X3,Y3;
		for(int x1=0; x1<=n; x1++)
		  for(int y1=0; y1<=m; y1++)
		    for(int x2=0; x2<=n; x2++)
			  for(int y2=0; y2<=m; y2++)
			    if(area(x1,y1,x2,y2)==a) {X1=x1;Y1=y1;X2=x2;Y2=y2; X3=0; Y3=0;}
		sst ss;
		if(X1==-1) ss<<"IMPOSSIBLE";
		else ss<<X1<<" "<<Y1<<" "<<X2<<" "<<Y2<<" "<<X3<<" "<<Y3;
		string ret=ss.str();
	    cout<<"Case #"<<l<<": "<<ret<<endl;
	}
}
