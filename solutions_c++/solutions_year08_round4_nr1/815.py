#include <vector>
#include <cstdio>
#define maxint ((1<<31)-1)
using namespace std;
typedef pair<int,int> node;

int change(vector<node> &tree, int n, int v) {
	if (tree[n].second==-1) {
		if (v==tree[n].first) return 0;
		else return -1;
	}
	int left = change(tree, 2*n+1, v); //fprintf(stderr, "%d sais %d\n", (2*n+1)+1, left);
	int right = change(tree, 2*n+2, v); //fprintf(stderr, "%d sais %d\n", (2*n+2)+1, right);
	int leftval = left?1-v:v;
	int rightval = right?1-v:v;
	int myval = tree[n].first ? leftval&&rightval : leftval||rightval;
	if (myval==v) return 0;
	
	int m1=maxint, m2=maxint, m3=maxint;
	int m4 = maxint, m5 = maxint, m6 = maxint;
	if (tree[n].first) {
		if (tree[n].second && ((leftval||rightval) == v)) return 1;
		if (left!=-1 && ((!leftval&&rightval) == v)) m1 = left;
		if (right!=-1 && ((leftval&&!rightval) == v)) m2 = right;
		if (left!=-1 && right!=-1 && ((!leftval&&!rightval) == v)) m3 = left+right;

		if (tree[n].second) {
			if (left!=-1 && ((!leftval||rightval) == v)) m4 = left+1;
			if (right!=-1 && ((leftval||!rightval) == v)) m5 = right+1;
			if (left!=-1 && right!=-1 && ((!leftval||!rightval) == v)) m6 = left+right+1;
		}
	} else {
		if (tree[n].second && ((leftval&&rightval) == v)) return 1;
		if (left!=-1 && ((!leftval||rightval) == v)) m1 = left;
		if (right!=-1 && ((leftval||!rightval) == v)) m2 = right;
		if (left!=-1 && right!=-1 && ((!leftval||!rightval) == v)) m3 = left+right;
		
		if (tree[n].second) {
			if (left!=-1 && ((!leftval&&rightval) == v)) m4 = left+1;
			if (right!=-1 && ((leftval&&!rightval) == v)) m5 = right+1;
			if (left!=-1 && right!=-1 && ((!leftval&&!rightval) == v)) m6 = left+right+1;
		}
	}

	int result = min(m1,min(m2,min(m3,min(m4,min(m5,m6)))));
	if (result==maxint) return -1;
	else return result;
}

int main() {
	int n;
	scanf("%d", &n);
	for (int ixn=1; ixn<=n; ixn++) {
		int m,v;
		scanf("%d %d", &m, &v);
		vector<node> tree;
		for (int i=0; i<(m-1)/2; i++) {
			int g,c;
			scanf("%d %d", &g, &c);
			tree.push_back(make_pair(g,c));
		}
		for (int i=0; i<(m+1)/2; i++) {
			int g;
			scanf("%d", &g);
			tree.push_back(make_pair(g,-1));
		}
		int result = change(tree,0,v);
		if (result==-1) printf("Case #%d: IMPOSSIBLE\n", ixn);
		else printf("Case #%d: %d\n", ixn, result);
	}

	return 0;
}
