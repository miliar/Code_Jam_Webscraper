/*###################START INCLUDE-urile#########################/*/
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

/*###################STOP INCLUDE-urile#########################/*/
using namespace std;
/*######################START PRECODE#############################*/
const long double eps = 1e-7; // marja de eroare
const long double pi=acos(-1.0);//valoarea lui PI
typedef long long LL;
typedef unsigned long long ULL;
typedef long double LD;
typedef pair<int,int> PII;
#define PB push_back  //vector<> v.PB(X);
#define NP next_permutation //v.NP()
#define MP make_pair //MP
#define X first //.X 
#define Y second //.Y
#define ALL(a) (a).begin(), (a).end() //sort(ALL(v))
#define RALL(a) (a).rbegin(), (a).rend()//sort(RALL(v)) //sens invers
#define FORIT(it, v) for (typeof((v).begin()) it = (v).begin(); it != (v).end(); ++it) //parcurg cu iteratoru//FORIT(it, V) {cout << *it << '\n';}
#define STERGE(v) memset(v,0,sizeof v) //set 0 on something
long long BIG_INF =  0x3f3f3f3f;
#define STERGEI(v) memset(v,0x3f, sizeof(v)) //set cu infinit
//memcmp
typedef stringstream iss; //iss f(string); f>>X; sau f << X;//sau de output
/*#####################TEMPLATES##################################*/

template<class A, class B> inline A i2s(B x){stringstream s; s<<x; A r; s>>r;return r;} //string x = i2s<string, int>(X);
template<class A> inline A abs(A a) {if (a < 0) return -a; return a;} //
//__gcd(A, B) - euclidu
template<class A> inline A euclid(A a, A b, A &x, A &y) {
	if (!b) {x=1, y = 0; return a;} 
	A ret = euclid(b, a%b, x, y);
	A aux = x; 
	x = y; y = aux - (a/b)*y;
	return ret;
} ///euclid(556, 21, A, B); si A * 556 + B * 21 = gcd-ul
//de verificad daca e prim
template<class A> inline int isPrime(A X) {
	if (X <= 1 || (X % 2 == 0 && X != 2)) return 0;
	for (A i = 3; i * i <= X; i+=2) if (X % i == 0) return 0;
	return 1;
} ///isPrime(22531);


