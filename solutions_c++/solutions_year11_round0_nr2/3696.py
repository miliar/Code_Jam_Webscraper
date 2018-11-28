/*
 * B.Magicka.cpp
 *
 *  Created on: May 7, 2011
 *      Author: ahmed
 */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
typedef long long ll;
using namespace std;

#define pb push_back
#define mp make_pair
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<vector<pii> > adjL;
int oo = (int) 1e9;

int main()
{
	freopen("a.txt", "wt", stdout);
	int t;scanf("%d", &t);
	for (int ii = 0; ii < t; ++ii) {
//		vector<vector<int > >vv = vector<vector<int > >(26, vector<int >(26, 0));
		map<pair<char, char>, char >mpc;
		map<char, char >mpr;
		int a, b, n;
		scanf("%d", &a);
		string cmb;
		for (int i = 0; i < a; ++i) {
			cin>>cmb;
			mpc[mp(cmb[0], cmb[1])] = cmb[2];
			mpc[mp(cmb[1], cmb[0])] = cmb[2];
		}
		scanf("%d", &b);
		string rm;
		for (int i = 0; i < b; ++i) {
			cin>>rm;
			mpr[rm[0]] = rm[1];
			mpr[rm[1]] = rm[0];
		}
		scanf("%d", &n);
		string all;
		cin>>all;
		vector<char> vc;
		vc.pb(all[0]);
		for (int i = 1; i < (int )all.size(); ++i) {

			if(vc.size() > 0 && mpc.count(mp(all[i], vc[vc.size()-1]))) {
				vc.pb(all[i]);
//				cout<<vc[vc.size()-1]<<" "<<vc[vc.size()-2]<<endl;
				while(vc.size() > 1 && mpc.count(mp(vc[vc.size()-1], vc[vc.size()-2]))) {
					char c1 = vc[vc.size()-1];
					char c2 = vc[vc.size()-2];
					vc.pop_back();
					vc.pop_back();
					vc.pb(mpc[mp(c1,c2)]);
				}
			}
			else if(find(vc.begin(), vc.end(), mpr[all[i]]) != vc.end())
							vc = vector<char>();
			else
				vc.pb(all[i]);
		}
		printf("Case #%d: ", ii+1);
		cout<<"[";
		for (int i = 0; i < (int)vc.size(); ++i) {
			if(i)
				cout<<", ";
			cout<<vc[i];
		}
		cout<<"]"<<endl;
	}
	return 0;
}

/*
5
0 0 2 EA
1 QRI 0 4 RRQR
1 QFT 1 QF 7 FAQFDFQ
1 EEZ 1 QE 7 QEEEERA
0 1 QW 2 QW
 */
