#include <cstdio>
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
using namespace std;

int main(){
	int t;
	cin >> t;
	for(int i=0;i<t;i++){
		int n;
		int time = 0;
		int opos = 1, bpos = 1;
		int ofree = 0, bfree = 0;
		int dist = 0;
		char color;
		int button;
		cin >> n;
		//printf("opos\tbpos\tofree\tbfree\tdist\tTime\n");
		
		for(int j=0;j<n;j++){
			cin >> color >> button;
			//printf("%d\t%d\t%d\t%d\t%d\t%d\n", opos, bpos, ofree, bfree, dist, time);

			if(color=='O')	{ dist = max(0, abs(opos-button)-ofree); ofree = 0; opos = button; }
			else			{ dist = max(0, abs(bpos-button)-bfree); bfree = 0; bpos = button; }

			time += dist+1;

			if(color=='O')	{ bfree += dist+1; }
			else			{ ofree += dist+1; }

		}
		//printf("%d\t%d\t%d\t%d\t%d\t%d\n", opos, bpos, ofree, bfree, dist, time);
		printf("Case #%d: %d\n", i+1, time);
	}
	return 0;
}