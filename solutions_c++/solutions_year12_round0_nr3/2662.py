//============================================================================
// Name        : Recycled.cpp
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
	int T;
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	scanf ("%d",&T);
	set<pair<int,int> >st;
	REP(cases,T){
		int A,B;
		st.clear();
		scanf ("%d %d",&A,&B);
		int ten(1);
		int tmp(A);
		int cnt(0);
		while (tmp)ten*=10,tmp/=10,++cnt;
		ten/=10;
		FOR(i,A,B){
			tmp=i;
			//printf("%d ",i);
			REP(j,cnt){
				tmp=tmp%10*ten+tmp/10;
				//printf("%d ",tmp);
				if (tmp>i&&tmp>=A&&tmp<=B){
					st.insert(MP(i,tmp));
					//printf("%d %d\n",i,tmp);
				}
			}
			//puts("");
		}
		printf("Case #%d: %d\n",cases+1,(int)st.size());
	}
	return 0;
}
