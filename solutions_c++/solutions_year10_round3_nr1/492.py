#include <stdio.h>
#include <algorithm>
#include <vector>

using namespace std;

struct rope {
	int a;
	int b;
};

vector<rope> list;

bool comp(rope x,rope y) {
	if (x.a!=y.a) return x.a<y.a;
	return x.b<y.b;
}

int main () {
	freopen ("in.txt","r",stdin);
	freopen ("out.txt","w",stdout);
	int t,ii,i,j,n,res;
	scanf ("%d",&t);
	for (ii=1;ii<=t;ii++) {
		scanf ("%d",&n);
		rope tmp;
		list.clear();
		for (i=0;i<n;i++) {
			scanf ("%d%d",&tmp.a,&tmp.b);
			list.push_back(tmp);
		}
		sort(list.begin(),list.end(),comp);
		res = 0;
		for (i=0;i<n;i++) {
			for (j=i+1;j<n;j++) {
				if (list[j].b<list[i].b) res++;
			}
		}
		printf ("Case #%d: %d\n",ii,res);
	}
	return 0;
}
