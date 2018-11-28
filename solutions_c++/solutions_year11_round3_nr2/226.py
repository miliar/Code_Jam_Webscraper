#include <cstdio>
#include <algorithm>
#include <vector>
using namespace std;

typedef long long LL;

const int MAX = 1000010;
const double INF = 1e15;
int len[MAX];
int L,N,C;
LL t;

vector<LL> zysk;

void simulate() {
  LL leftX, leftY;
  leftX = leftY = INF;
  int x = 0;
  for(int i=0; i<N; i++){
    if (i == x) leftX = t;
    
    LL czas = 2 * len[i];    
    if (leftX <= 2 * len[i]){
      zysk.clear();
      zysk.push_back((2 * len[i] - leftX) / 2);
      for(int j=i+1; j<N; j++)
        zysk.push_back(len[j]);
      return ;
    }
    
    leftX -= czas;
  }
  return ;
}

LL singleCase(){
  scanf("%d %lld %d %d",&L,&t,&N,&C);
  for(int i=0; i<C; i++) {
    scanf("%d",&len[i]);
  }
  
  LL sum = 0;
  for(int i=0; i<N; i++){
    len[i] = len[i % C];
    sum += len[i] * 2;
  }
  
  simulate();
  sort(zysk.rbegin(), zysk.rend());
  for(int i=0; i<zysk.size(); i++){
    if (i < L) sum -= (LL)zysk[i];
  }
  return sum;
}

int main() {
  int test;
  scanf("%d",&test);
  for(int i=1; i<=test; i++){
    printf("Case #%d: %lld\n",i,singleCase());
  }
  return 0;
}

