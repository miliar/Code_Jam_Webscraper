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
#include <bitset>

using namespace std;

typedef unsigned long long int u64;
typedef long long int i64;

set<int> cn[410];

queue< pair<int, bitset<410> > > bfs; 

int main() {
	int NC;

	cin >> NC;
	
	for(int cs=1;cs<=NC;cs++) {
		int P,W;
		cin >> P >> W;

		for(int i=0;i<W;i++) {
			int p1,p2;
			char com;
			cin >> p1 >> com >> p2;
			cn[p1].insert(p2);
			cn[p2].insert(p1);
		}
		bitset<410> bb(0);
		bitset<410> ct(0);
		bb.set(0,1);
		set<int>::iterator it;
		pair<int, bitset<410> > pos(0,bb);
		bfs.push(pos);
		int bestd=1000,bestt=0;
		while(!bfs.empty()) {
			pos=bfs.front();
			bfs.pop();
			int apos=pos.first;
			bb=pos.second;
			if(bb.count()-1 > bestd)
				break;
			if(cn[apos].count(1)) {
				int disti=bb.count()-1;
				ct.reset();
				for(int i=0;i<P;i++) {
					if(bb[i]) {
						for(it=cn[i].begin();it!=cn[i].end();it++) {
							if(bb[*it]==0) 
								ct[*it]=1;
						}
					}
				}
				int thti = ct.count();
				if(disti<bestd || (disti==bestd && thti>bestt)) {
					bestd=disti;
					bestt=thti;
				}
			}
			else {
				for(it=cn[apos].begin();it!=cn[apos].end();it++) {
					if(bb[*it]==0) {
						bitset<410> ai = bb;
						ai[*it]=1;
						int ppos=*it;
						pair<int, bitset<410> > lpos(ppos,ai);
						bfs.push(lpos);
					}
				}
			}
		}
		
		while(!bfs.empty())
			bfs.pop();
		for(int i=0;i<410;i++)
			cn[i].clear();
		
		cout << "Case #" << cs << ": " <<  bestd << ' ' << bestt << endl;
	}
	
	return 0;
}