namespace X {
	/*#######-MAX FLOW JMENOS-#######*/
const int noduri =  256;
	typedef int matrice[noduri][noduri];
const int INF = 99999999;
	
	
	void max_flow_cost(int &flow, int &cost, int sink, int sursa, matrice CAPU, matrice P, vector<vector<int> > G) {
		//sterge PU si CAPU daca te doare in cot
		matrice CAP;
		memcpy(CAP, CAPU, sizeof(CAP));
		flow = 0; cost = 0;
		//P-rice
		while (1) {
			//find cu cat cresc?
			int BFS[noduri];
			memset(BFS, 0, sizeof(BFS));           
			queue<int> Q; Q.push(sursa);
			BFS[sursa]=INF;
			while (!Q.empty()) {
				int nod = Q.front(); Q.pop();
				for (int i = 0; i < G[nod].size(); ++i) {
					int nod2 = G[nod][i];
					int aux = CAP[nod][nod2];
					if (BFS[nod] < aux) aux = BFS[nod];
					if (aux <= BFS[nod2]) continue;
					BFS[nod2] = aux;
					Q.push(nod2);
				}
			}
			if (BFS[sink]==0) return; //nu se mai poate creste
			int cresc = BFS[sink];
			
			flow+=cresc;
			//find the ala cost minim care cresc .. cresc unitatzi
			//find a drum-from sink->source
			BFS[sursa] = -7;
			int pret[noduri];
			for (int i = 0; i < noduri; ++i) pret[i] = INF;           
			pret[sursa] = 0;
			while (!Q.empty()) {Q.pop();}
			Q.push(sursa);
			
			while (!Q.empty()) {
				int nod = Q.front(); Q.pop();
				//am un nod
				for (int i = 0; i < G[nod].size(); ++i) {
					int nod2 = G[nod][i]; 
					//baga o conectie de la nod -> nod2
					if (CAP[nod][nod2] < cresc) continue;
					if (pret[nod2] <= pret[nod] + P[nod][nod2] * cresc) continue;
					BFS[nod2] = nod; pret[nod2] = pret[nod] + P[nod][nod2] * cresc;
					Q.push(nod2);
				}
			}
            
			//update
			cost+=pret[sink];
			int nod = sink;
			while (1) {if (BFS[nod]==-7) break; CAP[BFS[nod]][nod]-=cresc; CAP[nod][BFS[nod]]+=cresc; nod = BFS[nod];}
			
		}
	}
	/*#######-STOP MAX FLOW JMENOS-#######*/
	/*################POLYGONU MEU FORTZOSS##########################*/
	typedef int pentruPoligon;
	struct Point {
		pentruPoligon x, y;
		Point(){};
		Point(pentruPoligon _x, pentruPoligon _y) {x = _x; y = _y;}
	};
	struct Polygon {
		vector<Point> P;
		int N;
		Polygon() {P.clear(); P.resize(0); N = 0;}
		void PolygonAdd(Point X) {P.push_back(X); N++;}
		pentruPoligon PolygonArie() {
			pentruPoligon arie = 0;
			for (int i = 1; i <= N; ++i) arie+=P[i%N].x * (P[(i-1)%N].y - P[(i+1)%N].y);
			return arie;
		}
		Polygon PolygonHull() {
			int p = 0;
			Polygon R;
			vector<int> used(N, 0);
			//leftmost point
			for (int i = 0; i < N; ++i) if (P[i].x < P[p].x) p = i;
			
			int start = p;
			R.PolygonAdd(P[p]);
			while (1) {
				int n = -1;
				pentruPoligon dist = 0;
				for (int i = 0; i < N; ++i) {
					if (i == p) continue;
					if (used[i]) continue;
					if (n == -1) n = i;
					pentruPoligon cross = 0;
					//(X[i] - X[p]) x (X[n] - X[p]);
					pentruPoligon AX = P[i].x - P[p].x;
					pentruPoligon AY = P[i].y - P[p].y;
					pentruPoligon BX = P[n].x - P[p].x;
					pentruPoligon BY = P[n].y - P[p].y;
					cross = AX * BY - AY * BX;
					
					pentruPoligon d = AX * AX + AY * AY;
					if (cross < 0) {n = i; dist = d;}
					else if (cross == 0 && d > dist) {n = i; dist = d;}
				}        
				if (n==-1) break;                                          
				p = n;
				used[p] = 1;
				if (p == start) break; //am terminat 
				R.PolygonAdd(P[p]);
			}
			return R;       
		}
	};
	/*################END_OF_POLYGONU MEU FORTZOSS##########################*/
	
	
	/*############################MAX_FLOW_FARA_COSTURI############################################*/
	//change dimenstion of matrice
#define noduri 256
	typedef int matrice[noduri][noduri];
#define INF 99999999
	
	int max_flow(int sursa, int sink, vector<vector<int> > G, matrice CAPU) {
		//sterge primele 2 linii daca vrei sa mentii modificarile in CAPacitate
		matrice CAP;
		memcpy(CAP, CAPU, sizeof(CAP));  
		int flow = 0;
		while (1) {
			//BFS 
			int BFS[noduri];
			memset(BFS, 0, sizeof(BFS));
			
			BFS[sursa] = -7;
			queue<int> Q; Q.push(sursa);
			while (!Q.empty()) {
                int nod = Q.front(); Q.pop();
                if (nod == sink) break;
                for (int i = 0; i < G[nod].size(); ++i) {
                    int nod2 = G[nod][i];
                    if (CAP[nod][nod2] <= 0 || BFS[nod2]) continue;
                    BFS[nod2] = nod;
                    Q.push(nod2);
                    if (nod2 == sink) break;
				}
                if (BFS[sink]) break;
			}
			if (BFS[sink] == 0) return flow;
			//UPDATE
			for (int i = 0; i < G[sink].size(); ++i)  {
				int nod = G[sink][i];
				if (CAP[nod][sink] <= 0 || BFS[nod] == 0) continue;
				int cresc = CAP[nod][sink];
				while (1) {if (BFS[nod] == -7) break; cresc = min(cresc,
                        CAP[BFS[nod]][nod]); nod = BFS[nod];}
				flow+=cresc;
				if (!cresc) continue;
				nod = G[sink][i];
				CAP[nod][sink]-=cresc; CAP[sink][nod]+=cresc;
				while (1) {if (BFS[nod] == -7) break; CAP[BFS[nod]][nod]-=cresc; CAP[nod][BFS[nod]]+=cresc; nod = BFS[nod];}
				
			}
		}
		return flow;
    }
	/*#############END_OF_FLUX_MAXIM######################################**/
	
	
	
