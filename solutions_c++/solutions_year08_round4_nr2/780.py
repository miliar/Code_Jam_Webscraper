#pragma comment(linker,"/STACK:256000000")

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>

#define FOR(i,a,b) for (int i = (int)a; i < (int)b; ++i)
#define REP(i,a) FOR(i,0,a)
#define ALL(a) a.begin(),a.end()
#define SIZE(a) (int)((a).size())
#define PB push_back
#define FILL(a) memset(&a,0,sizeof(a))
typedef long long LL;

using namespace std;

int kos(int x1,int y1,int x2,int y2){
	return x1*y2-x2*y1;
}

int main(){
	freopen("b.in","r",stdin);
	freopen("b.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		int n,m,a;
		scanf("%d%d%d",&n,&m,&a);
		int resx1=-1,resx2,resx3,resy1,resy2,resy3;
		bool fl=false;
		int x1=0,y1=0;
				FOR(x2,x1,n+1){
					if (fl) break;
					REP(y2,m+1){
						LL pl=kos(x1,y1,x2-x1,y2-y1);
						if (fl) break;
						FOR(x3,x2,n+1){
							if (fl) break;
							REP(y3,m+1){
								if (fl) break;
								pl+=kos(x2,y2,x3-x2,y3-y2);
								pl+=kos(x3,y3,x1-x3,y1-y3);
								int cur=pl;
								if (cur<0) cur=-cur;
								if (cur==a){
									resx1=x1;
									resx2=x2;
									resx3=x3;
									resy1=y1;
									resy2=y2;
									resy3=y3;
									fl=true;
								}
								pl-=kos(x2,y2,x3-x2,y3-y2);
								pl-=kos(x3,y3,x1-x3,y1-y3);
							}
						}
					}
				}
		cerr<<it+1<<endl;
		printf("Case #%d: ",it+1);
		if (resx1==-1) puts("IMPOSSIBLE");
		else printf("%d %d %d %d %d %d\n",resx1,resy1,resx2,resy2,resx3,resy3);
	}
}