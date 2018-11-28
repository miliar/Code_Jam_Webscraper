/*
 * author: Eslam Zanaty
 * lang: c++
 * prob. kind :
 */
#include<iostream>
#include<fstream>
#include<cstdio>
#include<cmath>
#include<algorithm>
#include<string.h>
#include<vector>
#include<stack>
#include<queue>
#include<set>
using namespace std;
int main() {
	ifstream cin("A-large.in");
	ofstream cout("A-large.out");
	int test;
	cin >> test;
	for (int tt = 1; tt <= test; tt++) {
		int input;
		cin >> input;
		char rob;
		int x;
		queue<int> red, org;
		queue<char> order;
		for (int i = 0; i < input; i++) {
			cin >> rob >> x;
			if (rob == 'O') {
				org.push(x);
			} else {
				red.push(x);
			}
			order.push(rob);
		}
		int r = 1, o = 1, nr = 0, no = 0, time = 0;
		if (!red.empty()) {
			nr = red.front();
			red.pop();
		}
		if (!org.empty()) {
			no = org.front();
			org.pop();
		}
		while (!order.empty()) {
			if (order.front() == 'O') {
				if (no > o)
					o++;
				else if (no < o)
					o--;
				else if (no == o) {
					if (!org.empty()) {
						no = org.front();
						org.pop();
					}
					order.pop();
				}
				if (nr > r)
					r++;
				else if (nr < r)
					r--;
			} else {
				if (nr > r)
					r++;
				else if (nr < r)
					r--;
				else if (nr == r) {
					if (!red.empty()) {
						nr = red.front();
						red.pop();
					}
					order.pop();
				}
				if (no > o)
					o++;
				else if (no < o)
					o--;
			}
			time++;
		}
		cout << "Case #" << tt << ": " << time << endl;
	}
	return 0;
}
