// projA.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"

#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <iostream>

int xx[100010];
int yy[100010];

using namespace std;

typedef __int64 ll;

ll cnk(ll n, ll k) {
	if (n < k)
		return 0;
	ll ret = 1;
	for (ll i = 1; i <= k; i++) {
		ret = ret * (n-i+1) / i;
	}
	return ret;
}

int _tmain(int argc, _TCHAR* argv[])
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int nt;
	scanf("%d", &nt);
	for (int test = 1; test <= nt; test++) {
		int n, A, B, C, D, x0, y0, M;
		scanf("%d %d %d %d %d %d %d %d", &n, &A, &B, &C, &D, &x0, &y0, &M);

		set<pair<int,int> > sp;
		for (int i = 0; i < n; i++) {
			xx[i] = x0;
			yy[i] = y0;
			sp.insert(make_pair(x0,y0));

			x0 = (A * (__int64)x0 + B) % M;
			y0 = (C * (__int64)y0 + D) % M;

		}

		vector<pair<int,int> > vp = vector<pair<int,int> >(sp.begin(), sp.end());

		/*
		printf("points: ");
		for (int i = 0; i < vp.size(); i++)
			cout << vp[i].first << "," << vp[i].second << " ";
		cout << endl;
		*/

		map<pair<int,int>, int> mp;
		for (int i = 0; i < vp.size(); i++) {
			mp[make_pair(vp[i].first%3, vp[i].second%3)]++;
		}

		vector<pair<int,int> > ost;
		for (int i = 0; i < 3; i++) 
			for (int j = 0; j < 3; j++)
				ost.push_back(make_pair(i,j));
		sort(ost.begin(), ost.end());

		ll ret = 0;
		for (int i = 0; i < ost.size(); i++) {
			for (int j = i; j < ost.size(); j++) {
				for (int k = j; k < ost.size(); k++) {

					if ((ost[i].first + ost[j].first + ost[k].first)%3)
						continue;
					if ((ost[i].second + ost[j].second + ost[k].second)%3)
						continue;

					if (i == j && j == k) {
						ll n = mp[ost[i]];
						if (n < 3)
							continue;
						ret += cnk(n,3);
					} else {
						if (i == j) {
							ret += cnk(mp[ost[i]], 2) * (ll)mp[ost[k]];
						} else if (j == k) {
							ret += cnk(mp[ost[j]], 2) * (ll)mp[ost[i]];
						} else {
							ret += mp[ost[i]] * (ll)mp[ost[j]] * mp[ost[k]];
						}
					}
				}
			}
		}

		cout << "Case #" << test << ": " << ret << endl;

	}

	return 0;
}

