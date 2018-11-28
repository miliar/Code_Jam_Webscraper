#include <iostream>
#include <vector>

#define REP(i,n) for (int (i)=0; (i)<(n); (i)++)

using namespace std;

int C, D, N;
vector<char> v(1);
pair<pair<char, char>, char> trans[37];
pair<pair<char, int>, pair<char, int> > opps[29];

bool oppositable(char s) {
	bool b = false;
	REP(d,D) {
		if ((opps[d].first.first==s && opps[d].second.second) || 
			opps[d].second.first==s && opps[d].first.second){
				v.clear();
				REP(d2,D) {
					opps[d2].first.second = 0;
					opps[d2].second.second = 0;					
				}
				b = true;
				break;
			} else {
				if (opps[d].first.first==s) opps[d].first.second++;
				if (opps[d].second.first==s) opps[d].second.second++;
			} 
	}
	return b;
}

bool transformable(char s) {
	bool b = false;
	REP(c,C) {
		char l = v[v.size()-1];
		if ((s==trans[c].first.first && l==trans[c].first.second) ||
			(l==trans[c].first.first && s==trans[c].first.second)) {
				v.erase(v.end()-1);
				REP(d2,D) {
					if (opps[d2].first.first==l) opps[d2].first.second--;
					if (opps[d2].second.first==l) opps[d2].second.second--;
				}
				if (oppositable(trans[c].second)) {b=true;break;}
				v.push_back(trans[c].second);	
				c = 0;
				b = true;
			}
	}
	return b;
}

void printVector(int t) {
	if (v.size()==0) {printf("Case #%d: []\n", t); return;}
	printf("Case #%d: [%c",t,v[0]);
	for (int i = 1; i < v.size(); i++)
		printf(", %c", v[i]);
	printf("]\n");
}

int main(int argn, char* argv[])
{
	int T; cin >> T;
	REP(t,T) {
		cin >> C; 
		REP(c,C) {
			cin >> trans[c].first.first;
			cin >> trans[c].first.second;
			cin >> trans[c].second;
		}
		cin >> D;
		REP(d,D) {
			cin >> opps[d].first.first;
			cin >> opps[d].second.first;
			opps[d].first.second = 0;
			opps[d].second.second = 0;
		}
		cin >> N;
		v.clear();
		REP(n,N) {
			char s; cin >> s;
			if (!transformable(s) && !oppositable(s)) v.push_back(s);
		}
		printVector(t+1);
	}
	return 0;
}