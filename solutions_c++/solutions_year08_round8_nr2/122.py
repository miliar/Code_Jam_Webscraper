#include<iostream>
#include<algorithm>
#include<vector>
#include<set>
#include<map>
#include<deque>
#include<string>
#include<cctype>
#include<cmath>
#include<sstream>
#include<numeric>
#include<complex>
#include<queue>
using namespace std;

int setBit(int num, int index, int value){return value ? (num|(1<<index)) : (num&(~(1<<index)));}
int getBit(int num, int index){return (num >> index) & 1 ? 1 : 0;}

int N;
struct offer{
	string c;
	int start, end;
	bool operator<(const offer& o)const{
		return start < o.start || (start==o.start && end > o.end);
	}
};
vector<offer> v;

bool check(vector<offer>& o){

	set<string> c;
	int s = 0, i;
	for(i = 0 ; i < o.size() ; i++){
		if(o[i].start > s+1)break;
		c.insert(o[i].c);
		s = max(s, o[i].end);
	}
	return c.size() <= 3 && s == 10000;
}

int main(){


	//freopen("1.in", "rt", stdin);
	//freopen("B-small-attempt0.in", "rt", stdin);freopen("B-small-attempt0.out", "wt", stdout);
	freopen("B-small-attempt1.in", "rt", stdin);freopen("B-small-attempt1.out", "wt", stdout);
	//freopen("B-large.in", "rt", stdin);freopen("B-large.out", "wt", stdout);

	int tt; cin >> tt;
	for(int t = 0 ; t < tt ; t++){

		v.clear();
		cin >> N;
		int i;
		for(i = 0 ; i < N ; i++){
			string str; int s, e;
			cin >> str >> s >> e;
			offer o = {str, s, e};
			v.push_back(o);
		}

		int best = -1;
		for(i = 0 ; i < (1<<N) ; i++){
			vector<offer> o;
			for(int j = 0 ; j < N ; j++)
				if(getBit(i,j))o.push_back(v[j]);
			sort(o.begin(), o.end());
			if(check(o))
				if(best == -1 || o.size() < best)
					best = o.size();
		}

		cout << "Case #" << t+1 << ": ";
		if(best == -1)
			cout << "IMPOSSIBLE" << endl;
		else
			cout << best << endl;
	}

	return 0;
}
