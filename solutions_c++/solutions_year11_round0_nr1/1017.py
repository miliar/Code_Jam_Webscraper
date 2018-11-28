#include <iostream>
#include <fstream>
#include <sstream>
#include <functional>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>
#include <map>
#include <set>
#include <string>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <cctype>
#include <complex>
#include <cassert>
using namespace std;
#define REP(i,n) for(int i=0;i<(int)(n);i++)
#define EACH(i,c) for(__typeof((c).begin())i=(c).begin();i!=(c).end();++i)
#define FOR(i,k,n) for (int i=(k);i<(int)(n);i++)
#define FEQ(i,k,n) for(int i=(k);i<=(int)(n);i++)
typedef long long ll;
typedef complex<double> P;

int main()
{
  int tc;scanf("%d",&tc);
  for(int t = 1; t <= tc; t++){
    int n;scanf("%d",&n);
    pair<char,int> order[100];
    vector<int> orange,blue;
    REP(i,n){
      cin>>order[i].first>>order[i].second;
      if (order[i].first == 'O') orange.push_back(order[i].second);
      else blue.push_back(order[i].second);
    }
    int po = 1, pb = 1, ans = 0, io = 0, ib = 0;
    REP(i,n){
      if (order[i].first == 'O'){
        int tmp = abs(po - order[i].second);
        if (ib < blue.size()){
          if (abs(pb - blue[ib]) <= tmp + 1) pb = blue[ib];
          else pb += pb > blue[ib] ? -(tmp+1) : tmp+1;
        }
        po = order[i].second;
        io++;
        ans += tmp + 1;
      }
      else{
        int tmp = abs(pb - order[i].second);
        if (io < orange.size()){
          if (abs(po - orange[io]) <= tmp + 1) po = orange[io];
          else po += po > orange[io] ? -(tmp+1) : tmp+1;
        }
        pb = order[i].second;
        ib++;
        ans += tmp + 1;
      }
    }
    printf("Case #%d: %d\n",t,ans);
  }
  return 0;
}

