#include <iostream>
#include <queue>
#include <set>
#include <vector>
#include <string>

using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 

class PushRelabel {
public:
  PushRelabel(int numVertices);
  ~PushRelabel();
  void addEdge(int i, int j, int cap);
  void initialize_preflow();
  void push(int u, int v);
  void relabel(int u);
  void runalg(int source, int sink);
  int maxFlow(){ return e[t]; }
  int** flow() { return f; }
private:
  int n;
  int* h;
  int* e;
  int** f;
  set<int>* G;
  int** c;
  int** cf;
  int s;
  int t;
};

PushRelabel::PushRelabel(int numVertices){
  n = numVertices;
  h = new int[n];
  e = new int[n];
  G = new set<int>[n];
  f = new int*[n];
  c = new int*[n];
  cf = new int*[n];
  for (int i = n-1; i >= 0; --i){
    f[i] = new int[n];
    c[i] = new int[n];
    cf[i] = new int[n];
    memset(c[i],0,sizeof(int)*n);
  }
}

PushRelabel::~PushRelabel(){
  delete[] h; delete[] e; delete[] G;
  for (int i = 0; i < n; ++i){
    delete[] f[i]; delete[] c[i]; delete[] cf[i];
  }
  delete[] f; delete[] c; delete[] cf;
}

void PushRelabel::addEdge(int i, int j, int cap){
  if (present(G[i],j)){
    c[i][j] += cap;
  } else {
    G[i].insert(j);
    G[j].insert(i);
    c[i][j] = cap;
  }
}

void PushRelabel::initialize_preflow() {
  memset(h,0,sizeof(int)*n);
  h[s] = n;
  memset(e,0,sizeof(int)*n);	
  for (int i = n-1; i >= 0; --i){
    memset(f[i],0,sizeof(int)*n);
    for (int j = n-1; j >= 0; --j)
      cf[i][j] = c[i][j];
  }
  tr(G[s],v){
    f[s][*v] = c[s][*v];
    f[*v][s] = -c[s][*v];
    e[*v] = c[s][*v];
    e[s] -= c[s][*v];
    cf[s][*v] = c[s][*v] - f[s][*v];
    cf[*v][s] = c[*v][s] - f[*v][s]; 
  }
}

void PushRelabel::push(int u, int v) {
  int temp = min(e[u],cf[u][v]);
  f[u][v] += temp; f[v][u] -= temp;
  e[v] += temp; e[u] -= temp;
  cf[v][u] += temp; cf[u][v] -= temp;
}

void PushRelabel::relabel(int u){
  h[u] = 0;
  tr(G[u],v)
    if (cf[u][*v] > 0)
      if (h[u] == 0 || h[u] > 1 + h[*v])
	h[u] = 1 + h[*v];
}


void PushRelabel::runalg(int source, int sink) {
  s = source;
  t = sink;
  initialize_preflow();
  queue<int> q;
  char* l = new char[n];
  int u,m;
  memset(l,0,sizeof(char)*n);
  tr(G[s], w)
    if (*w != t) {
      q.push(*w);
      l[*w] = 1;
    }
  while (q.size() != 0) {
    u = q.front();
    m = -1;
    for (set<int>::iterator v = G[u].begin(); v != G[u].end() && e[u] > 0; ++v) {
      if (cf[u][*v] > 0) {
	if (h[u] > h[*v]) {
	  push(u,*v);
	  if (l[*v] == 0 && *v != s && *v != t) {
	    l[*v] = 1;
	    q.push(*v);
	  }
	}
	else if (m == -1 || m > h[*v]) m = h[*v]; 
      }
    }
    if (e[u] != 0) h[u] = 1 + m;
    else {
      l[u] = 0;
      q.pop();
    }
    for (int x = 0; x < 1<<31; ++ x);
  }
}

int main(){
  int N;
  cin >> N;
  for (int iZ = 0; iZ < N; ++iZ){
    int R,C;
    cin >> R >> C;
    PushRelabel x = 2+(R*C);
    int n = 0;
    for (int i = 0; i < R; ++i){
      string s;
      cin >> s;
      for (int j = 0; j < C; ++j){
	if (s[j] == '.'){
	  ++n;
	  if (j % 2 == 0){
	    x.addEdge(0,i*C+j+1,1);
	    if (j > 0)
	      x.addEdge(i*C+j+1,i*C+j,1);
	    if (j < C-1)
	      x.addEdge(i*C+j+1,i*C+j+2,1);
	    if (i > 0){
	      if (j > 0)
		x.addEdge(i*C+j+1,(i-1)*C+j,1);
	      if (j < C-1)
		x.addEdge(i*C+j+1,(i-1)*C+j+2,1);
	    }
	    if (i < R - 1){
	      if (j > 0)
		x.addEdge(i*C+j+1,(i+1)*C+j,1);
	      if (j < C-1)
		x.addEdge(i*C+j+1,(i+1)*C+j+2,1);
	    }
	  } else {
	    x.addEdge(i*C+j+1,R*C+1,1);
	  }
	}
      }
    }
    x.runalg(0,R*C+1);
    cout << "Case #" << (iZ+1) << ": ";
    cout << n - x.maxFlow();
    cout << endl;
  }
}


