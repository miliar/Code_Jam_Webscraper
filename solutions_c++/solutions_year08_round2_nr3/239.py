#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

#include <cmath>
#include <cstdio>
#include <cstdlib>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

typedef vector<int> vi;
typedef vector<double> vd;

#define PI 3.1415926535897932384626433832795


int main()
{
	int cases;
	cin >> cases;
	for(int c = 0; c < cases; ++c) {
		int deck;
		int ds;
		vector<int> index;
		cin >> deck >> ds;
		for(int i = 0; i < ds; ++i) {
			int qq;
			cin >> qq;
			index.push_back(qq);
		}

		vector<int> positions;
		for(int i = 0; i < deck; ++i) positions.push_back(0);
		
		int done = 1;
		int pos = 0;
		while(done <= deck) {
			int step = done-1;
			int zeros = 0;
			for(int i = 0; i < positions.size(); ++i) {
				if(!positions[i]) ++zeros;
			}
			step = step%zeros;
			for(int i = pos;; ++i) {
				if(i == positions.size()) i = 0;
				if(!positions[i]) --step;
				if(step == -1) {
					positions[i] = done;
					++done;
					pos = i;
					break;
				}
			}
		}
		
		cout << "Case #" << c+1 << ": ";
		for(int i = 0; i < ds; ++i) {
			cout << positions[index[i]-1] << " ";
		}
		cout << endl;
	}
	return 0;
}





