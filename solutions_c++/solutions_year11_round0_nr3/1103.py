/*
 * C.cpp
 *
 *  Created on: May 6, 2011
 *      Author: elvitucho
 */

#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>

using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

typedef pair < int, int > pii;
typedef long long LL;



void run1(int caso){
	int N ;
	cin >> N;
	vector<int> v;
	LL tot = 0,sum=0;
	int mini = INT_MAX;
	REP(i,N){
		int wi;
		cin >> wi;
		v.push_back(wi);
		tot ^= wi;
		mini = min(mini,wi);
		sum+=wi;
	}
	if(tot==0){
		LL sol = sum-mini;
		cout << "Case #"<<caso<<": "<< sol<<endl;
	}else
		cout << "Case #"<<caso<<": "<< "NO"<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}
