//#include <iostream>
#include <fstream>
#include <set>
#include <list>
#include <vector>
#include <map>
#include <queue>
#include <stack>
#include <string>
#include <cmath>
#include <algorithm>
using namespace std;

ifstream cin("A-large.in",ios::in);
ofstream cout("A-large.out",ios::out);

void function() {
	int N;
	cin >> N;
	vector < vector <bool> > A;
	for (int i=0; i<N; i++) {
		vector <bool> temp;
		char ch;
		bool t;
		ws(cin);
		for (int j=0; j<N; j++) {
			cin >> ch;
			if (ch=='0') t=0;
			else t=1;
			temp.push_back(t);
		}
		A.push_back(temp);
	}
	vector <int> pos;
	for (int i=0; i<N; i++) {
		int max = -1;
		for (int j=N-1; j>=0; j--) {
			if (A[i][j]) {
				max = j;
				break;
			}
		}
		pos.push_back(max);
	}
	int sum=0;
	for (int i=0; i<N; i++) {
		for (int j=i; j<N; j++) {
			if (pos[j]<=i) {
				sum+=j-i;
				int temp = pos[j];
				for (int k=j; k>i; k--)
					pos[k] = pos[k-1];
				pos[i] = temp;
				break;
			}
		}
	}
	cout <<sum;
	return;
}



	




int main() {
	int T;
	cin>>T;
	for (int i=1; i<=T; i++) {
		cout<<"Case #"<<i<<": ";
		function();
		cout<<endl;
	}
	return 0;
}