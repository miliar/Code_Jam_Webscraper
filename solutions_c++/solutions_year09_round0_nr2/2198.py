#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>
using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef vector<double> vd;
typedef vector<char> vc;

#define ALL(t) 			t.begin(),t.end()
#define FOR(i,n) 		for(int i=0;i<(int)(n);i++)
#define FOREACH(i,t) 	for (typeof(t.begin())i=t.begin();i!=t.end();i++)

char buf[1024*1024];

struct field {
	int 	x;
	int 	y;
	int 	alt;
	char 	label;
};

bool fsort_pred(const field *left, const field *right)
{
	if(left==NULL)
		return false;
	
	if(right==NULL)
		return true;
	
	return left->alt < right->alt;
}

int main () {
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);	
	
	int t;
	
	gets(buf);
	sscanf(buf, "%d", &t);
	
	FOR(i, t) {
		int w,h;
		scanf("%d %d", &h, &w);
		
		field m[w*h];
		vector<field*> sorted;
		
		FOR(j, h) {
			FOR(k, w) {
				scanf("%d", &m[w*j+k].alt);
				m[w*j+k].label = 0;
				m[w*j+k].x = k;
				m[w*j+k].y = j;
				sorted.push_back(&m[w*j+k]);
			}
		}
		
		sort(ALL(sorted), fsort_pred);
		
		char currl = 0;
		vector<field*>::iterator it;
		FOREACH(it, sorted) {
			field *dir[5], *min;
			int j=(*it)->y, k=(*it)->x;
			if(j-1>=0) dir[1]=&m[w*(j-1)+k];	else dir[1] = NULL;
			if(k-1>=0) dir[2]=&m[w*j+k-1];		else dir[2] = NULL;
			if(k+1<w)  dir[3]=&m[w*j+k+1];		else dir[3] = NULL;
			if(j+1<h)  dir[4]=&m[w*(j+1)+k]; 	else dir[4] = NULL;
			dir[0] = *it;

			min = *min_element(dir, dir+5, fsort_pred);
			
			if((*it)->label==0) {
				if(min==(*it)) {
					(*it)->label = ++currl;
				} else {
					if(min->label!=0) {
						(*it)->label = min->label;
					} else {
						(*it)->label = min->label = ++currl;
					}
				}
			} else {
				if(min!=(*it)) {
					min->label = (*it)->label;
				}
			}
		}
	
		currl = 'a'-1;
		printf("Case #%d:\n", i+1);	
		map<char, char> lbls;
		FOR(j, h) {
			FOR(k, w) {
				field *current;
				current = &m[w*j+k];
				
				map<char, char>::iterator it = lbls.find(current->label);
				
				if(it != lbls.end()) {
					current->label = it->second;
				} else {
					lbls[current->label] = ++currl;
					current->label = lbls[current->label];
				}
				
				printf("%c ", current->label);
			}
			printf("\n");
		}
		
	}

	return 0;
}
