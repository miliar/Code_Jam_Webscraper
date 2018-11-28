#include <iostream>
#include <cstdio>
#include <string>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <cmath>
#include <algorithm>
#include <sstream>
#include <stack>
#include <cstring>
#include <iomanip>
#include <ctime>
using namespace std;
#define pb push_back
#define INF 1000000000
#define FOR(i,n) for(int (i)=0;(i)<(n);++(i))
#define FORI(i,n) for(int (i)=1;(i)<=(n);++(i))
#define mp make_pair
#define pii pair<int,int>
#define ll long long
#define vi vector<int>
#define SZ(x) ((int)(x.size()))
#define fi first
#define se second
#define wez(n) int (n); scanf("%d",&(n));
#define wez2(n,m) int (n),(m); scanf("%d %d",&(n),&(m));
#define wez3(n,m,k) int (n),(m),(k); scanf("%d %d %d",&(n),&(m),&(k));
inline void pisz(int n) { printf("%d\n",n); }
template<typename T,typename TT> ostream& operator<<(ostream &s,pair<T,TT> t) {return s<<"("<<t.first<<","<<t.second<<")";}
template<typename T> ostream& operator<<(ostream &s,vector<T> t){FOR(i,SZ(t))s<<t[i]<<" ";return s; }
#define IN(x,y) ((y).find((x))!=(y).end())
#define DBG(vari) cerr<<#vari<<" = "<<(vari)<<endl;
#define ALL(t) t.begin(),t.end()
#define FOREACH(i,t) for (typeof(t.begin()) i=t.begin(); i!=t.end(); i++)
#define TESTS wez(testow)while(testow--)
#define REP(i,a,b) for(int (i)=(a);(i)<=(b);++i)
#define REPD(i,a,b) for(int (i)=(a); (i)>=(b);--i)
#define REMAX(a,b) (a)=max((a),(b));
#define REMIN(a,b) (a)=min((a),(b));
#define IOS ios_base::sync_with_stdio(0);

// zastąpić tym maina
// wypełnić readInput(), compute() i writeOutput(); zmienne definiować wewnątrz klasy Instance
// PARALLEL - czy ma odpalić testy równolegle, CORES - liczba rdzeni
// uwaga - wersja równoległa może potrzebować dużo pamięci! (T razy więcej)
//         mozna sobie z tym poradzić tworząc duże tablice dynamicznie dopiero w compute()
//         (bo naraz wykonywane są co najwyżej CORES=3 kopie compute())
//         (pamiętać o delete [] na koniec compute)
// linkować z pthreads

#include <pthread.h>
#include <semaphore.h>
#define PARALLEL 0
#define CORES 3
struct Instance {
   pthread_mutex_t finished;
   Instance() : finished(PTHREAD_MUTEX_INITIALIZER) { pthread_mutex_lock(&finished); }
   
   // define variables here
   int k, res;
   string s;
   bool adj[300][300], wyst[300];
   
   void readInput() { // should read input; will run sequentially
      cin >> k >> s;
   }
   
   /*void dfs (int v) {
      if (seen[v]++) return;
      int indeg = 0, outdeg = 0;
      FOR(c,300) {
         if (adj[v][c]) ++outdeg;
         if (adj[c][v]) ++indeg;
      }
      sumdiffs += abs(indeg - outdeg);
   }*/
   
   bool leet (char c) {
      return c == 'o' || c == 'i' || c == 'e' || c == 'a' || c == 's' || c == 't' || c == 'b' || c == 'g';
   }
   
   void compute() { // should produce output and store it, not use IO; will run in parallel
      if (k != 2) return;
      int n = SZ(s);
      FOR(c,300) FOR(d,300) adj[c][d] = 0;
      FOR(i,n-1) {
         vector<char> v,w;
         v.pb(s[i]);
         w.pb(s[i+1]);
         if (leet(s[i])) {
            v.pb(s[i] + 'A' - 'a');
         }
         if (leet(s[i+1])) {
            w.pb(s[i+1] + 'A' - 'a');
         }
         //DBG(v)DBG(w)
         FOREACH(it,v) FOREACH(jt,w) {
            adj[*it][*jt] = 1;
         }
      }
      FOR(c,300) wyst[c] = 0;
      FOR(i,n) wyst[s[i]] = 1;
      int sd = 0, kr = 0;
      FOR(v,300) {
         int indeg = 0, outdeg = 0;
         FOR(c,300) {
            if (adj[v][c]) ++outdeg, ++kr;
            if (adj[c][v]) ++indeg;
         }
         sd += abs(indeg - outdeg);
      }
      res = 1 + max(0, sd/2 - 1);
      res += kr;
   }
   
   void writeOutput () { // should write stored output, without newline; will run sequentially
      if (k != 2) { cout << "nie"; return; }
      cout << res;
   }
};

Instance *instances;
sem_t coreSemaphore;
pthread_mutex_t cerr_lock = PTHREAD_MUTEX_INITIALIZER;

void* runner (void* input) {
   int testno = *reinterpret_cast<int*>(input);
   sem_wait(&coreSemaphore);
   instances[testno].compute();
   pthread_mutex_lock(&cerr_lock);
   cerr << "test " << testno+1 << " is finished" << endl;
   pthread_mutex_unlock(&cerr_lock);
   pthread_mutex_unlock(&instances[testno].finished);
   sem_post(&coreSemaphore);
   return 0;
}

int main () {
   string pierwszalinia;
   getline(cin,pierwszalinia);
   int tests = atoi(pierwszalinia.c_str());
   if (PARALLEL) {
      instances = new Instance[tests];
      // reading input
      FOR(i,tests) {
         instances[i].readInput();
      }
      
      // running computations in parallel
      sem_init(&coreSemaphore, 0, CORES);
      pthread_t irrelevant;
      FOR(i,tests) pthread_create(&irrelevant, NULL, runner, new int(i));
      FOR(i,tests) pthread_mutex_lock(&instances[i].finished); // wait until all are finished
      
      // writing output
      FOR(i,tests) {
         printf("Case #%d: ", i+1);
         instances[i].writeOutput();
         printf("\n");
      }
   } else {
      FOR(i,tests) {
         instances = new Instance;
         instances->readInput();
         instances->compute();
         printf("Case #%d: ", i+1);
         instances->writeOutput();
         printf("\n");
         cerr << "test " << i+1 << " is finished" << endl;
         delete instances;
      }
   }
}
