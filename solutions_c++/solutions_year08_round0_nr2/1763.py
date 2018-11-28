#include <algorithm>
#include <vector>
#include <set>
#include <string>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <map>
#include <sstream>
#include <queue>

#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <cstring>

#define REP(i, n) for(int i=0;i<int(n);i++)
#define FOR(i, a, b) for(int i=(a);i<int(b);i++)
#define RFOR(i, b, a) for(int i=(b);i>int(a);i--)
#define foreach(it, c)  for(__typeof((c).begin()) it = (c).begin();it!=(c).end();++it)
#define ALL(x)   (x).begin(),(x).end()
#define SIZE(x)   (int)(x).size()
#define SORT(x) sort(ALL(x))
using namespace std;
#define VI vector<int>
#define VS vector<string>
#define PB push_back
#define ISS istringstream
#define OSS ostringstream
int T;
void takeit(vector<pair<int,int> > &A, vector<pair<int,int> > &B, int turn, int time){
	if( turn ){
		int ind = -1;
		REP(i, B.size()){
			if( B[i].first >= time ){
				if( ind == -1 ) ind = i;
				else if( B[i].second < B[ind].second ) ind = i;
			}
		}
		if( ind == -1 ) return;
		int fin = B[ind].second + T;
		B.erase(B.begin()+ind);
		takeit(A,B,1-turn,fin);
	}else{
		int ind = -1;
		REP(i, A.size()){
			if( A[i].first >= time ){
				if( ind == -1 ) ind = i;
				else if( A[i].second < A[ind].second ) ind = i;
			}
		}
		if( ind == -1 ) return;
		int fin = A[ind].second + T;
		A.erase(A.begin()+ind);
		takeit(A,B,1-turn,fin);
	}
}
int tonum(string s){
	return ((s[0]-'0')*10+(s[1]-'0'))*60 + ((s[3]-'0')*10+(s[4]-'0'));
}
int main(){
	int i,j ,k;
	int casos;
	cin >> casos;
	for(int h = 0 ; h < casos ; h ++ ){
		int NA, NB;
		cin >> T >> NA >> NB;
		vector<pair<int,int> > A, B;
		string s, t;
		REP(i, NA){
			cin >> s >> t;
			A.PB(make_pair(tonum(s), tonum(t)));
		}
		REP(i, NB){
			cin >> s >> t;
			B.PB(make_pair(tonum(s), tonum(t)));
		}
		sort(ALL(A));sort(ALL(B));
		int resa = 0, resb = 0;
		while( A.size() || B.size() ){
			if( (A.size()&&B.size()&&A[0].first<B[0].first)||(!B.size()) ){
				takeit(A,B,0,A[0].first);
				resa++;
			}else takeit(A,B,1,B[0].first), resb++;
		}
		printf("Case #%i: %i %i\n", h+1, resa, resb);
	}return 0;
}
