#include <iostream>
#include <sstream>
#include <cstdio>
#include <string>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <vector>
#include <list>
#include <queue>
#include <stack>
#include <set>
#include <map>
#include <algorithm>
#include <cmath>
using namespace std;

#define INF (1<<29)
#define eps 1e-9

#define ll long long
#define ld long double
#define ull unsigned long long

#define mp make_pair
#define pb push_back

#define Clear(t) memset((t), 0, sizeof(t))
#define Clear2(t, v) memset((t), (v), sizeof(t))

#define For(i,a,b) for(int i = (int)(a), _t = (int)(b); i <= _t; i++)
#define Ford(i,a,b) for(int i = (int)(a), _t = (int)(b); i >= _t; i--)

#define SZ(t) ( (int)((t).size()) )
#define All(v) (v).begin(), (v).end()
#define Sort(v) sort(All(v))
#define present(c,x) ((c).find(x) != (c).end())

int N;
int d[10010];
int l[10010];
int D;

void input(){
   cin >> N;
   For(i, 0, N-1) cin >> d[i] >> l[i];
   cin >> D;
}

bool check(int i, int dist){
   //cout << "check ... " << i << ", " << dist << endl;
   if(i==0){
      if(d[0] >= dist)   return true;
      return false;
   }
   
   For(j, 0, i-1){
      int tmp = d[i] - d[j];
      if(tmp >= dist && tmp <= l[j]){
         if(check(j, tmp)) return true;
      }
   }
   
   return false;
}
bool solve(){
   For(i, 0, N-1){
      if(D-d[i] <= l[i]){
         if(check(i, D - d[i]))  return true;
      }
   }
}

int main(){
   //freopen("input.txt", "rt", stdin);
	freopen("A-small-attempt0.in", "rt", stdin); 
	//freopen("A-large.in", "rt", stdin);     
   freopen ("output.txt","w",stdout);

	int sotest;   cin >> sotest;
	For(run, 1, sotest){   cout << "Case #" << run << ": ";
      input();
      
      if(solve()) cout << "YES" << endl;
      else        cout << "NO" << endl;      
   }
	
	return 0;
}
