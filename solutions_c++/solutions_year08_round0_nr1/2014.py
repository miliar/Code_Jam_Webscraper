#include <iostream>
#include <map>

#define REP(i,n) for(typeof(n) _n=n, i=0;i<_n;++i)
#define FOREACH(i,x) for(typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define INFTY 100000

using namespace std;

map<string,int> best;

int findMin(){
	int answer = INFTY;
	FOREACH(site,best)
		answer = min(answer,site->second);
	return answer;
}

void runCase(){
	int engNo;
	cin >> engNo;
	string s;
	getline(cin,s);
	best.clear();
	REP(i,engNo){
		getline(cin,s);
		best[s] = 0;
	}
	int qNo;
	cin >> qNo;
	getline(cin,s);
	REP(i,qNo){
		int m = findMin();
		getline(cin,s);
		FOREACH(site,best)
			if (site->second > m+1)
				best[site->first] = m+1;
		best[s] = INFTY;
	}
	cout << findMin() << endl;
}

int main(){
	int cases;
	cin >> cases;
	string s;
	getline(cin,s);
	REP(i,cases){
		cout << "Case #" << i+1 << ": ";
		runCase();
	}
	return 0;
}
