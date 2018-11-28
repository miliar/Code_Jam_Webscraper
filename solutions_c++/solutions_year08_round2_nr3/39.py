/* Peter Zielinski, Jagiellonian University, Poland */

#include <cstdio>
#include <queue>
#include <list>
#include <set>
#include <algorithm>
#include <deque>
#include <utility>
#include <cstring>
#include <ctime>
#include <cstdlib>
using namespace std;

#define FOR(i,a,b) for (int i=(a); i<(int)(b); ++i)
#define FORD(i,a,b) for (int i=(a)-1; i>=(int)(b); --i)
#define FORE(i,x) for (__typeof((x).begin()) i=(x).begin(); i!=(x).end(); ++i)
#define PB push_back
#define MP make_pair
#define FI first
#define SE second
typedef long long ll;

/* my treap :) */

template<class T>
		class drzewko {
	class wezel {
		public:
			T v;
			int rank, size;
			wezel* next[2];
			wezel(T x, int r) {
				v = x;  // wartosc trzymana w wezle
				rank = r;  // losowo wyznaczona ranga elementu
				size = 1; // poczatkowy rozmiar poddrzewa
				next[0] = next[1] = 0;
			}
	};

	wezel* root;
	void rotuj(wezel*& g, int strona) {
		wezel* tmp = g->next[strona^1];
		g->next[strona^1] = tmp->next[strona];
		tmp->next[strona] = g;
		g = tmp;
	}
  
	void clearR(wezel*& g) {
		if(!g) return;
		clearR(g->next[0]);
		clearR(g->next[1]);
		delete g;
	}
  
	void wypiszR(wezel* g) {
		if(!g) return;
		wypiszR(g->next[0]);
		printf("%d ", g->v);
		wypiszR(g->next[1]);
	}
  
	wezel*& findR(wezel*& g, T x) {
		if(!g || g->v == x) return g;
		return g->v < x ? findR(g->next[1],x) : findR(g->next[0],x);
	}
  
	int losuj() {
		return rand()%RAND_MAX;
	}
  
	int get_rank(wezel*& g) {
		if(!g) return -1;
		return g->rank;
	}
  
	int get_size(wezel*& g) {
		if(!g) return 0;
		return g->size;
	}
  
	void popraw_size(wezel*& g) {
		if(!g) return;
		g->size = get_size(g->next[0]) + get_size(g->next[1]) + 1;
	}
  
	void insertR(wezel*& g, T x) {	
		if(!g) { g = new wezel(x, losuj()); return; }
		if(g->v < x) insertR(g->next[1],x);
		else insertR(g->next[0],x);
		if(get_rank(g->next[0]) > get_rank(g->next[1]) && get_rank(g->next[0]) > g->rank) rotuj(g,1);
		else if(get_rank(g->next[1]) > get_rank(g->next[0]) && get_rank(g->next[1]) > g->rank) rotuj(g,0);
		popraw_size(g->next[0]);
		popraw_size(g->next[1]);
		popraw_size(g);
	}
  
	int glebokoscR(wezel*& g) {
		if(!g) return 0;
		return max(glebokoscR(g->next[0]), glebokoscR(g->next[1])) +1;
	}
  
	void usunR(wezel*& g, T x) {
		if(!g) return;
		if(g->v < x) usunR(g->next[1],x);
		else if(g->v > x) usunR(g->next[0],x);
		--(g->size);
	}
  
	wezel*& kty_elementR(wezel*& g, int nr) {
		if(get_size(g->next[0]) == nr-1) return g;
		if(get_size(g->next[0]) < nr) return kty_elementR(g->next[1], nr-(get_size(g->next[0])+1));
		return kty_elementR(g->next[0], nr);
	}
  
	int ktoryR(wezel*& g, T x) {
		if(g->v == x) return 1+get_size(g->next[0]);
		if(g->v < x) return get_size(g->next[0])+1+ktoryR(g->next[1],x);
		return ktoryR(g->next[0],x);
	}
  
	wezel*& nast(wezel*& g) {
		if(!g) return g;
		if(g->next[0]) return nast(g->next[0]);
		return g;
	}

  // najwiekszy SILNIE mniejszy
	wezel*& lower_boundR(wezel*& g, T x) {
		if(!g) return g;
		if(g->v < x) {
			wezel*& res = lower_boundR(g->next[1],x);
			if(res) return res;
			return g;
		}
		return lower_boundR(g->next[0],x);
	}
  
  // najmniejszy SILNIE wiekszy
	wezel*& upper_boundR(wezel*& g, T x) {
		if(!g) return g;
		if(g->v < x || g->v == x) return upper_boundR(g->next[1],x);
		wezel*& res = upper_boundR(g->next[0],x);
		if(res) return res;
		return g;
	}
  
  // INTERFEJS
			public:
	
				drzewko() { root = 0; }
	
				~drzewko() { clearR(root); }
	
				int size() { return get_size(root); }
	
				void insert(T x) {
					insertR(root,x);
				}
	
				wezel*& find(T x) {
					return findR(root, x);
				}
	
				void clear() {
					clearR(root);
					root = 0;
				}	
	
				int glebokosc() {
					return glebokoscR(root);
				}
	
				T lower_bound(T x) {
					wezel*& res = lower_boundR(root,x);
					if(!res) return x;
					return res->v;
				}
	
				T upper_bound(T x) {
					wezel*& res = upper_boundR(root,x);
					if(!res) return x;
					return res->v;
				}
	
				void erase(T x) {
					wezel*& tmp = findR(root, x);
					wezel*& nastepnik = nast(tmp->next[1]);
					wezel *r;
					if(!nastepnik) {
						r = tmp->next[0];
						usunR(root,tmp->v);
						delete tmp;
						tmp = r;
					} else {
						usunR(root, nastepnik->v);
						tmp->v = nastepnik->v;
						r = nastepnik->next[1];
						delete nastepnik;
						nastepnik = r;
					}
				}
	
				T kty_element(int nr) {
					return kty_elementR(root,nr)->v;  
				}
	
				int ktory(T x) {
					return ktoryR(root,x);
				}
	
				void wypisz() {
					wypiszR(root);
				}
		};

int res[1000000];

void testcase() {
	srand(time(NULL));
	vector<int> quest;
	int k, n;
 	scanf("%d%d", &k, &n);
	FOR(i,0,n) { int x; scanf("%d", &x); quest.PB(x); }
	fill_n(res,k,0);
	int latacz = 0, zuzytych = 0;
	drzewko<int> zbiorek;
	FOR(i,0,k) zbiorek.insert(i);
	int przesuniecie = 0;
	FOR(i,0,k) {
		int ktory = i+przesuniecie;
		if(ktory >= zbiorek.size()) ktory %= zbiorek.size();
		int gdzie = zbiorek.kty_element(ktory+1);
		przesuniecie = ktory;
		res[gdzie] = i+1;
		zbiorek.erase(gdzie);
	}
	FORE(it,quest) printf("%d ", res[(*it)-1]);
}

int main() {
  int t;
  scanf("%d", &t);
  FOR(i,0,t) {
	printf("Case #%d: ", i+1);
	testcase();
	printf("\n");
  }
  return 0;
}
