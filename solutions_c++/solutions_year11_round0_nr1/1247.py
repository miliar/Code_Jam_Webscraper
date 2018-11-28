#include<stdio.h>
#include<cstdlib>
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>

using namespace std;

#define PB push_back
#define F first
#define S second

typedef pair<int,int> II;


int main() {

	int T;
	cin >> T;
	for(int t=0 ; t<T ; t++) {

		int n,x;
		char c;
		cin >> n;
		
		vector<II> path;
		vector<int> orange, blue;
		for(int i=0 ; i<n ; i++) {
			cin >> c >> x;
			if(c == 'O') {
				path.PB(II(0, x));
				orange.PB(x);
			} else {
				path.PB(II(1,x));
				blue.PB(x);
			}
		}
		orange.PB(1); blue.PB(1);

		int po = 1, pb = 1;
		int io = 0, ib = 0;
		int dia = 0;

		for(int i=0 ; i<n ; i++) {
			int moveo = orange[io] - po;
			int moveb = blue[ib] - pb;
			if(path[i].F == 0) {
				if(abs(moveb) > abs(moveo)) {
					if(moveb < 0) moveb = -(abs(moveo)+1);
					else moveb = abs(moveo)+1;
				}
				po += moveo;
				pb += moveb;
				dia += abs(moveo)+1;
				io++;
			} else {
				if(abs(moveo) > abs(moveb)) {
					if(moveo < 0) moveo = -(abs(moveb)+1);
					else moveo = abs(moveb)+1;
				}
				po += moveo;
				pb += moveb;
				dia += abs(moveb)+1;
				ib++;
			}
		}

		cout << "Case #" << t+1 << ": " << dia << endl;
	}

	return 0;
}
