//============================================================================
// Name        : Dancing.cpp
// Author      : alpc92
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define PB push_back
#define MP make_pair
#define inf 0x3fffffff
#define REP(iterator,upperbound) for(int iterator(0);iterator<(upperbound);++iterator)
#define FOR(iterator,lowerbound,upperbound) for(int iterator(lowerbound);iterator<=(upperbound);++iterator)
#define FORD(iterator,upperbound,lowerbound) for(int iterator(upperbound);iterator>=(lowerbound);--iterator)
#define FORIT(iter,STL) for (typeof(STL.begin()) iter(STL.begin());iter!=STL.end();++iter)
#define SIZE(STL) ((int)STL.size())
#define CLEAR(STL) (STL.clear())
#define CLEAR0(array) memset(array,0,sizeof(array))
#define CLEAR1(array) memset(array,-1,sizeof(array))
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int, int> PII;
#define MAXLOOP 100
#define WORKERNUM 10
#define UPNUM 4
#define DOWNNUM 2
#define PASSWAY 1
template<class T>
inline void chkmax(T &a, T b) {
	if (a < b)
		a = b;
}
template<class T>
inline void chkmin(T &a, T b) {
	if (a > b)
		a = b;
}
int main(){
	int T,N,S,P;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf("%d",&T);
	REP(cases,T){
		scanf ("%d %d %d",&N,&S,&P);
		int t,ans(0);
		REP(i,N){
			scanf ("%d",&t);
			int tmp(t/3);
			if (t%3==0){
				if (tmp>=P){
					++ans;
					//printf("%d %d %d\n",tmp,tmp,tmp);
				}
				else if (tmp+1>=P&&tmp-1>=0&&S>0){
					++ans;
					--S;
					//printf("%d %d %d\n",tmp-1,tmp,tmp+1);
				}
			}else if (t%3==1){
				if (tmp+1>=P){
					++ans;
					//printf("%d %d %d\n",tmp,tmp,tmp+1);
				}
			}else if (t%3==2){
				if (tmp+1>=P){
					++ans;
					//printf("%d %d %d\n",tmp,tmp+1,tmp+1);
				}
				else if (tmp+2>=P&&S>0){
					++ans;
					--S;
					//printf("%d %d %d\n",tmp,tmp,tmp+2);
				}
			}
		}
		printf("Case #%d: %d\n",cases+1,ans);
	}
	return 0;
}
