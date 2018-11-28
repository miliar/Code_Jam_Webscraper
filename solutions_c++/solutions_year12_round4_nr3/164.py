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
#define VI vector<int>
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

const double EPS = 10e-9;
namespace Simplex{
// Typ wykorzystywany do wykonywania obliczeñ - domyslnie jest to long double
  typedef long double T;
  typedef vector<T> VT;
  vector<VT> A;
  VT b,c,res;
  VI kt,N;
  int m;
  inline void pivot(int k,int l,int e){
      int x=kt[l]; T p=A[l][e];
      FOR(i,k) A[l][i]/=p; b[l]/=p; N[e]=0;
      FOR(i,m) if (i!=l) b[i]-=A[i][e]*b[l],A[i][x]=A[i][e]*-A[l][x];
      FOR(j,k) if (N[j]){
        c[j]-=c[e]*A[l][j];
        FOR(i,m) if (i!=l) A[i][j]-=A[i][e]*A[l][j];
      }
      kt[l]=e; N[x]=1; c[x]=c[e]*-A[l][x];
  }
  VT doit(int k){
    VT res; T best;
    while (1){
      int e=-1,l=-1; FOR(i,k) if (N[i] && c[i]>EPS) {e=i; break;}
      if (e==-1) break;
      FOR(i,m) if (A[i][e]>EPS && (l==-1 || best>b[i]/A[i][e]))
        best=b[ l=i ]/A[i][e];
      if (l==-1) 
		return VT();
      pivot(k,l,e);
    }
    res.resize(k,0); FOR(i,m) res[kt[i]]=b[i];
    return res;
  }
  VT simplex(vector<VT> &AA,VT &bb,VT &cc){
    int n=AA[0].size(),k;
    m=AA.size(); k=n+m+1; kt.resize(m); b=bb; c=cc; c.resize(n+m);
    A=AA; FOR(i,m){ A[i].resize(k); A[i][n+i]=1; A[i][k-1]=-1; kt[i]=n+i;}
    N=VI(k,1); FOR(i,m) N[kt[i]]=0;
    int pos=min_element(ALL(b))-b.begin();
    if (b[pos]<-EPS){ 
      c=VT(k,0); c[k-1]=-1; pivot(k,pos,k-1); res=doit(k);
      if (res[k-1]>EPS) return VT();
      FOR(i,m) if (kt[i]==k-1)
          FOR(j,k-1) if (N[j] && (A[i][j]<-EPS || EPS<A[i][j])){
            pivot(k,i,j); break;
          }
      c=cc; c.resize(k,0); FOR(i,m) FOR(j,k) if (N[j]) c[j]-=c[kt[i]]*A[i][j];
    }
    res=doit(k-1); if (!res.empty()) res.resize(n);
    return res;
  }
};
typedef long double LD;

#include <pthread.h>
#include <semaphore.h>
#define PARALLEL 0
#define CORES 3
struct Instance {
   pthread_mutex_t finished;
   Instance() : finished(PTHREAD_MUTEX_INITIALIZER) { pthread_mutex_lock(&finished); }
   
   // define variables here
   int n, h[2006];
   
   void readInput() { // should read input; will run sequentially
      cin >> n;//DBG(n)
      FOR(i,n-1) {
         cin >> h[i];
         h[i]--;
      }
   }
   
   bool impossible;
   int scaled[2005];
   
   template<typename T> bool isgood (T *wyn) {
      FOR(i,n-1) {
         int j = h[i];
         REP(k,i+1,j-1) {
            LD lhs = (LD)(k-j)/(j-i) * wyn[i] + 
            (LD)(i-k)/(j-i) * wyn[j]
            + 1.0L * wyn[k];
            if (lhs >= 0) {return 0;}
         }
         REP(k,j+1,n-1) {
            LD lhs = (LD)(k-j)/(j-i) * wyn[i] + 
            (LD)(i-k)/(j-i) * wyn[j]
            + 1.0L * wyn[k];
            if (lhs > 1e-8) {return 0;}
         }
      }
      return 1;
   }
   
   void compute() { // should produce output and store it, not use IO; will run in parallel
      vector<vector<LD> > A;
      vector<LD> b,c(n,0),res;
      FOR(i,n-2) {
         int j = h[i];
         REP(k,i+1,j-1) {
            A.pb(vector<LD>(n,0));
            b.pb(-1);
            A[SZ(A)-1][i] = (LD)(k-j)/(j-i);
            A[SZ(A)-1][j] = (LD)(i-k)/(j-i);
            A[SZ(A)-1][k] = 1;
         }
         REP(k,j+1,n-1) {
            A.pb(vector<LD>(n,0));
            b.pb(0);
            A[SZ(A)-1][i] = (LD)(k-j)/(j-i);
            A[SZ(A)-1][j] = (LD)(i-k)/(j-i);
            A[SZ(A)-1][k] = 1;
         }
      }
      FOR(i,n) {
         A.pb(vector<LD>(n,0));
         b.pb(1000);
         A[SZ(A)-1][i] = 1;
         A.pb(vector<LD>(n,0));
         b.pb(0);
         A[SZ(A)-1][i] = -1;
      }
         
      res = Simplex::simplex(A,b,c);
      //cerr<<setprecision(10) << fixed ;DBG(res)
      if (res.empty()) impossible = 1;
      else {
         impossible = 0;
         
         LD largest = *max_element(ALL(res));
         int zwiekszen = 0;
         if (largest != 0) {
            while (largest*2 <= 1000000000.0L) {
               //DBG(largest)
               FOR(i,n) res[i] *= 2;
               largest *= 2;
               ++zwiekszen;
            }
         }
         //DBG(zwiekszen)
         //FOR(i,n) scaled[i] = (res[i]);
         
         int power3[15];
         power3[0] = 1;
         FORI(i,10) power3[i] = power3[i-1]  *3;
         
         FOR(mask,power3[n]) {
            FOR(i,n) {
               int ki = (mask / power3[i]) % 3;
               ki --;
               scaled[i] = round(res[i]);
               if (scaled[i] + ki != -1) scaled[i] += ki;
            }
            if (isgood(scaled)) {
               cerr << "success" << endl;
               break;
            }
            if (mask == power3[n] - 1) cerr << "zleee" << endl;
         }
      }
   }
   
   void writeOutput () { // should write stored output, without newline; will run sequentially
      if (impossible) {
         cout << "Impossible";
      } else {
         FOR(i,n) {
            cout << fixed << setprecision(9) << scaled[i];
            if (i != n-1) cout << " ";
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
