#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

const int nmax = 300;

struct trip{
	int start,end,type;
};


trip tt[nmax];

bool cmp(trip a,trip b){
	return a.start < b.start;
}

int num(string a){
	return ((a[0]-'0') * 10 + a[1]-'0') * 60 + ((a[3]-'0') * 10 + a[4]-'0');
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin >> test;

	for (int te = 0;te < test; ++te){
		int t,na,nb;
		int k = 0;
		vector <int> aval[2]; // aval trains)

		cin >> t >> na >> nb;
		for (int i = 0;i < na; ++i){
			string st,en;
			cin >> st >> en;
			tt[k].start = num(st);
			tt[k].end = num(en);
			tt[k].type = 0;
			++k;
		}

		for (int i = 0;i < nb; ++i){
			string st,en;
			cin >> st >> en;
			tt[k].start = num(st);
			tt[k].end = num(en);
			tt[k].type = 1;
			++k;
		}

		sort(tt,tt+k,cmp);

		int ans[2] = {0,0};

		for (int i = 0;i < k; ++i){
			if (aval[tt[i].type].size() > 0 && aval[tt[i].type][0] <= tt[i].start) 
				aval[tt[i].type].erase(aval[tt[i].type].begin());
			else 
				ans[tt[i].type]++;

			aval[(tt[i].type+1)%2].push_back(tt[i].end+t);
			sort(aval[(tt[i].type+1)%2].begin(),aval[(tt[i].type+1)%2].end());
		}
		cout << "Case #" << te+ 1 << ": " << ans[0] << " " <<ans[1] << endl;
	}

	return 0;
}