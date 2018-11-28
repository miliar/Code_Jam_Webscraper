#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
#include <map>

//#define dprintf(...) printf(__VA_ARGS__)
#define dprintf(...)

using namespace std;

struct state {
	int p;
	set<int> torel;
	set<int> rel;
};

typedef multimap<int,state> states_map;

states_map states;

void expand_states(int br,state cur) {
	state tmp;
	int bribe;
	set<int>::iterator it,bound;
	pair<set<int>::iterator,set<int>::iterator> range;

	dprintf("Expanding states with current bribe %d\n",br);
	for(it=cur.torel.begin();it!=cur.torel.end();it++) {
		bribe=0;
		tmp=cur;
		range=tmp.rel.equal_range(*it);
		bound=range.first;
		dprintf("Testing lower bound of %d...\n",*it);
		if((bound==tmp.rel.begin())) {
			bribe+=(*it)-1;
		} else {
			bound--;
			bribe+=(*it)-(*bound)-1;
		}
		bound=range.second;
		dprintf("Testing higher bound of %d...\n",*it);
		if(bound==tmp.rel.end()) {
			bribe+=cur.p-(*it);
		} else {
			bribe+=(*bound)-(*it)-1;
		}
		tmp.rel.insert(*it);
		tmp.torel.erase(*it);
		states.insert(make_pair(br+bribe,tmp));
		dprintf("After releasing prisoner %d bribe is %d\n",*it,bribe);
	}
}

void search() {
	int bribe;
	state tmp;
	states_map::iterator it;

	it=states.begin();
	while(!(it->second.torel.empty())) {
		bribe=it->first;
		tmp=it->second;
		states.erase(it);
		expand_states(bribe,tmp);
		it=states.begin();
	}
	printf("%d\n",it->first);
}

int main(void) {
	int cases,i,j,tmp,p,q;
	bool changed;
	state cur;
	scanf("%d\n",&cases);
	dprintf("%d cases to proceed\n",cases);
	for(i=1;i<=cases;i++) {
		scanf("%d %d\n",&p,&q);
		dprintf("Case %d has p=%d and q=%d\n",i,p,q);
		cur.p=p;
		cur.torel.clear();
		cur.rel.clear();
		states.clear();
		printf("Case #%d: ",i);
		for(j=0;j<q;j++) {
			scanf("%d",&tmp);
			cur.torel.insert(tmp);
		}
		dprintf("Got %d prisons to open\n",cur.torel.size());
		expand_states(0,cur);
		search();
	}
	return 0;
}
