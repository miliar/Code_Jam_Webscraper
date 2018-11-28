#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string.h>

#define INT_MAX 20000

using namespace std;

typedef struct {
	int is_leaf;
	int is_and;
	int is_changeable;
	int val;
} tree_t;

tree_t tree[100];

int case_cnt;
int M;
int desired;

int nodes_i;
int nodes_l;

int mini;

int calc_tree(int pos) {

	int r,l;

	if ( tree[pos].is_leaf ) {
		return tree[pos].val;
	}

	l = calc_tree( (pos+1) * 2 - 1);
	r = calc_tree( (pos+1) * 2 );

	if ( tree[pos].is_and ) {
		tree[pos].val = l & r;
	} else {
		tree[pos].val = l | r;
	}

	return tree[pos].val;
}

void tryit(int where, int changed) {

	if ( tree[where].is_leaf ) {
		if ( calc_tree(0) == desired ) {
			if ( changed < mini ) mini = changed;
		}
		return;
	}

	tryit( where+1, changed );

	if ( tree[where].is_changeable ) {
		tree[where].is_and = ( tree[where].is_and + 1 ) % 2;
		tryit( where+1, changed+1);
		tree[where].is_and = ( tree[where].is_and + 1 ) % 2;
	}
}
		


int main ( int argc, char ** argv ) {
	int case_nr;
	int x,y;
	int G,C;
	int val;

	scanf("%d",&case_cnt);
	for (case_nr = 0; case_nr < case_cnt; case_nr++ ) {
		memset(tree, 0, sizeof(tree) );
		mini = INT_MAX;

		scanf("%d %d", &M, &desired);
	
		nodes_i = (M-1)/2;
		nodes_l = (M+1)/2;

		for (x=0; x<nodes_i; x++) {
			scanf("%d %d", &G, &C);
			tree[x].is_leaf = 0;
			tree[x].is_and = G;
			tree[x].is_changeable = C;
			tree[x].val = 0;
		}

		for (x=0; x<nodes_l; x++) {
			scanf("%d", &val);
			tree[x+nodes_i].is_leaf = 1;
			tree[x+nodes_i].is_and = 0;
			tree[x+nodes_i].is_changeable = 0;
			tree[x+nodes_i].val = val;
		}

		tryit( 0, 0);

		if ( mini != INT_MAX ) {
			printf("Case #%d: %d\n", case_nr+1, mini);
		} else {
			printf("Case #%d: IMPOSSIBLE\n", case_nr+1);
		}
	}

	return 0;
}
