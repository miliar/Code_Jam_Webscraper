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

char co[300];

#include <pthread.h>
#include <semaphore.h>
#define PARALLEL 0
#define CORES 3
struct Instance {
   pthread_mutex_t finished;
   Instance() : finished(PTHREAD_MUTEX_INITIALIZER) { pthread_mutex_lock(&finished); }
   
   // define variables here
   string line, out;
   
   void readInput() { // should read input; will run sequentially
      getline(cin,line);
   }
   
   void compute() { // should produce output and store it, not use IO; will run in parallel
      FOR(i,SZ(line)) {
         out += co[line[i]];
      }
   }
   
   void writeOutput () { // should write stored output, without newline; will run sequentially
      cout << out;
   }
};

Instance *instances;
sem_t coreSemaphore;

void* runner (void* input) {
   int testno = *reinterpret_cast<int*>(input);
   sem_wait(&coreSemaphore);
   instances[testno].compute();
   cerr << "test " << testno+1 << " is finished" << endl; // synchronizowac to!
   pthread_mutex_unlock(&instances[testno].finished);
   sem_post(&coreSemaphore);
   return 0;
}

int main () {
   string a[4],b[4];
   a[0]="ejpmysljylckdkxveddknmcrejsicpdrysi";
   b[0]="ourlanguageisimpossibletounderstand";
   a[1]="rbcpcypcrtcsradkhwyfrepkymveddknkmkrkcd";
   b[1]="therearetwentysixfactorialpossibilities";
   a[2]="dekrkdeoyakwaejtysrreujdrlkgcjv";
   b[2]="soitisokayifyouwanttojustgiveup";
   a[3]="yqee";
   b[3]="azoo";
   FOR(i,300) co[i] = '-';
   co[' ']=' ';
   FOR(u,4) FOR(i,SZ(a[u])) {
      co[a[u][i]] = b[u][i];
   }
   vector<bool> occ(300,0);
   //for (char c = 'a'; c <= 'z'; ++c) { DBG(c) DBG(co[c]) }
   for (char c = 'a'; c <= 'z'; ++c) { //DBG(c) DBG(co[c]) }
      occ[co[c]]=1;
   }
   for (char c = 'a'; c <= 'z'; ++c) {
      if (!occ[c]) co['z'] = c;
   }
   //for (char c = 'a'; c <= 'z'; ++c) { DBG(c) DBG(co[c]) }



   int tests;
   scanf("%d",&tests);
   char buf[20];
   cin.getline(buf,10);
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
