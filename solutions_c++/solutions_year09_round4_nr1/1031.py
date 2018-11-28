#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <cmath>
#include <algorithm>
#include <string>
#include <sstream>
#include <fstream>
#include <utility>
#include <queue>

using namespace std;

int main(){
    int nq; cin >> nq;
    for (int Q = 1; Q <= nq; Q++){
        int res = 0;
        int N; cin >> N;
        vector<vector<int> > V(N);
        vector<int> W(N);
        for (int i=0;i<N;i++){
            int pos = 0;
            for (int j=0;j<N;j++){
                char c; cin >> c;
                if (c == '1') pos = j;
            }
            //V[pos].push_back(i);
            W[i] = pos;
        }
        for (int pos = 0; pos < N; pos++){
              for (int i=pos;i<N;i++){
                  if (W[i] <= pos){
                     for (int j=i;j>pos;j--){
                         swap(W[j],W[j-1]);
                         res++;
                     }
                     break;
                  }
              }
              
        }
        cout << "Case #" << Q << ": " << res << endl;
    }
    return 0;
}

/*
        for (int i=0;i<N;i++) sort(V[i].begin(),V[i].end());
        priority_queue<int>  PQ;
        for (int i=0; i< N; i++){*/

        /*
        vector<int> used(N,0);
        for (int i = N-1; i >= 0; i--){
            for (int j=0;j<V[i].size();j++){
                   int pos;
                   for (int k = i; k < N; k++){
                       if (!used[k]){ pos = k; break; }
                   }
                   if (pos > V[i][j]){
                      used[pos] = 1;
                      res+=pos - V[i][j];
                      for (int k = 0; k < N; k++){
                          for (int l = 0; l < V[k].size(); l++)
                      }
                   }
                   else used[V[i][j]] = 1;
                   
            }
        }
        */