	/***************************************************
	 AI de aflat maxim / min pe un interval
	 
	 /**************************************************/
#define AIMAX 400040
	typedef int AITYPE;
	
	AITYPE treeAI[AIMAX];
	void updateAI(int nod, int a, int b, int at, AITYPE val) {
		if (a > b) return;
		if (a == b) {if (at == a) treeAI[nod] = val; return;}
		if (at < a || at > b) return;
		int mij = (a + b) / 2;
		updateAI(2*nod, a, mij, at, val);
		updateAI(2*nod+1, mij+1, b, at, val);
		treeAI[nod] = 0;
		if (a <= mij) treeAI[nod] = treeAI[2*nod];
		if (mij + 1 <= b && treeAI[nod*2 + 1] > treeAI[nod]) treeAI[nod] = treeAI[2*nod+1];
	}
	AITYPE getAI(int nod, int a, int b, int l, int r) {
		if (a > b) return 0;
		if (r < a || l > b) return 0;
		if (a == b) return treeAI[nod];
		if (l <= a &&  r >= b) return treeAI[nod];
		int mij = a + b; mij /= 2;
		AITYPE mx = getAI(2*nod, a, mij, l, r);
		AITYPE mx2 = getAI(2*nod+1, mij+1, b, l, r);
		if (mx > mx2) mx2 = mx;
		return mx2;
	}
	/////////////////////////////////////////////////////////////////////
	
	
	
	/*********************************************************************888
	 AIB:
	 treeAIB - copacu de suma
	 maxAIB marimea
	 
	 /**********************************************************************/
	
	typedef int AIBTYPE;
#define maxAIB 1000070
	
	AIBTYPE treeAIB[maxAIB];
	
	AIBTYPE getAIB(int idx) {
        AIBTYPE sum = 0; // the sum
        while (idx > 0) {
			sum += treeAIB[idx];
			idx -= (idx & -idx);
		}
        return sum;
	}
	void updateAIB(int idx, AIBTYPE val){
		while (idx <= maxAIB){
			treeAIB[idx] += val;
			idx += (idx & -idx);
		}
	}
	
	////////////////////////////////////////////////////////////////////////
	
	
	/////////////////////////////////////////////////////////////////////////////////////
	
	/*********************************************
	 Set:
	 use vset and rankset, 
	 create_set - initializare un nod
	 find_set - afla reprezentativu si normalizeaza
	 join - join 2 seturi 
	 Freebugs I hope
	 /*********************************************/
	
	
	
	int vset[1000001];
	int rankset[1000001];
	int create_set(int x) {
		vset[x] = x;
		rankset[x] = 0;
    }
	int find_set(int x) {
		if (x != vset[x]) vset[x] = find_set(vset[x]);
		return vset[x];
	}
	void join(int x, int y) {
		x = find_set(x);
		y = find_set(y);
		if (rankset[x] > rankset[y]) vset[y] = x;
		else vset[x] = y;
		if (rankset[x] == rankset[y]) rankset[y]++;
	}
	
	
	
	
	////////////////////////////////////////////////////////////////////////////////////
	
	/********************************************
	 Type: Graph, defines a graph type:
	 - lista de adiacentza
	 - n numarul de noduri
	 1 la n
	 /********************************************/
	typedef struct {
        vector<vector<int> > E; //muchiile
        vector<int> degree;     //gradele
        int n;                  //numarul de noduri
        
        void init(int _n) //initializeaza un graph gol cu N noduri
        {
			E.resize(_n + 3);
			degree.resize(_n + 3);
			n = _n;
		}
        void addEdge(int a, int b) //pune edge de la a la b
        {
			++degree[a];
			E[a].push_back(b);
		}
        //DFS algorithm - only if initiated
        vector<int> processed; //contine -1, sau componenta din care face parte
        int componente;        //contine numarul de componnete
        void initDFS() {processed.resize(n + 3, -1); componente = 0;}
        void eraseDFS() {processed.clear();} //erase de DFS, to clear memory
        
        void runDFS(int nod, int color)
        {
			if (processed[nod] != -1) return;
			processed[nod] = color;
			for (int i = 0; i < degree[nod]; ++i) runDFS(E[nod][i], color);     
			
		}
		
        void dfs() {
			initDFS(); //initiaza
			for (int i = 1; i <= n; ++i) if (processed[i] == -1) 
			{
				++componente;
				runDFS(i, componente);
			}             
		}
	} graph;
	
	
	
	
	//////////////////////////////////////////////////////////////////
	/**********************************************************************
	 Implemented trie: works with alphabet on chars
	 create a root
	 use addWord(root, "word", 1998);
	 use findWord(root, "word"); //-1 sau valuare
	 
	 HOW TO USE:
	 
	 trie *root = new trie;
	 init(root);
	 root->key = '*';
	 addWord(root, "ana", 20);  
	 addWord(root, "anna", 30);
	 addWord(root, "gika", 27);
	 cout <<    findWord(root, "a") << '\n';
	 cout <<    findWord(root, "an")<< '\n';
	 cout <<    findWord(root, "ana")<< '\n';
	 cout <<    findWord(root, "anaa")<< '\n';
	 cout <<    findWord(root, "anna")<< '\n';
	 cout <<    findWord(root, "gika") << '\n';
	 
	 ***********************************************************************/
	
