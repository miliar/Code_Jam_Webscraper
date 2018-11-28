#include <iostream>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <list>
#include <deque>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <utility>
#include <sstream>
#include <cstring>
#include <bitset>
using namespace std;

#define FALL(ii,vv) for (int (ii)=0; (ii)<(vv).size();(ii)++)
#define REP(i,b) for(int (i)=(0);(i)<(b);(i)++)
#define FUP(i,a,b) for(int (i)=(a); (i)<=(b); (i)++)
#define ALL(a) a.begin(), a.end()
#define PB push_back
#define MP make_pair

typedef vector<int> vi;
typedef long long ll;

bool b[1055][1055];
bool b1[1055][1055];

int main(){
	int test,X0,Y0,X1,Y1,n;
	scanf("%d",&test);
	REP(tN,test){
		scanf("%d",&n);
		REP(i,200) REP(j,200) b[i][j]=false;
		REP(i,n){
			scanf("%d %d %d %d",&X0,&Y0,&X1,&Y1);
			FUP(x,X0,X1) FUP(y,Y0,Y1) b[x][y]=true;
		}
		
		bool x,y;
		int res = 0;
		while(true){
			int ile = 0;
			REP(i,200) REP(j,200) ile+=b[i][j];
			if (ile==0){
				printf("Case #%d: %d\n",tN+1,res);
				break;
			}
			
			REP(i,199) REP(j,199){
				if (b[i][j]){
					x = false;
					y = false;
					
					if (i>0 && b[i-1][j]) x=true;
					if (j>0 && b[i][j-1]) y=true;
					b1[i][j]=(x||y);
				}
				else{
					x = false;
					y = false;
					
					if (i>0 && b[i-1][j]) x=true;
					if (j>0 && b[i][j-1]) y=true;
					b1[i][j]=(x&&y);
				}
			}
			
			REP(i,200) REP(j,200) b[i][j]=b1[i][j];
			res++;
		}
	}
	return 0;
}
