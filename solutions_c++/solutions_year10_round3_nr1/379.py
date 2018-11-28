#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <algorithm>
#define MAX 1005

using namespace std;

pair<int, int> AB[MAX];

bool comp(pair<int,int> p1, pair<int,int> p2) {
	return p1.first < p2.first;
}

int main() {
	int T,N,ct;
	cin >> T;
	for(int c=1;c<=T;c++) {
		ct=0;
		cin >> N;
		for(int i=0;i<N;i++)
			cin >> AB[i].first >> AB[i].second;
		sort(AB,AB+N,comp);
		for(int i=0;i<N;i++) {
			for(int j=i+1;j<N;j++) {
				if(AB[i].second > AB[j].second)
					ct++;
			}
		}
		cout << "Case #" << c << ": " << ct << '\n';
	}
	return 0;
}
