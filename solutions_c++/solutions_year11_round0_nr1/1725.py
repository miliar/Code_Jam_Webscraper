#include<iostream>
#include<vector>
using namespace std;

#define REP(i,i0,in) for(int i=(i0); i<(in); i++)
#define fst(p) ((p).first)
#define snd(p) ((p).second)

typedef pair<char,int> pci;
int compute(vector<pci> &V){
  // 0: O, 1: B
  int turn[] = {0, 0};
  int pos[] = {1, 1};
  REP(i,0,V.size()){
    int tg = fst(V[i])=='B';
    int nes = abs(snd(V[i])-pos[tg])+1;
    pos[tg] = snd(V[i]);
    if (turn[tg]+nes <= turn[!tg]) {
      turn[tg] = turn[!tg]+1;
    } else {
      turn[tg] = turn[tg]+nes;
    }
  }
  return max(turn[0],turn[1]);
}

int main(){
  int T;
  cin >> T;
  REP(t,0,T){
    int N;
    cin >> N;
    vector<pci> V(N);
    REP(i,0,N){
      cin >> fst(V[i]);
      cin >> snd(V[i]);
    }
    int ans = compute(V);
    cout << "Case #" << (t+1) << ": " << ans << endl;
  }
  return 0;
}
