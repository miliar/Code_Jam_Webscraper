/*
 * GCJ2012QR2.cpp
 *
 *  Created on: 2012-4-14
 *      Author: MacTavish
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
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
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>
using namespace std;
#define REP(i,n) for(int i=0;i<(n);++i)
#define FOR(i,l,h) for(int i=(l);i<=(h);++i)
#define FORD(i,h,l) for(int i=(h);i>=(l);--i)
#define CLR(x,val) memset((x),val,sizeof((x)))
#define swap(a,b,t) ((t)=(a),(a)=(b),(b)=(t))
#define sqr(x) ((x)*(x))
#define sgn(a) (a>eps?1:(a<-eps?-1:0))
#define SZ(a) (int((a).size()))
template<class T>inline T MAX(T a,T b){return a>b?a:b;}
template<class T>inline T MIN(T a,T b){return a<b?a:b;}
template<class T>inline T GCD(T a,T b){return b==0?a:GCD(b,a%b);}
inline int rint() {int x;scanf("%d",&x);return x;}
typedef long long i64;
typedef unsigned long long u64;
const double pi = acos(-1.0);
const double eps = 1e-10;
const int inf = 0x3fffffff;

int t;
int main(int argc,char *argv[]){
	int test=rint();
	int caser=0;
	while(test--){
		int n=rint(),s=rint(),p=rint();
		int ans=0;
		REP(i,n){
			t=rint();
			int ss=t/3;
			if(ss>=p){
				++ans;
			}else if(t>=p){
				t-=p;
				int a,b,tp;
				b=p-1;
				a=t-b;
				tp=a+b;
				a=MIN(a,b);
				b=tp-a;
				if(p-a<2||((p-a==2)&&s)){
					++ans;
					if(p-a==2)s--;
				}else{
					b=p;a=t-b;
					tp=a+b;
					a=MIN(a,b);
					b=tp-a;
					if(p-a<2||((p-a==2)&&s)){
						++ans;
						if(p-a==2)s--;
					}else{
						b=p-2;a=t-b;
						tp=a+b;
						a=MIN(a,b);
						b=tp-a;
						if(p-a<2||((p-a==2)&&s)){
							++ans;
							if(p-a==2)s--;
						}
					}
				}
			}

		}
		printf("Case #%d: %d\n",++caser,ans);
	}return 0;
}