	typedef struct trie{
        char key;
        int value;
        struct trie *next, *child; //points to the next one and to the child if any
	} trie;
	void init(trie *nod) 
	{
		nod->child = nod->next = NULL;
		nod->key = 0;
		nod->value = 0;
	}
	void addWord(trie *nod, char *s, int val) 
	{
		//find s[0] pe nivelu actual
		
		trie *ref = nod;
		char C = 0; C = s[0];
		while (ref != NULL) {if (ref->key == C) break; ref = ref->next;}
		
		if (ref == NULL) {
			trie *nou = new trie;
			init(nou);
			nou->value = val; nou->key = C;
			trie *kido = new trie;
			nou->child = kido;
			kido->child=NULL; kido->next=NULL;kido->key='*';kido->value = -99;
			nou->next = nod->next;
			nod->next = nou;
			ref = nou;
		};
		//found
		
		if (C == 0) {ref->value = val; return;}
		addWord(ref->child, s+1, val);
	}
	int findWord(trie *nod, char* s) 
	{
		trie *ref = nod;
		char C = 0; C = s[0];
		while (ref != NULL) {if (ref->key == C) break; ref = ref->next;}
		
		if (ref == NULL) return -1; //not found
		if (C == 0) return ref->value;
		return findWord(ref->child, s+1);
    }
    
	
	///////////////////////////////////////////////////////////////////////////
}
/*######################STOP PRECODE#############################*/
void solve();
int main() {
	int t;
	scanf("%d\n", &t);
	for (int i = 1; i <= t; ++i) {
		printf("Case #%d: ", i);
		solve();
	}
	return 0;
}
int n, k;

int v[100][100];
int r[100][100];

int di[] = {0, 0, 1, 1,1, -1, -1, -1};
int dj[] = {1, 1, 0, 1, -1, 0, 1, -1};

void raspuns(int a, int b) {
	if (a == 0 && b == 0) cout << "Neither\n";
	if (a == 0 && b == 1) cout << "Blue\n";
	if (a == 1 && b == 0) cout << "Red\n";
	if (a == 1 && b == 1) cout << "Both\n";
}
void rotate() {
//	for (int i = 0; i < n; ++i)
//		for (int j = 0; j < n; ++j) r[i][j] = v[j][n - i - 1];

	while (1) {
		int f = 0;

		for (int i = 0; i < n; ++i)
			for (int j = 0; j + 1 < n; ++j) if (v[i][j] && !v[i][j + 1]) {
				f = 1;
				v[i][j + 1] = v[i][j];
				v[i][j] = 0;
			}
		if (f == 0) break;
	}
}
void solve() {
	cin >> n >> k;

	int i, j;
	for (i = 0; i < n; ++i)
		for (j = 0; j < n; ++j) {
			char c;
			cin >> c;
			if (c == '.') v[i][j] = 0;
			if (c == 'R') v[i][j] = 1;
			if (c == 'B') v[i][j] = 2;
		}
	rotate();

	int sol[] = {0, 0, 0};

	for (int i = 0; i < n; ++i) 
		for (int j = 0; j < n; ++j)
			for (int d = 0; d < 8; ++d) {
				int st = v[i][j];
				int cate = 1;

				int nx = i, ny = j;
				for (int lo = 1; lo < k; ++lo) {
					nx = nx + di[d];
					ny = ny + dj[d];
					if (nx >= n || ny >= n) break;
					if (nx < 0 || ny < 0) break;
					cate += (v[nx][ny] == st);
				}

				if (cate == k) sol[st] = 1; 
			}

	raspuns(sol[1], sol[2]);
}
