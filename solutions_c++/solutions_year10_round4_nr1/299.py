#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<sstream>
#include<cmath>
#include<string>
#include<cstring>
#include<cctype>
#include<algorithm>
#include<vector>
#include<bitset>
#include<queue>
#include<stack>
#include<utility>
#include<list>
#include<set>
#include<map>
 
using namespace std;

#define eps 1e-9
#define INF INT_MAX
#define all(v) (v).begin(),(v).end()
#define rall(v) (v).end(),(v).begin()
#define mp make_pair
#define pb push_back

#define SZ(v) ((int)(v).size())
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define REP(i,n) FOR(i,0,n)
#define FORE(i,a,b) for(int i=(a);i<=(b);++i)
#define REPE(i,n) FORE(i,0,n)
#define REPSZ(i,v) REP(i,SZ(v))
#define CLEAR(t) memset((t),0,sizeof(t))

#define MAX 60

typedef pair < int, int > pii;
typedef long long LL;

vector<int> v;

int k;

int a,b,c,d;
int v1[MAX][MAX];
int v2[MAX][MAX];

int widthd(int k){
   REP(ind,k){
      bool foi=true;
      REP(i,k-ind-1)REP(j,k-ind-1-i){
         int x=k-ind-1-i-j;
         if(v1[i][j]!=v1[i+x][j+x]){ 
			 foi=false;
			 break;
		 }
      }
      if(foi) 
		  return ind;
   }
}

void cambia(){
	REP(i,k-1)REP(j,k-1-i){
		int x=k-1-i-j;
		swap(v1[i][j],v1[i+x][j+x]);
	}
}
void copia(){
  REP(i,k)REP(j,k){
     v2[i][j]=v1[j][k-1-i];
  }
  REP(i,k)REP(j,k) 
	  v1[i][j]=v2[i][j];
}
void run1(int caso){
	
	v.clear();
	cin>>k;


  REP(i,2*k-1){
	 REP(j,min(i+1,2*k-1-i)){
		int x=min(i,k-1); int y=max(0,i-k+1);
		cin>>v1[x-j][y+j];
	 }
  }
 
  
  a=widthd(k);
  cambia();

  b=min(widthd(k),a);
 copia();

  c=widthd(k);
	cambia();
  d=min(widthd(k),c);
   
  int sol = (b+d+k)*(b+d+k)-k*k;
  cout << "Case #"<<caso<<": "<< sol<<endl;
}
int main()
{
	int T; scanf("%d",&T);
	FORE(i,1,T) run1(i);
	return 0;
}