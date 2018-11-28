#include <iostream>
#include <cstdio>
#include <cmath>
#define ffor(_a,_f,_t) for(int _a=(_f),__t=(_t);_a<__t;_a++)
#define all(_v) (_v).begin() , (_v).end()
#define sz size()
#define pb push_back
#define SET(__set, val) memset(__set, val, sizeof(__set))
#define FOR(__i, __n) ffor (__i, 0, __n)
#define sqr(_a) ((_a) * (_a))
#define syso system("pause")

using namespace std;

double dist(double x1, double y1, double x2, double y2){
  return sqrt(sqr(x1 - x2) + sqr(y1 - y2));
}

int main(){
  freopen("Al.out","wt", stdout);
  freopen("Al.in","r", stdin);
  int tests, b;
  scanf("%d\n", &tests);
  string str;
  FOR (test, tests){
    int n;
    scanf("%d", &n);
    long long val[n], st;
    FOR (i, n){
      cin >> str;
      val[i] = 0LL;
      st = 1LL;
      FOR (j, n){
        if (str[j] == '1')
          val[i] |= st;
          
        st <<= 1LL;
      }
      
    }
    
    int ret = 0;
    FOR (i, n){
      ffor (j, i, n)
        if (val[j] < (1LL << (i + 1LL))){
          ret += j - i;
          for (int k = j; k > i; k--)
            swap(val[k], val[k - 1]);
            
          break;
        }
    }
    
    printf("Case #%d: %d\n", test + 1, ret);
  }
  
//  syso;
  return 0;
}
