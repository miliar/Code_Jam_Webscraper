#include <iostream>
#include <vector>
#include <cstdio>
#include <cstdlib>
using namespace std;

typedef pair<int,int> P;

int main(void){
  int T;
  cin>>T;

  for(int SET=1;SET<=T;SET++){
    int n;
    cin>>n;

    vector<P> O,B;
    int ox = 1,bx = 1;

    for(int i=0;i<n;i++){
      char ch;
      int x;
      cin>>ch>>x;

      if(ch == 'O'){
        O.push_back(P(i,abs(x-ox)+1));
        ox = x;
      }
      else{
        B.push_back(P(i,abs(x-bx)+1));
        bx = x;
      }
    }

    int id = 0;
    int ans = 0;

    while(!O.empty() || !B.empty()){
      bool flg = false;

      if(!O.empty()){
        O[0].second--;
        if(O[0].first == id && O[0].second <= 0){
          flg = true;
          id++;
          O.erase(O.begin());
        }
      }

      if(!B.empty()){
        B[0].second--;
        if(B[0].first == id && B[0].second <= 0 && !flg){
          id++;
          B.erase(B.begin());
        }
      }

      ans++;

      //printf("%3d : (%d,%d) (%d,%d)\n",ans,!O.empty() ? O[0].first : -1,!O.empty() ? O[0].second : -1,!B.empty() ? B[0].first : -1,!B.empty() ? B[0].second : -1);
    }

    printf("Case #%d: %d\n",SET,ans);
  }

  return 0;
}
