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

#define max_macro(a,b)    (((a) > (b)) ? (a) : (b))
#define min_macro(a,b)    (((a) < (b)) ? (a) : (b))

struct Segment {
	Segment(short x1_, short y1_, short x2_, short y2_) {
		x1 = min_macro(x1_, x2_);
		x2 = max_macro(x1_, x2_);
		y1 = min_macro(y1_, y2_);
		y2 = max_macro(y1_, y2_);
		horiz = y1 == y2;
	}
	short x1, y1;
	short x2, y2;
	bool horiz;
} ;

struct sortByX {
	bool operator()(const Segment& S1, const Segment& S2) {
		return S1.x1 < S2.x1;
	}
};


struct sortByY {
	bool operator()(const Segment& S1, const Segment& S2) {
		return S1.y1 < S2.y1;
	}
};

#define MAX_COORD 10000

struct delta {
	short dx, dy;
};

static delta dd[] = {
	{0, 1}, // North
	{-1, 0}, // West
	{0, -1}, // South
	{+1, 0}, // East
};

#define  LEN_S 42
#define  OFFSET 3001
static char s[LEN_S];

unsigned map_move(char s, unsigned curr_dir) {
	switch(s)
	{
	case 'F' : return curr_dir;
	case 'L': return (curr_dir + 1) % 4;
	case 'R': return (curr_dir + 3) % 4;
	}
}

static vector<Segment> vert_seg[MAX_COORD];
static vector<Segment> horiz_seg[MAX_COORD];

bool find_if_vert_seg(short y, short x_begin, short x_end) {
	unsigned ss = 0;
	for(unsigned j = x_begin; j <= x_end; ++j) {
		if(!vert_seg[j].empty()) {
			for(unsigned t = 0, t_end = (unsigned) vert_seg[j].size(); t < t_end; ++t) {
				if(vert_seg[j][t].y1 <= y && vert_seg[j][t].y2 > y) ++ss;
			}
		}
	}
	return ss > 0 && ss % 2 == 0;
}

bool find_if_horiz_seg(short x, short y_begin, short y_end) {
	unsigned ss = 0;
	for(unsigned j = y_begin; j <= y_end; ++j) {
		if(!horiz_seg[j].empty()) {
			for(unsigned t = 0, t_end = (unsigned) horiz_seg[j].size(); t < t_end; ++t) {
				if(horiz_seg[j][t].x1 <= x && horiz_seg[j][t].x2 > x) ++ss;
			}
		}
	}
	return ss > 0 && ss % 2 == 0;
}

int main(void) {
	unsigned num_tests;
	scanf(" %u", &num_tests);
	for(unsigned test_it = 1; test_it <= num_tests; ++test_it) {
		for(unsigned j = 0; j < MAX_COORD; ++j) {
			vert_seg[j].clear(); horiz_seg[j].clear();
		}
		short curr_x = OFFSET, curr_y = OFFSET;
		unsigned curr_dir = 0; // North
		unsigned num_segs;
		short min_x = SHRT_MAX, min_y = SHRT_MAX;
		short max_x = SHRT_MIN, max_y = SHRT_MIN;
		scanf(" %u", &num_segs);
		unsigned start_x = curr_x, start_y = curr_y;
		for(unsigned j = 0; j < num_segs; ++j) {
			unsigned rep_cnt;
			scanf(" %s %u", s, &rep_cnt);
			// Intrepret
			unsigned g = (unsigned)strlen(s);
			for(unsigned qq = 0; qq < rep_cnt; ++qq) {
				for(unsigned k = 0; k < g; ++k) {
					if(s[k] == 'F') {
						curr_x += dd[curr_dir].dx;
						curr_y += dd[curr_dir].dy;
						min_x = min_macro(min_x, curr_x);
						max_x = max_macro(max_x, curr_x);
						min_y = min_macro(min_y, curr_y);
						max_y = max_macro(max_y, curr_y);
					} else {
						if(curr_y != start_y) { // Vert seg
							vert_seg[curr_x].push_back(Segment(start_x, start_y, curr_x, curr_y));
						}
						if(curr_x != start_x) { // Horiz
							horiz_seg[curr_y].push_back(Segment(start_x, start_y, curr_x, curr_y));
						}
						start_x = curr_x; start_y = curr_y;
						curr_dir = map_move(s[k], curr_dir);
					}
				}
			}
		}
		if(curr_y != start_y) { // Vert seg
			vert_seg[curr_x].push_back(Segment(start_x, start_y, curr_x, curr_y));
		}
		if(curr_x != start_x) { // Horiz
			horiz_seg[curr_y].push_back(Segment(start_x, start_y, curr_x, curr_y));
		}
		start_x = curr_x; start_y = curr_y;
		for(short x = min_x; x <= max_x; ++x) {
			sort(vert_seg[x].begin(), vert_seg[x].end(), sortByY());
		}

		for(short y = min_y; y <= max_y; ++y) {
			sort(horiz_seg[y].begin(), horiz_seg[y].end(), sortByX());
		}

		unsigned area = 0;
		for(short x = min_x; x <= max_x; ++x) {
			for(short y = min_y; y <= max_y; ++y) {
				if(find_if_horiz_seg(x, min_y, y) && find_if_horiz_seg(x, y+1, max_y)) {
					++area;
				} else if(find_if_vert_seg(y, min_x, x) && find_if_vert_seg(y, x+1, max_x)) {
					++area;
				}
			}
		}

		printf("Case #%d: %u\n", test_it, area);
	}
	return 0;
}
