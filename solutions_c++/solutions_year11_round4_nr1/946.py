#include <iostream>
#include <vector>
#include <string>
#include <cstring>
#include <cmath>
#include <fstream>
#include <map>
#include <set>
#include <list>
#include <algorithm>
#include <iomanip>
using namespace std;

typedef long long ll;

multiset<pair<int, int> > mp;
int main()
{
	int T, bi, ei, wi;
	int X, S, R, t, N, acc;
	cin>>T;
	for(int tt = 1; tt <= T; ++tt){
		double sumt = 0;
		cin>>X>>S>>R>>t>>N;
		acc = R - S;
		int begin = 0;
		mp.clear();
		for(int i = 0; i < N; ++i){
			cin>>bi>>ei>>wi;
			if(bi > begin){
				mp.insert(make_pair(S, bi - begin));
			}
			mp.insert(make_pair(wi + S, ei - bi));
			begin = ei;
		}
		if(begin < X){
			mp.insert(make_pair(S, X - begin));
		}
		double lefttime = t;
		multiset<pair<int, int> >::iterator itr = mp.begin();
		while(itr != mp.end()){
			sumt += (double)((*itr).second) / (*itr).first;
			++itr;
		}
		itr = mp.begin();
		while(fabs(lefttime) > 1e-9){
			if(itr == mp.end())break;
			double cur_time = (double)((*itr).second) / (*itr).first;
			double after_time = (double)((*itr).second) / ((*itr).first + acc);
			if(after_time <= lefttime){
				lefttime -= after_time;
				sumt -= cur_time - after_time;
			}else {
				double len = lefttime * ((*itr).first + acc);
				sumt -= len / ((*itr).first) - lefttime;
				lefttime = 0;
			}
			++itr;
		}
		cout<<"Case #"<<tt<<": "<<fixed<<setprecision(9)<<sumt<<endl;
	}
	return 0;
}


		
