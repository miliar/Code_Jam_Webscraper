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
	char c;
	int b;
	cin >> NC;
	
	for(int cs=1;cs<=NC;cs++) {
		int N;
		cin >> N;
		int O=1,B=1,spO=0,spB=0,wst=0;
		cin >> c >> b;
		if(c=='O') {
			spO = ((b>O)?(b-O):(O-b))+1;
			O=b;
		}
		else {
			spB = ((b>B)?(b-B):(B-b))+1;
			B=b;
		}
		for(int i=1;i<N;i++) {
			cin >> c >> b;
			if(c=='O') {
				spO += ((b>O)?(b-O):(O-b));
				O=b;
				if(spB>0) {					
					if(spO<spB)
						spO=0;
					else
						spO-=spB;
					wst+=spB;
					spB=0;
				}
				spO++;
			}
			else {
				spB += ((b>B)?(b-B):(B-b));
				B=b;
				if(spO>0) {
					if(spB<spO)
						spB=0;
					else
						spB-=spO;
					wst+=spO;
					spO=0;
				}
				spB++;
			}
		}
		wst+=spB+spO;
		
		
	
		cout << "Case #" << cs << ": " <<  wst << endl;
	}
	
	return 0;
}
