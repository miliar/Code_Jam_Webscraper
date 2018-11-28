#include <iostream>
#include <map>
#include <vector>
#include <string>
#include <algorithm>

#define REP(i,n) for(typeof(n) _n=n, i=0;i<_n;++i)
#define FOREACH(i,x) for(typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define ALL(x) (x).begin(),(x).end()
#define INFTY 1000000

using namespace std;

long long solveCase(){
	int deck;
	cin >> deck;
	int n; cin >> n;
	vector<int> pos;
	REP(i,n){
		int p; 
		cin >> p;
		pos.push_back(p);	
	}
	
	vector<int> order(deck,-1);
	int p = deck-1;
	for(int c = 1; c <= deck; c++){
			REP(i,c)
				do { p = (p+1)%deck; } while (order[p] != -1);
			order[p] = c;
			//REP(j,deck) cout << order[j] << " " ;
			//cout << endl;
	}

	REP(i,pos.size())
		cout << " " << order[pos[i]-1];
}	

int main(){
	int cases;
	cin >> cases;
	REP(i,cases){
		cout << "Case #" << i+1 << ":";
		solveCase();
		cout << endl;
	}		
	return 0;
}
