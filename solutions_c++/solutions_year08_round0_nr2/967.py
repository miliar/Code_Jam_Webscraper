#include <cstdio>
#include <vector>
#include <algorithm>

using namespace std;

struct item
{
  int time, value;
  
  item() {}
  item(int time, int value) : time(time), value(value) {}
  
  bool operator < (const item &z) const {
    if(time != z.time) return time < z.time;
    return value > z.value;
  }
};

void input(void);
void solve(void);

vector <item> A;
vector <item> B;

int case_cnt = 1;

int main(void)
{
  int t;
  scanf("%d", &t);
  while(t--) {
    input();
    solve();
  }
    
  return 0;
}

void input(void)
{
  A.clear();
  B.clear();
     
  int turn;
  scanf("%d", &turn);
  
  int nA, nB;
  scanf("%d %d", &nA, &nB);
  for(int i = 0; i < nA; i++) {
    int hh, mm;
    scanf("%d : %d", &hh, &mm);
    A.push_back(item(hh * 60 + mm, -1));
    scanf("%d : %d", &hh, &mm);
    B.push_back(item(hh * 60 + mm + turn, +1));
  }
  for(int i = 0; i < nB; i++) {
    int hh, mm;
    scanf("%d : %d", &hh, &mm);
    B.push_back(item(60 * hh + mm, -1));
    scanf("%d : %d", &hh, &mm);
    A.push_back(item(60 * hh + mm + turn, +1));
  }
}

void solve(void)
{ 
  sort(A.begin(), A.end());
  sort(B.begin(), B.end());
  
  int ansA = 0;
  int cntA = 0;
  for(int i = 0; i < A.size(); i++) {
    cntA -= A[i].value;
    if(ansA < cntA) ansA = cntA;
  }
  
  int ansB = 0;
  int cntB = 0;
  for(int i = 0; i < B.size(); i++) {
    cntB -= B[i].value;
    if(ansB < cntB) ansB = cntB;
  }
  
  printf("Case #%d: %d %d\n", case_cnt++, ansA, ansB);
}

