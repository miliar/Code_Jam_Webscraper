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

bool iseq(LL x1,LL y1,LL x2,LL y2){
	return x1==x2&&y1==y2;
}

LL getn(LL x,LL y){
	return (x%3)*3+(y%3);
}

int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	int tc;
	scanf("%d",&tc);
	REP(it,tc){
		LL n, A, B, C, D, x0, y0, M;
		cin>>n>>A>>B>>C>>D>>x0>>y0>>M;
		LL col[9];
		FILL(col);
		col[getn(x0,y0)]++;
		FOR(i,1,n){
			x0=(A * x0 + B) % M;
			y0=(C * y0 + D) % M;
			col[getn(x0,y0)]++;
		}
		LL res=0;
		REP(x1,3){
			REP(y1,3){
				REP(x2,3){
					REP(y2,3){
						REP(x3,3){
							REP(y3,3){
								if ((x1+x2+x3)%3==0&&(y1+y2+y3)%3==0){
									LL umn1=col[getn(x1,y1)];
									LL umn2;
									if (iseq(x1,y1,x2,y2)) umn2=max(col[getn(x2,y2)]-1,0LL);
									else umn2=col[getn(x2,y2)];
									LL umn3;
									if (iseq(x2,y2,x3,y3)){
										if (iseq(x1,y1,x3,y3)) umn3=max(col[getn(x3,y3)]-2,0LL);
										else umn3=max(col[getn(x3,y3)]-1,0LL);
									}
									else{
										if (iseq(x1,y1,x3,y3)) umn3=max(col[getn(x3,y3)]-1,0LL);
										else umn3=col[getn(x3,y3)];
									}
									res+=umn1*umn2*umn3;
								}
							}
						}
					}
				}
			}
		}
		res/=6;
		printf("Case #%d: %I64d\n",it+1,res);
	}
}