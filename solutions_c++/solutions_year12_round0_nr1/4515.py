/*
 * GCJ2012QR1.cpp
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
int R[30];
char Q1[190]="ejp mysljylc kd kxveddknmc re jsicpdrysi";
char A1[190]="our language is impossible to understand";
char Q2[]="rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
char A2[]="there are twenty six factorial possibilities";
char Q3[]="de kr kd eoya kw aej tysr re ujdr lkgc jv";
char A3[]="so it is okay if you want to just give up";
char arr[30];
char str[200];
int main(int argc,char *argv[]){
	arr['z'-'a']='q';
	arr['q'-'a']='z';
	for(int i=0;i<strlen(Q1);++i)if(Q1[i]!=32){
		arr[Q1[i]-'a']=A1[i];
	}
	for(int i=0;i<strlen(Q2);++i)if(Q2[i]!=32){
		arr[Q2[i]-'a']=A2[i];
	}
	for(int i=0;i<strlen(Q3);++i)if(Q3[i]!=32){
		arr[Q3[i]-'a']=A3[i];
	}
//	for(int i=0;i<30;++i)printf("%c %c\n",i+'a',arr[i]);
	int test=rint();
	scanf("%*c");
	int caser=0;
	while(test--){
		gets(str);
		REP(i,strlen(str))if(str[i]!=32){
			str[i]=arr[str[i]-'a'];
		}
		printf("Case #%d: ",++caser);
		puts(str);
	}
	return 0;
}
