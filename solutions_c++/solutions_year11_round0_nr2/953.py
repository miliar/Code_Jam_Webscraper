#include <cstdio>
#include <algorithm>
#include <vector>
#include <list>
#include <set>
#include <map>
#include <string>
#include <numeric>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>

#define ALL(s) (s).begin(), (s).end()
#define FOREACH(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define FOR(i, a, b) for (int i = (a); i <= (b); i++)
#define REP(i, a) for (int i = 0; i < a; i++)

#define SZ(x) ((int) (x).size())
#define MAX(a,b) ((a) > (b) ? (a) : (b))
#define MIN(a,b) ((a) < (b) ? (a) : (b))

using namespace std;

int ncombinations;
int noppositions;
int ninvoke;

list<char> invoke_list;
list<char> actual_list;

typedef pair<char, char> ElementPair;
map<ElementPair, char> combinations;
map<ElementPair, bool> oppositions;

void combine() {
	if (actual_list.size() >= 2) {
		// get rightmost two elements
		list<char>::iterator it = actual_list.end();
		it--;
		char a = *it;
		it--;
		char b = *it;
		
		// build lookup pairs
		ElementPair p = ElementPair(a, b);
		map<ElementPair, char>::iterator combo_it = combinations.find(p);
		
		// deal with result
		if (combo_it != combinations.end()) {
			char new_element = combo_it->second;
			actual_list.pop_back();
			actual_list.pop_back();
			actual_list.push_back(new_element);
		} else {
			return;
		}
	}
}

void collide() {
	char last = actual_list.back();
	FOREACH (i, actual_list) {
		// build possible collision pair
		ElementPair p = ElementPair(last, *i);
		
		// se if it opposes
		if (oppositions.find(p) != oppositions.end()) {
			// clear the list
			actual_list.clear();
			return;
		}
	}
}

void solve() {
	actual_list = list<char>();
	
	// simulate the game
	FOREACH (e, invoke_list) {
		actual_list.push_back(*e);
		combine();
		collide();
	}
	
	// print resulting list
	if (actual_list.size() > 0) {
		vector<char> final_list = vector<char>(ALL(actual_list));
		printf("[");
		REP (i, final_list.size()) {
			printf("%c", final_list[i]);
			
			if (i != final_list.size() - 1) {
				printf(", ");
			}
		}
		printf("]");
	} else {
		printf("[]");
	}
}

int main(int argc, char ** argv) {
	int ncases;
	cin >> ncases;

	FOR(t, 1, ncases) {
		printf("Case #%d: ", t);
		
		// read and store combinations
		combinations = map<ElementPair, char>();
		cin >> ncombinations;
		REP (i, ncombinations) {
			char el_a, el_b, r_el;
			scanf(" %c%c%c", &el_a, &el_b, &r_el);
			ElementPair p1 = ElementPair(el_a, el_b);
			ElementPair p2 = ElementPair(el_b, el_a);
			
			combinations[p1] = r_el;
			combinations[p2] = r_el;
		}
		
		// read and store oppositions
		oppositions = map<ElementPair, bool>();
		cin >> noppositions;
		REP (i, noppositions) {
			char a, b;
			scanf(" %c%c", &a, &b);
			ElementPair p1 = ElementPair(a, b);
			ElementPair p2 = ElementPair(b, a);
			
			oppositions[p1] = true;
			oppositions[p2] = true;
		}
		
		// build to-invoke list
		invoke_list = list<char>();
		cin >> ninvoke;
		
		// skip space
		char dummy;
		scanf("%c", &dummy);
		
		// read invoke list
		REP (i, ninvoke) {
			char el;
			scanf("%c", &el);
			invoke_list.push_back(el);
		}
		
		solve();
		
		printf("\n");
	}
}
