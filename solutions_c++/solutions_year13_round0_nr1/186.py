//

#include <cstdio>
#include <algorithm>
#include <cstring>
#include <utility>
#include <vector>
#include <queue>
#include <stack>
#include <map>
#include <string>
#include <set>
#include <cmath>
#include <iostream>
#include <ctime>
#include <cassert>

using namespace std;

#define db(x) cout << #x " == " << x << endl
//#define _ << ", " <<
#define Fr(a,b,c) for( int a = b ; a < c ; ++a )
#define CL(a,b) memset(a,b,sizeof(a))
typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> pii;
typedef vector<pair<int,int> > vpii;
typedef map<int,int> mii;
#define F first
#define S second
#define MP make_pair
#define PB push_back
#define INF 0x3f3f3f3f
#define LINF 0x3f3f3f3f3f3f3f3fLL
#define ULMAX 0xffffffffffffffffULL
#define y1 Y1

int t,_=1;
char gr[10][10];

int main() {
//	cin.sync_with_stdio(false);
	for(scanf("%d",&t);t--;){
		Fr(i,0,4) scanf("%s",gr[i]);
		bool x=0, o=0, ac=1;
		Fr(i,0,4) Fr(j,0,4) ac &= gr[i][j]!='.';
		Fr(i,0,4){
			bool bla1=1, bla2=1;
			Fr(j,0,4) bla1 &= (gr[i][j]=='X' || gr[i][j]=='T'), bla2 &= (gr[i][j]=='O' || gr[i][j]=='T');
			x|=bla1, o|=bla2;
			bla1=1, bla2=1;
			Fr(j,0,4) bla1 &= (gr[j][i]=='X' || gr[j][i]=='T'), bla2 &= (gr[j][i]=='O' || gr[j][i]=='T');
			x|=bla1, o|=bla2;
		}
		bool bla1=1, bla2=1;
		Fr(j,0,4) bla1 &= (gr[j][j]=='X' || gr[j][j]=='T'), bla2 &= (gr[j][j]=='O' || gr[j][j]=='T');
		x|=bla1, o|=bla2;
		bla1=1, bla2=1;
		Fr(j,0,4) bla1 &= (gr[j][3-j]=='X' || gr[j][3-j]=='T'), bla2 &= (gr[j][3-j]=='O' || gr[j][3-j]=='T');
		x|=bla1, o|=bla2;
		
		printf("Case #%d: ",_++);
		if(x) puts("X won");
		else if(o) puts("O won");
		else if(ac) puts("Draw");
		else puts("Game has not completed");
	}
	return 0;
}
