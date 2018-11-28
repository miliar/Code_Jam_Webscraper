#include <fstream>
#include <cmath>
#include <string>
#include <map>
#include <vector>
#include <set>
#include <cstdlib>
#include <algorithm>
#define forn(i,n) for(int i = 0; i < n; i++)
#define lng long long
#define Uint unsigned
using namespace std;
#ifdef ___ASDASD___
	ifstream cin("input.txt");
	ofstream cout("output.txt");
#endif
#ifndef ___ASDASD___
#include <iostream>
#endif
lng f(lng y){
	return 0ll;
}
//////
//////
///////
///////

int main() {
	int t;
	cin>>t;
	forn(c,t){
		int r,k,n;
		cin>>r>>k>>n;
		vector<int> groups(n);
		vector<bool> starthere(n);
		vector< pair<int,int> > way;
		forn(i,n){
			cin>>groups[i];
		}
		//запилим порядок прохождения
		int round = 0;
		int firstround = 0;
		lng roundcost = 0;
		lng firstroundcost = 0;
		int j = 0, g = 0;
		while(!starthere[j]){
			way.push_back(make_pair(j,0));
			starthere[j] = true;
			int gr = groups[j];
			int e = j;
			if(j < n - 1)
				++j;
			else j = 0;
			while(gr + groups[j] <= k && j != e){
				gr += groups[j];
				if(j < n - 1)
					++j;
				else j = 0;
			}
			round++;
			roundcost += gr;
			way[g++].second = gr;
		}
		//вычислим как далеко до первого круга
		for(g = 0; way[g].first != j; g++){
			firstroundcost+=way[g].second;
			firstround++;
		}
		round -= firstround;
		roundcost -= firstroundcost;
		//вычислим прибыль
		lng tc = 0;
		if(firstround < r){
			tc+=firstroundcost;
			r-=firstround;
		} else {
			forn(i,r){
				tc+=way[i].second;
			}
			
			cout<<"Case #"<<(c + 1)<<": "<<tc<<endl;
			continue;
		}
		int times = r / round;
		tc += roundcost * times;
		r -= times * round;
		int i = 0;
		for(int i = 0; i < r; i++){	
			int e = (i + g < way.size())?
				(i + g):
				(way.size() - i - g);
			tc+=way[e].second;
		}
		cout<<"Case #"<<(c + 1)<<": "<<tc<<endl;
	}	
}
