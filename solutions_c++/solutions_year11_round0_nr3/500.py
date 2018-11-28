#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
#include <vector>
#include <cmath>
#include <map>
using namespace std;

vector<int> n;

int calc() {
	sort(n.begin(), n.end());

int    maxValue = 0;
	for(int i=1;i<n.size();i++)
	    maxValue += n[i];

	return maxValue;
}

int main()
{
	int nCase = 1, T;
	int N, t, ck;
	
	cin >> T;
	while(T-->0) {
	    cin >> N;
		n.clear(); ck = 0;
		for(int i=0;i<N;++i) {
			cin >> t;
			n.push_back(t);
			ck ^= t;
		}
		if(ck) {
			printf( "Case #%d: NO\n", nCase++);
		} else {
			printf( "Case #%d: %d\n", nCase++, calc());
		}
	}
	return 0;
}
