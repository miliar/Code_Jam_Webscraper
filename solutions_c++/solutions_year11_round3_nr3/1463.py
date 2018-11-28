/*
 * c.cpp
 *
 *  Created on: May 22, 2011
 *      Author: greenvirag
 */

#include <algorithm>
#include <iostream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <list>

using namespace std;

typedef long long int llint;

int gcd(int a, int b) {
	int c;
    if( a<b ) {
        c = a;
        a = b;
        b = c;
    }

    while(true) {
		c = a%b;
		if(c==0)
		  return b;
		a = b;
		b = c;
    }
}

int gcd(vector<int>& nums, const int H, const int L) {
	if (nums.size()==0) {
		return 1;
	}
	if (nums.size()==1) {
		return nums.at(0);
	}
	int a;
	int ret = nums.front();
	nums.erase(nums.begin());
	while (nums.size()) {
		a = nums.back();
		ret=gcd(a,ret);
		nums.pop_back();
	}
	if (ret==1) {
		return -1;
	}
	return ret;
}


int lcm(int a, int b) {
	int c=1;
	for(; c%a != 0 || c%b != 0; c++);
	return c;
}

int lcm(vector<int>& nums, const int H, const int L) {
	if (nums.size()==0) {
		return 1;
	}

	if (nums.size()==1) {
		return nums.at(0);
	}

	int a;
	int ret = nums.front();
	nums.erase(nums.begin());
	while (nums.size()) {
		a = nums.back();
		ret=lcm(a,ret);
		if (ret>H) {
			return -1;
		}
		nums.pop_back();
	}
	return ret;
}

void run(int testcase)
{
	register int i;
	register unsigned int j;
	int v,w;

	int N, L, H, k;
	cin >> N;
	cin >> L;
	cin >> H;

//	cout << "\nN " << N;
//	cout << ", L " << L;
//	cout << ", H " << H;
//	cout << "\n";

	vector<int> lows;
	vector<int> mids;
	vector<int> highs;

	set<int> all;

	for (i=0; i<N; i++) {
		cin >> k;
		if (k==1) {
			continue;
		}
		if (k<L) {
			if (all.find(k)==all.end()) {
				lows.push_back(k);
				all.insert(k);
			}
		} else if (k>H) {
			if (all.find(k)==all.end()) {
				highs.push_back(k);
				all.insert(k);
			}
		} else {
			if (all.find(k)==all.end()) {
				mids.push_back(k);
				all.insert(k);
			}
		}
	}

	sort(lows.begin(), lows.end());
	sort(highs.begin(), highs.end());
	sort(mids.begin(), mids.end());

//	for (j=0; j<highs.size(); j++) {
//		cout << "\tj " << highs.at(j);
//	}
//	cout << endl;

	long int h = gcd(highs, H, L);
//	cout << "h = " << h << endl;

	long int l = lcm(lows, H, L);
//	cout << " and l = " << l << endl;

	if ((l==-1 || h==-1) || (l>h && h>1) || l>H || (h>1 && h<L)) {
		cout << "Case #" << testcase << ": NO" << endl;
		return;
	}


//	for (j=0; j<mids.size(); j++) {
//		cout << "\tj " << mids.at(j);
//	}
//	cout << endl;

	for (i=L; i<=H; i++) {
		if ( (l==1 || i%l==0 ) && (h==1 || h%i==0 )) {
			bool oke = true;
			// care only for mids
			for (j=0; j<mids.size(); j++) {
				if (mids.at(j) > i) {
					v = mids.at(j);
					w = i;
				} else {
					w = mids.at(j);
					v = i;
				}
				if (v%w != 0) {
					oke = false;
					break;
				}
			}
//			cout << endl;

			if (oke == true) {
				cout << "Case #" << testcase << ": " << i << endl;
				return;
			}
		}
	}

	cout << "Case #" << testcase << ": NO" << endl;
}


int main()
{
	int i=1, testcase;
	cin >> testcase;
	for (; i<=testcase; i++) {
		run(i);
	}
	return 0;
}
