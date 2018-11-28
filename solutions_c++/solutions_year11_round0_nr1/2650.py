#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>

using namespace std;

struct button {
  int pos;
  char col;
};

int main() {
  int T;
  cin>>T;
  int cas = 1;
  while(T--) {
    int N;
    cin>>N;
    vector <button> list(N);
    vector <int> listo;
    vector <int> listb;
    for (int i =0 ;i<N ;i++) {
      cin>>list[i].col>>list[i].pos;
      if (list[i].col == 'O')
        listo.push_back(list[i].pos);
      else
        listb.push_back(list[i].pos);
    }
    int co = 1; int cb = 1;
    int po = 0; int pb = 0;
    int time = 0;
    for (int i =0;i<N;i++) {
      if(list[i].col == 'O') {
        int d = abs(list[i].pos - co) + 1;
        time += d;
        co = list[i].pos;
        po++;
        if (pb < listb.size()) {
          if (d >= abs(listb[pb] - cb)) {
            cb = listb[pb];
          } else {
            cb = listb[pb] + abs(listb[pb] - cb) - d ;
          }
        }
      } else {
        int d = abs(list[i].pos - cb) + 1;
        time += d;
        cb = list[i].pos;
        pb++;
        if (po < listo.size()) {
          if (d >= abs(listo[po] - co)) {
            co = listo[po];
          } else {
            co = listo[po] + abs(listo[po] - co) - d ;
          }
        }
      }
    }
    cout<<"Case #"<<cas<<": "<<time<<endl;
    cas++;
  }
}
