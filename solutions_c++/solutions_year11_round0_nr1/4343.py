#include <cstdio>
#include <cmath>
#include <iostream>
#include <algorithm>
#include <vector>
#include <cstdlib>
#include <queue>
#include <set>
#include <cstring>
#include <sstream>
#include <cassert>
#include <map>
#include <stack>

#define FOR(I,A,B) for(int I=(A);I<(B);I++)
#define REP(I,N) FOR(I,0,N)
#define ALL(A) (A).begin(),(A).end()

#define SQR(x) ((x)*(x))
#define PB(x) push_back(x)

#define PI (acos(-1.0))

using namespace std;

typedef vector<int> VI;
typedef vector< vector<int> > VVI;
int main(){
	freopen("A-large.in","rt",stdin);
	freopen("A-large.out","wt",stdout);
	int t;
	scanf("%d\n",&t);
	int k = 1;
	while(t-->0){
		string temp;
		getline(cin,temp);
		stringstream  sst(temp);
		int n;
		sst>>n;
		vector<int> O,B;
		for(int i = 0;i < n;i++){
			string label;
			int pos;
			sst>>label>>pos;
			if(label=="O")
				O.PB(pos);
			if(label=="B")
				B.PB(pos);
		}
		int time = 0;
		int o = 1;
		int b = 1;
		stringstream sst2(temp);
		sst2>>n;
		int p = 0,q = 0;
		for(int i = 0; i < n;i++){
			string label;
			int pos;
			sst2>>label>>pos;
			if( label == "O"){
				int lh = min(o,O[p]);
				int rh = max(o,O[p]);
				for(int j = lh;j < rh;j++){
					time++;
					if(q < B.size()){
						if( b < B[q])b++;
						else if( b > B[q]) b--;
					}
				}
				if(q < B.size()){
					if( b < B[q])b++;
					else if(b >B[q])b--;
				}
				time++;
				o = O[p++];
			}
			if( label == "B"){
				int lh = min(b,B[q]);
				int rh = max(b,B[q]);
				for(int j = lh;j < rh;j++){
					time++;
					if(p < O.size()){
						if( o < O[p])o++;
						else if( o > O[p]) o--;
					}
				}
				if(p < O.size()){
					if( o < O[p])o++;
					else if( o > O[p]) o--;
				}
				time++;
				b = B[q++];
			}
		}
		printf("Case #%d: %d\n",k++,time);
	}
	return 0;
}

