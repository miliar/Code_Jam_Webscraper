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

vector<int> arrivals[2];
vector<int> departures[2];

int parse(string s){
	int t = 0;
	t = 10*(s[0]-'0')+(s[1]-'0');
	t = 60*t + 10*(s[3]-'0')+(s[4]-'0');
}

void runCase(){
	string s;
	int TO;
	cin >> TO;
	int aNo, bNo;
	cin >> aNo >> bNo;
	getline(cin,s);

	REP(i,2){ arrivals[i].clear(); departures[i].clear();}

	REP(i,aNo){
		getline(cin,s);
		departures[0].push_back(parse(s.substr(0,5)));
		arrivals[1].push_back(parse(s.substr(6,5))+TO);
	}

	REP(i,bNo){
		getline(cin,s);
		departures[1].push_back(parse(s.substr(0,5)));
		arrivals[0].push_back(parse(s.substr(6,5))+TO);
	}

	REP(i,2){ sort(ALL(arrivals[i])); sort(ALL(departures[i])); arrivals[i].push_back(INFTY);}

	REP(i,2){
		int j = 0;
		int answer = 0;
		FOREACH(t,departures[i]){
			if (arrivals[i][j] > (*t))
				answer++;
			else
				j++;
		}
		cout << " " << answer;
	}
	cout << endl;
}

int main(){
	int cases;
	cin >> cases;
	string s;
	getline(cin,s);
	REP(i,cases){
		cout << "Case #" << i+1 << ":";
		runCase();
	}
	return 0;
}
