#include <iostream>
#include <vector>
#include <numeric>
#include <map>
#include <set>
#include <queue>

#define REP(i,e) for(int i=0;i<(int)(e);i++)

using namespace std;

main(){
  int CT;
  cin >> CT;
  REP(C,CT){
    cout << "Case #" << C+1 << ": ";
    long long a,b,c,result=0;
    cin >> a >> b >> c;
    vector<long long> v;
    REP(i,c){long long n; cin >> n; v.push_back(n);}
    sort(v.rbegin(),v.rend());

    REP(i,c){
      result+=v[i]*((i/b)+1);
    }
    cout << result << endl;
  }
}
