#include <stdio.h>
#include <vector>
#include <algorithm>

using namespace std;

struct Trip {
	int dep, arr;
};

bool before(Trip a, Trip b) {
	if (a.dep != b.dep)
		return a.dep < b.dep;
	return a.arr < b.arr;
}

vector <Trip> trip[2];
vector <bool> done[2];
int n[2], t;

int fill(int place, int i) {
	int other = 1 - place, j;
	done[place][i] = true;
	for (j=0; j < n[other] && (done[other][j] || trip[other][j].dep < trip[place][i].arr+t); j++);
	if (j < n[other])
		fill(other,j);
}

int main() {
	int cases, test = 1;
	int i, ia, ib, n1, n2, ansa, ansb;
	
	scanf("%d",&cases);
	while (cases--) {
		scanf("%d %d %d",&t,&n[0],&n[1]);
		trip[0] = vector <Trip> (n[0]);
		trip[1] = vector <Trip> (n[1]);
		for (i=0; i < n[0]; i++) {
			scanf("%d:%d",&n1,&n2);
			trip[0][i].dep = n1*60 + n2;
			scanf("%d:%d",&n1,&n2);
			trip[0][i].arr = n1*60 + n2;
		}
		for (i=0; i < n[1]; i++) {
			scanf("%d:%d",&n1,&n2);
			trip[1][i].dep = n1*60 + n2;
			scanf("%d:%d",&n1,&n2);
			trip[1][i].arr = n1*60 + n2;
		}
		
		sort(trip[0].begin(),trip[0].end(),before);
		sort(trip[1].begin(),trip[1].end(),before);
		done[0] = vector <bool> (n[0],false);
		done[1] = vector <bool> (n[1],false);
		
		ansa = ansb = 0;
		for (ia=ib=0; ia < n[0] && ib < n[1]; ) {
			if (done[0][ia]) {
				ia++;
				continue;
			}
			if (done[1][ib]) {
				ib++;
				continue;
			}
			if (before(trip[0][ia],trip[1][ib]))
				fill(0,ia++), ansa++;
			else
				fill(1,ib++), ansb++;
		}
		
		while (ia < n[0])
			ansa += !done[0][ia++];
		while (ib < n[1])
			ansb += !done[1][ib++];
		
		printf("Case #%d: %d %d\n",test++,ansa,ansb);
	}
	
	return 0;
}
