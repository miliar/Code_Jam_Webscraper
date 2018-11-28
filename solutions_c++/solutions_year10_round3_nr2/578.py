#include <iostream>
#include <iomanip>
#include <string>
#include <vector>
#include <cstdio>
#include <map>
#include <algorithm>

#define For(i,n) for(int i=0;i<(n);i++)
#define For1(i,n) for(int i=1;i<=(n);i++)
#define ll long long
#define clear(d) memset(d,0,sizeof(d))
#define INF 2000000000

using namespace std;

int main(){
  int CN;
  cin >> CN;
  int L,P,C;
  For1(CI,CN){
    cin >> L >> P >> C;
    int lg = 0;
    int l=L;
    while(l<P){
      l*=C;
      lg++;
    }
    int res=0;
    while(lg!=1){
      if(lg%2==0){
        lg=lg/2;
      }
      else{
        lg=(lg+1)/2;
      }
      res++;
    }

    cout << "Case #" << CI << ": " << res << endl;
  }
}
