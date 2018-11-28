#include <iostream>
#include <vector>
#include <queue>

using namespace std;

struct item{
  int s, q, w;
  item() {}
  item(int S, int Q, int W) : s(S), q(Q), w(W) {}
  bool operator < (const item &b) const {
    return w > b.w;
  }
};

int main(){
  int N;
  cin >> N;
  for (int n=1; n<=N; ++n){
    int S;
    cin >> S;
    string line;
    getline(cin, line);
    vector<string> engines(S);
    for (int i=0; i<S; ++i){
      getline(cin, line);
      engines[i] = line;
    }
    int Q;
    cin >> Q;
    getline(cin, line);
    vector<string> queries(Q);
    for (int i=0; i<Q; ++i){
      getline(cin, line);
      queries[i] = line;
    }

    int d[Q][S];
    for (int i=0; i<Q; ++i){
      for (int j=0; j<S; ++j){
        d[i][j] = INT_MAX;
      }
    }

    int answer;
    if (Q == 0){
      answer = 0;
    }else{
      priority_queue<item> pq;
      for (int j=0; j<S; ++j){
        if (engines[j] != queries[0]){
          d[0][j] = 0;
          pq.push(item(j, 0, 0));
        }
      }

      while (pq.size()){
        int s = pq.top().s;
        int q = pq.top().q;
        int w = pq.top().w;
        pq.pop();

        //printf("popped (s=%d, q=%d, w=%d)\n", s, q, w);

        if (q == Q-1){
          answer = w;
          break;
        }

        if (d[q][s] < w) continue;

        if (queries[q+1] != engines[s] && w < d[q+1][s]){
          d[q+1][s] = w;
          pq.push(item(s, q+1, w));
        }

        for (int k=0; k<S; ++k){
          if (queries[q+1] != engines[k] && w + 1 < d[q+1][k]){
            d[q+1][k] = w + 1;
            pq.push(item(k, q+1, w + 1));
          }
        }
      }
    }
    cout << "Case #" << n << ": " << answer << endl;
  }
  return 0;
}
