/*
 * A.cpp
 *
 *  Created on: Sep 12, 2009
 *      Author: Yasser
 */

#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<set>
#include<queue>
#include<map>
#include<sstream>
#include<cstdio>
#include<cmath>
#include<stack>
#include<complex>

using namespace std;

string toBase(int num, int b) {
	string s = "";
	while (num) {
		s += (char) ((num % b) + '0');
		num /= b;
	}
	return s;
}

bool islucky(string st,int b) {
	set<string> s;

	while(1){
		if(!s.insert(st).second)return false;
		long long num = 0;
		for (int i = 0; i < st.size(); i++) {
			num += (st[i] - '0') * (st[i] - '0');
		}
		if(num == 1)break;
		st = toBase(num,b);
	}
	return true;
}

int main() {

	freopen("in.in", "rt", stdin);
	freopen("in.txt","wt",stdout);

	int TC,i,n;
	int a[20],tt=1;
	string s;
	cin >> TC;
	getline(cin, s);
	while (TC--) {
		getline(cin, s);
		istringstream is(s);
		int x = 0;
		while (is >> a[x++])
			;
		x--;
		cout<<"Case #"<<tt++<<": ";
		for (n = 2;; n++) {
			for (i = 0; i < x; i++) {
				if(!islucky(toBase(n,a[i]),a[i]))
					break;
			}
			if(i == x)
			{
				cout<<n<<endl;
				break;
			}
		}
	}

	return 0;
}
