#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cmath>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <memory>
#define sz size()
#define mp make_pair
#define pb push_back
#define vi vector<int>
#define fu(i,n) for(int i=0; i<(n); i++)
#define ALL(a) (a).begin(),(a).end()
#define cl(a,co) memset(a,co,sizeof a)
#define un(a) a.erase( unique(ALL(a)), a.end() )
typedef long long ll;
//istringstream is(s); is >> a;

using namespace std;

int ileTestow, mx, my, pole;

int main(){

	scanf("%d",&ileTestow);

	for(int q=1; q<=ileTestow; q++){
		cin >> mx >> my >> pole;		
		
		//fu(x1,mx+1) fu(y1,my+1) fu(x2,mx+1) fu(y2,my+1) fu(x3,mx+1) fu(y3,my+1){
		//for(int x1=0; x1<=mx; x1++) for(int y1=0; y1<=my; y1++)
		int x1=0,  y1 = 0;
			for(int x2=0; x2<=mx; x2++) for(int y2=0; y2<=my; y2++)
				for(int x3=0; x3<=mx; x3++) for(int y3=0; y3<=my; y3++){
				int tmp = abs(x1*y2+x2*y3+x3*y1 - x3*y2-x1*y3-x2*y1);
				if( tmp == pole ){
					printf("Case #%d: %d %d %d %d %d %d\n",q,x1,y1,x2,y2,x3,y3);
					goto hell;
				}
		}

		printf("Case #%d: IMPOSSIBLE\n",q);
		hell: ;
	}

	return 0;
}
