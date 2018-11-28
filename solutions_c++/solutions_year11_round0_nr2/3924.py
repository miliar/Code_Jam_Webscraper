//============================================================================
// Name        : B.cpp
// Author      : Toqa Osama
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <sstream>
using namespace std;
vector<string> c, d;
vector<char> l;
int C, D, N;
string n;
void done() {
	bool flag = true;
	for (int i = 0; i < N; i++) {
		if (flag == true && i != 0) {
			bool m = false;
			for (int j = 0; j < d.size(); j++) {
				if ((n[i] == d[j][0] && n[i - 1] == d[j][1]) || (n[i]
						== d[j][1] && n[i - 1] == d[j][0])) {
					l.pop_back();
					l.push_back(d[j][2]);
					flag = false;
					m = true;
					break;
				}
			}
			if (m)
				continue;
		}
		char ch = '*';
		for (int j = 0; j < c.size(); j++) {
			if (n[i] == c[j][0])
				ch = c[j][1];
			else if (n[i] == c[j][1])
				ch = c[j][0];
		}
		if (ch != '*') {
			bool m = false;
			for (int j = 0; j < l.size(); j++) {
				if (l[j] == ch) {
					l.clear();
					flag = false;
					m = true;
					break;
				}
			}
			if (m)
				continue;
		}
		l.push_back(n[i]);
		flag = true;
	}
}
int main() {
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int test;
	cin >> test;
	string temp,end;
	getline(cin,end);
	for (int t = 1; t <= test; t++) {
		string temp;
		c.clear();
		d.clear();
		l.clear();
		getline(cin,temp);
		stringstream ss;
		int y = 0;
		if(temp[1]-'0' >= 0 &&temp[1]-'0'<= 9 ){
			string w = "";
									w += temp[y];
									w+=temp[y+1];
										ss<<w;
			ss>>D;
			y = 3;
		}
		else{
			D = temp[0]-'0';
			y = 2;
		}
		for (int k = 0; k < D; k++) {
			string w = "";
			w += temp[y];
			w+=temp[y+1];
			w+=temp[y+2];
			d.push_back(w);
			y+=4;
		}
		stringstream ss2;
		if(temp[y+1]-'0' >= 0 &&temp[y+1]-'0'<= 9 ){
			string w = "";
									w += temp[y];
									w+=temp[y+1];
										ss2<<w;
					ss2>>C;
					y +=3;
				}
				else{
					C = temp[y]-'0';
					y += 2;
				}
		for (int k = 0; k < C; k++) {
			string w = "";
			w += temp[y];
			w+=temp[y+1];
			c.push_back(w);
			y+=3;
		}
		stringstream ss1;
		if(temp[y+1]-'0' >= 0 &&temp[y+1]-'0'<= 9 && temp[y+2] == '0'){
									N = 100;
									y +=4;
								}
		else if(temp[y+1]-'0' >= 0 &&temp[y+1]-'0'<= 9 ){
			string w = "";
						w += temp[y];
						w+=temp[y+1];
							ss1<<w;
							ss1>>N;
							y +=3;
						}
						else{
							N = temp[y]-'0';
							y += 2;
						}
		n = temp.substr(y);
		done();
		cout << "Case #" << t << ": [";
		for (int i = 0; i < l.size(); i++) {
			cout << l[i];
			if (i != l.size() - 1)
				cout << ", ";
		}
		cout << "]";
		if (t != test)
			cout << endl;
	}
	return 0;
}
