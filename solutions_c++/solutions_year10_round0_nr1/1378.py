//#include <iostream>
#include <fstream>
#include <sstream>
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

void go() {
	int N, K;
	cin >> N >> K;	
	for (int i=0; i<N; i++) {
		if (!((K >> i) %2)) {
			cout << "OFF";
			return;
		}
	}
	cout << "ON";
	return;
}

int main() {
	int T;
	cin>>T;
	for (int i=1; i<=T; i++) {
		cout<<"Case #"<<i<<": ";
		go();
		cout<<endl;
	}
	return 0;
}