#include <map>
#include <cmath>
#include <vector>
#include <numeric>
#include <sstream>
#include <iostream>
using namespace std ;

#define PI 3.14159265358
#define pb push_back
#define LOOP(i,a,b) for (int i=a; i<b; i++)
#define FOR(i,n) LOOP(i,0,n)
#define REP(i,n) LOOP(i,1,n)
#define fill(f,n,v) FOR(i,n) f[i]=v
#define sz(a) (int)a.size()

class Train{
public:
	int st, en;
	char type;
	
	friend bool operator < (Train a, Train b) {
		if(a.st==b.st) return a.en < b.en;
		return a.st < b.st;
	}
	
	bool canBeConnectedBy(Train a, int T) {
		return type!=a.type && a.en+T <= st;
	}
};

int main() {
	//vars
	int N, T, nA, nB, rA, rB, M;
	bool used[101];
	Train trains[202];
	string s1, s2;
	
	cin >> N;
	FOR(n,N) {
		//input
		cin >> T >> nA >> nB;
		M = nA + nB;
		FOR(i,M) {
			cin >> s1 >> s2;
			if(i<nA) trains[i].type='A';
			else trains[i].type='B';
			
			trains[i].st = ((s1[0]-'0')*10 + (s1[1]-'0'))*60 +((s1[3]-'0')*10 + (s1[4]-'0'));
			trains[i].en = ((s2[0]-'0')*10 + (s2[1]-'0'))*60 +((s2[3]-'0')*10 + (s2[4]-'0'));
		}
		
		
		//process
		rA = rB = 0;
		sort(trains, trains+M);
		FOR(i,M) used[i] = false;
		
		//FOR(i,M) cout << trains[i].type << " " << trains[i].st << " " << trains[i].en << endl;
					
		FOR(i,M) {
			bool newTrain = true;
			FOR(j,i) if(!used[j]) if(trains[i].canBeConnectedBy(trains[j], T)) {
				newTrain = false;
				used[j] = true;
				break;
			}
			if(newTrain && trains[i].type=='A') rA++;
			else if(newTrain && trains[i].type=='B') rB++;
		}
		
		//output
		cout << "Case #" << (n+1) << ": " << rA << " " << rB << endl; 
	}
	return 0;
}