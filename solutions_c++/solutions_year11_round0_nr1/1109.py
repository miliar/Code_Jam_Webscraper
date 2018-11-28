/*
 * A.cpp
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


vector<int> goals0, goals1;
vector<pair<int,int> > goals;
int pos0,pos1, next, next0, next1;

bool estaenposicion(int robot){
	if(robot==0) return (pos0 ==goals[next].second);
	return (pos1 ==goals[next].second);
}
void acerca(int robot){
	if(robot==0){
		if(next0<goals0.size()){
			if(goals0[next0]>pos0) pos0++;
			else if(goals0[next0]<pos0) pos0--;
		}
	}else{
		if(next1<goals1.size()){
			if(goals1[next1]>pos1) pos1++;
			else if(goals1[next1]<pos1) pos1--;
		}
	}
}
void run1(int caso){
	int N;
	cin >> N;
	goals0.clear();goals1.clear();goals.clear();
	REP(i,N){
		char c;
		int val;
		cin >> c >> val;
		if(c=='O')  goals1.push_back(val);
		else goals0.push_back(val);
		goals.push_back(mp(c=='O',val));
	}

	next0 = 0, next1=0, next = 0;
	pos0=1, pos1=1;
	int sol=0;
	while(next < goals.size()){
		sol++;
		if(estaenposicion(goals[next].first)){
			if(goals[next].first==0) next0++;
			else next1++;
			acerca(goals[next].first==0?1:0);
			next++;
		} else {
			acerca(goals[next].first==0?1:0);
			acerca(goals[next].first);
		}

	}
	cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}
