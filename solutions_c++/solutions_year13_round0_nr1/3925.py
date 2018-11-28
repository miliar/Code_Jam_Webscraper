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

#define MAX 1000010

int n = 4;
string a[4];

bool check(string str){
   int tCnt = 0;
   char winner = 'T';   

   For(i, 0, str.size()-1){
      if(str[i] == 'T')  ++tCnt;
      else if(str[i] == '.')  return false;
      else{
         if(winner == 'T'){
            winner = str[i];
         }
         else{
            if(winner != str[i]) return false;
         }
      }
   }
   
   if(tCnt > 1)  return false;
   
   cout << winner << " won" << endl;
   return true;
}

void solve(){
   string str;
   
   //row;
   For(i, 0, n-1){
      str = "";
      For(j, 0, n-1) str = str + a[i][j];
      
      if(check(str)) return;
   }
   
   //column;
   For(j, 0, n-1){
      str = "";
      For(i, 0, n-1) str = str + a[i][j];
      
      if(check(str)) return;
   }
   
   //1st diagonal
   str = "";
   For(i, 0, n-1){      
      str = str + a[i][i];            
   }
   if(check(str)) return;
   
   //2nd diagonal
   str = "";
   For(i, 0, n-1){
      str = str + a[i][n-1-i];
   }
   if(check(str)) return;
   
   For(i, 0, n-1) For(j, 0, n-1) if(a[i][j] == '.'){
      cout << "Game has not completed" << endl;
      return;
   }
   
   cout << "Draw" << endl;
}
int main(){
   //freopen("input.txt", "rt", stdin);
	//freopen("A-small-attempt0.in", "rt", stdin); 
	freopen("A-large.in", "rt", stdin);     
   freopen ("output.txt","w",stdout);
	
	int sotest;   cin >> sotest;
	For(run, 1, sotest){   cout << "Case #" << run << ": ";
	
	  getline(cin, a[0]);
	  For(i, 0, n-1) getline(cin, a[i]);
	  
  	  solve();
   }
	
	return 0;
}


