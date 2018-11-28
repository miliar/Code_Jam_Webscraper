/*
 * Magicka.cpp
 *
 *  Created on: 07/05/2011
 *      Author: francisco
 */

#include <stdio.h>
#include <vector>
#include <set>

unsigned int t,nc,c,d,n,i,j;
char aux;

struct oppose {
	char a;
	char b;
} op;

struct combination {
	char a;
	char b;
	char r;
} co;

struct cmp {
	bool operator()(const combination &a, const combination &b) {
		if(a.a == b.a) return a.b < b.b;
		return a.a < b.a;
	}
};

struct comp {
	bool operator()(const oppose &a, const oppose &b) {
		if(a.a == b.a) return a.b < b.b;
		return a.a < b.a;
	}
};

std::set<combination,cmp> sc;
std::set<combination,cmp>::iterator itc;
std::set<oppose,comp> so;
std::set<oppose,comp>::iterator ito;
std::vector<char> v;
std::vector<char>::size_type sz;

bool invoke(const char& e, const char& f, char& g) {
	for(itc = sc.begin(); itc != sc.end(); itc++) {
		if( (itc->a == e && itc->b == f) || (itc->a == f && itc->b == e) ) {
			g = itc->r;
			return true;
		}
	}
	return false;
}

bool conflict(const char& e, const char& f) {
	for(ito = so.begin(); ito != so.end(); ito++) {
		if( (ito->a == e && ito->b == f) || (ito->a == f && ito->b == e) ) {
			return true;
		}
	}
	return false;
}

void test(const char& x) {
	sz = v.size();
	if(sz) {
		if(invoke(x,v[sz-1],aux)) {
			v[sz-1] = aux;
			return;
		}
		for(j = 0; j < sz; j++) {
			if(conflict(x,v[j])) {
				v.clear();
				return;
			}
		}
	}
	v.push_back(x);
}

int main(void) {

	scanf("%d",&t);
	for(nc = 1; nc <= t; nc++) {
		scanf("%d ",&c);
		for(i = 0; i < c; i++) {
			scanf("%c%c%c ",&co.a,&co.b,&co.r);
			if(co.a > co.b) {
				aux = co.a;
				co.a = co.b;
				co.b = aux;
			}
			sc.insert(co);
		}
		scanf("%d ",&d);
		for(i = 0; i < d; i++) {
			scanf("%c%c ",&op.a,&op.b);
			if(op.a > op.b) {
				aux = op.a;
				op.a = op.b;
				op.b = aux;
			}
			so.insert(op);
		}
		scanf("%d ",&n);
		for(i = 0; i < n; i++) {
			scanf("%c",&aux);
			test(aux);
		}
		printf("Case #%d: [",nc);
		sz = v.size();
		if(sz) printf("%c",v[0]);
		for(i = 1; i < sz; i++) {
			printf(", %c",v[i]);
		}
		printf("]\n");
		v.clear();
		sc.clear();
		so.clear();
	}
	return 0;
}
