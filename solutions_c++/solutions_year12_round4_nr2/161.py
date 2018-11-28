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

struct Guy {
   double r,x,y;
   int index;
   inline bool operator < (const Guy &g) const {
      if (r != g.r) return r < g.r;
      return index < g.index;
   }
};

double randDouble()
{
  double out;
  out = (double)rand()/(RAND_MAX + 1); //each iteration produces a number in [0, 1)
  out = (rand() + out)/RAND_MAX;
  out = (rand() + out)/RAND_MAX;
  out = (rand() + out)/RAND_MAX;
  out = (rand() + out)/RAND_MAX;
  out = (rand() + out)/RAND_MAX;

  return out;
}


#include <pthread.h>
#include <semaphore.h>
#define PARALLEL 1
#define CORES 3
struct Instance {
   pthread_mutex_t finished;
   Instance() : finished(PTHREAD_MUTEX_INITIALIZER) { pthread_mutex_lock(&finished); }
   
   // define variables here
   int n, w, l;
   Guy guy[1007];
   
   void readInput() { // should read input; will run sequentially
      cin >> n >> w >> l;
      FOR(i,n) {
         cin >> guy[i].r;
         guy[i].index = i;
      }
   }
   
   inline double sqr (double x) { return x*x; }
   
   inline bool wrong (int i, int j) {
      return sqr(guy[i].x - guy[j].x) + sqr(guy[i].y - guy[j].y) < sqr(guy[i].r + guy[j].r);
   }
   
   bool go (int i) {
      if (i == n) return 1;
      FOR(tries,3) {
         guy[i].x = randDouble() * w;
         guy[i].y = randDouble() * l;
         bool ok = 1;
         FOR(j,i) {
            if (wrong(j,i)) {
               ok = 0;
               break;
            }
         }
         if (ok) if (go(i+1)) return 1;
      }
      return 0;
   }
   
   bool res;
   void compute() { // should produce output and store it, not use IO; will run in parallel
      sort(guy,guy+n);
      reverse(guy,guy+n);
      guy[0].x = guy[0].y = 0;
      res = go(1);
   }
   
   void writeOutput () { // should write stored output, without newline; will run sequentially
      if (res == 0) cerr << "FAIL"; else {
      double outx[1007], outy[1007];
      FOR(i,n) {
         outx[guy[i].index] = guy[i].x;
         outy[guy[i].index] = guy[i].y;
      }
      FOR(i,n) {
         cout << setprecision(9) << fixed << outx[i] << " " << outy[i];
         if (i != n-1) cout  << " ";
      }
   }
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
