#include<iostream>
#include<functional>
#include<algorithm>
using namespace std;

int main()
{
  int T;
  cin >> T;
  for(int tc=1;tc<=T;++tc){
    int n,s,p;
    int res = 0;
    int po[101];
    
    // input
    cin >> n >> s >> p;
    for(int i = 0; i < n; ++i){
      cin >> po[i];
    }

    if( p == 0 ){
      res = n;
    }else{
      // p >= 1

      sort(po,po+n,greater<int>());
      
      for(int i = 0; i < n; ++i){
        if( po[i] >= p*3-2 ||
            po[i] >= p*3-1 ||
            po[i] >= p*3   ){
          // standard
          ++res;
        }else{
          // surprising
          if( ( p>=2 && po[i] >= p*3-4 && s > 0 ) ||
              ( p>=2 && po[i] >= p*3-3 && s > 0 ) ){
            // cout << p*3-3 << endl;
            --s;
            ++res;
          }
          
        }
      }
    }


    
    cout << "Case #" << tc << ": " << res << endl;
  }
  return 0;
}
