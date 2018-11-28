#include <list>
#include <deque>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <vector>
#include <utility>
#include <string>
#include <algorithm>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <sstream>

using namespace std;

int main() {
	int NC;
	cin >> NC;
	
	for(int cs=1;cs<=NC;cs++) {
		int N,n,out=0;
		cin >> N;
		for(int i=1;i<=N;i++) {
			cin >> n;
			if(n!=i)
				out++;
		}
		
			
		
	
	
	
		cout << "Case #" << cs << ": " << out  << endl;
	}
	
	return 0;
}
