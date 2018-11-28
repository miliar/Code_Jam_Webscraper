#include <vector>
#include <string>
#include <sstream>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>

using namespace std;

#define all(x) x.begin(),x.end()
#define FOR(it,x) for(__typeof(x.begin())it=x.begin();it!=x.end();++it)
#define bits(x) __builtin_popcount(x)

#define MAX 2002

set<int> rooms[MAX];
int from[MAX],to[MAX];
int n,m,cant;

int color[MAX];
int best[MAX], bestCant;

void go(int pos, int totcol) {
	if (pos==n) {
		if (totcol <= bestCant) return;
		for (int i=0;i<cant;i++) {
			int mask=0;
			FOR(it,rooms[i]) mask|=(1<<color[*it]);
			if (mask+1!=(1<<totcol)) return;
		}
		bestCant=totcol;
		for (int i=0;i<n;i++) best[i]=color[i];
		return;
	}
	for (int i=0;i<totcol;i++) {
		color[pos]=i;
		go(pos+1,totcol);
	}
	color[pos]=totcol;
	go(pos+1,totcol+1);
}

int main(){
	int casos,cc;
	cin>>casos;
	
	for (cc=0;cc<casos;cc++) {
		cout<<"Case #"<<cc+1<<": ";
		cin>>n>>m;
		
		for (int i=0;i<m;i++) { cin>>from[i]; from[i]--; }
		for (int i=0;i<m;i++) { cin>>to[i]; to[i]--; }
		
		rooms[0].clear();
		cant=0;
		for (int i=0;i<n;i++) rooms[cant].insert(i);
		cant++;
		
		for (int i=0;i<m;i++) {
			for (int j=0;j<cant;j++) if (rooms[j].count(from[i]) && rooms[j].count(to[i])) {
				set<int> n1, n2;
				bool first = true;
				FOR(it, rooms[j]) {
					if (first) n1.insert(*it);
					else n2.insert(*it);
					if (*it == from[i]) {
						n2.insert(*it);
						first=false;
					}
					if (*it == to[i]) {
						n1.insert(*it);
						first=true;
					}
				}
				rooms[j]=n1;
				rooms[cant++]=n2;
				break;
			}
		}
		bestCant=0;
		go(0,0);
		cout<<bestCant<<endl;
		for (int i=0;i<n;i++) {
			if (i!=0) cout<<" ";
			cout<<best[i]+1;
		}
		cout<<endl;
		
	}
	return 0;
}
