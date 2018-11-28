#include<iostream>
using namespace std;

void solve(){
   int n,s,p;
   cin >> n >> s >> p;
   int a,b,c,res;
   res = 0;
   for(int i = 0 ; i < n ; i++){
      int tmp;
      cin >> tmp;
      a = tmp/3;
      tmp -= a;
      b = tmp/2;
      tmp -= b;
      c = tmp;

      if(c >= p)res++;
      if(c == p-1 && s){
	 if(a > 0 || b > 0)res++,s--;
      }
   }
   cout << res << endl;
}

int main(){
   int n;
   cin >> n;
   for(int i = 1 ; i <= n ; i++){
      cout << "Case #" << i << ": " ;
      solve();
   }
   return 0;
}
