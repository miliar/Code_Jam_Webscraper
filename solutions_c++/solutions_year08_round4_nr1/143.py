#define _CRT_SECURE_NO_WARNINGS 1
#include <iostream>
#include <algorithm>
#include <stdlib.h>
#include <vector>
#include <string>
#include <bitset>
#include <math.h>
#include <limits.h>
#include <float.h>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <assert.h>
#include <sstream>
#include <limits>
#include <list>
#include <stdlib.h>
using namespace std;
typedef unsigned long long ULL;
typedef signed long long SLL;
typedef unsigned short ushort;
typedef signed char schar;
typedef unsigned char uchar;

#define GateAnd 1
#define GateOr 0

struct TNode {
	bool leaf;
	unsigned changed_needed_for[2];
	unsigned node_type; // 1-> AND, 0 -> OR
	unsigned current_val; // 0 or 1
	bool changable;
};

static TNode * tree;

static inline unsigned oper(unsigned type, unsigned ch1, unsigned ch2) {
	return type == GateOr ? (ch1 || ch2) : (ch1 && ch2);
}

static inline TNode& left_ch_idx(unsigned n) { return tree[(n << 1) + 1];}
static inline TNode& right_ch_idx(unsigned n) { return tree[(n + 1) << 1];}
#define max_macro(a,b)    (((a) > (b)) ? (a) : (b))
#define min_macro(a,b)    (((a) < (b)) ? (a) : (b))

static inline unsigned add_vals(unsigned p, unsigned q) {
	if(p == UINT_MAX || q == UINT_MAX) return UINT_MAX;
	else return p + q;
}

int main(void) {
	unsigned num_tests;
	scanf(" %u", &num_tests);
	for(unsigned test_it = 1; test_it <= num_tests; ++test_it) {
		unsigned v_target, m;
		scanf(" %u %u", &m, &v_target);
		tree = new TNode[m];
		unsigned int_node_cnt = (m - 1)/2, leaf_cnt = (m + 1)/2;
		for(unsigned j = 0; j < int_node_cnt; ++j) {
			unsigned g, c; scanf(" %u %u", &g, &c);
			tree[j].leaf = false;
			tree[j].node_type = g == 1 ? 1 : 0;
			tree[j].changed_needed_for[0] = tree[j].changed_needed_for[1] = UINT_MAX;
			tree[j].changable = c == 1;
		}
		for(unsigned j = int_node_cnt; j < m; ++j) {
			scanf(" %u", &tree[j].current_val);
			tree[j].leaf = true;
			tree[j].changed_needed_for[tree[j].current_val] = 0;
			tree[j].changed_needed_for[1 - tree[j].current_val] = UINT_MAX;
			tree[j].changable = false;
		}
		// Calc the tree:
		for(signed j = int_node_cnt - 1; j >= 0; --j) {
			TNode& lc = left_ch_idx(j), rc = right_ch_idx(j);
			unsigned ch1 = lc.current_val, ch2 = rc.current_val;
			unsigned v = oper(tree[j].node_type, ch1, ch2);
			tree[j].current_val = v;
			tree[j].changed_needed_for[v] = 0;
			unsigned ov = 1 - v;
			
			// See how we can get ov without changing this node
			if(tree[j].node_type == GateAnd) {
				if(ov == 0) {
					tree[j].changed_needed_for[ov] = min_macro(lc.changed_needed_for[0], rc.changed_needed_for[0]);
				} else { // ov == 1
					tree[j].changed_needed_for[ov] = add_vals(lc.changed_needed_for[1], rc.changed_needed_for[1]);
				}
			} else { // GateOr
				if(ov == 0) {
					tree[j].changed_needed_for[ov] = add_vals(lc.changed_needed_for[0], rc.changed_needed_for[0]);
				} else { // ov == 1
					tree[j].changed_needed_for[ov] = min_macro(lc.changed_needed_for[1], rc.changed_needed_for[1]);
				}
			}

			if(tree[j].changable) { // Changeable
				unsigned num_ch = UINT_MAX;
				if(tree[j].node_type == GateAnd) { // We turn it into an or node
					if(ov == 0) {
						num_ch = add_vals(lc.changed_needed_for[0], rc.changed_needed_for[0]);
					} else { // ov == 1
						num_ch = min_macro(lc.changed_needed_for[1], rc.changed_needed_for[1]);
					}
				} else { // GateOr
					if(ov == 0) {
						num_ch = min_macro(lc.changed_needed_for[0], rc.changed_needed_for[0]);
					} else { // ov == 1
						num_ch = add_vals(lc.changed_needed_for[1], rc.changed_needed_for[1]);
					}
				}
				if(num_ch != UINT_MAX) {
					++num_ch; // For the current change
					tree[j].changed_needed_for[ov] = min_macro(tree[j].changed_needed_for[ov], num_ch);
				}
			}
		}


		// Output:
		if(tree[0].changed_needed_for[v_target] == UINT_MAX) {
			printf("Case #%d: IMPOSSIBLE\n", test_it);
		} else {
			printf("Case #%d: %d\n", test_it, tree[0].changed_needed_for[v_target]);
		}

		delete[] tree;
	}
	return 0;
}
