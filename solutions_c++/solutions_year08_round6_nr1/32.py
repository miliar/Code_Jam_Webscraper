#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <map>
#include <set>

using namespace std;

#define HMAX 1000000

int main()
{
  int ncase;
  cin >> ncase;

  for (int cas = 1; cas <= ncase; cas++) {
    int N;
    cin >> N;

    vector<int> hv, wv;
    vector<bool> bv;
    set<long long> nbmap;
    for (int i = 0; i < N; i++) {
      int h, w;
      string b;
      cin >> h >> w;
      cin >> b;
      hv.push_back(h);
      wv.push_back(w);
      bv.push_back(b[0] == 'B');
      if (b[0] == 'N') {
        nbmap.insert((long long)h * (HMAX+1) + w);
        cin >> b;
      }
      //cout << h << " " <<bv[i] << endl;
    }

    int h_min = -1, h_max = -1;
    int w_min = -1, w_max = -1;
    for (int i = 0; i < N; i++) {
      int h = hv[i];
      int w = wv[i];
      
      if (bv[i]) {
        if (h_min == -1) {
          h_min = h_max = h;
          w_min = w_max = w;
        } else {
          h_min = min(h_min, h);
          h_max = max(h_max, h);
          w_min = min(w_min, w);
          w_max = max(w_max, w);
        }
      }
    }
    //cout << h_min << " " << h_max << " " << w_min << " " << w_max << endl;

    int neg_h_min = 0, neg_h_max = HMAX+1;
    int neg_w_min = 0, neg_w_max = HMAX+1;
    vector<int> neg_sp_h[4];
    vector<int> neg_sp_w[4];
    for (int i = 0; i < N; i++) {
      int h = hv[i];
      int w = wv[i];
      if (!bv[i]) {
        if (h_min <= h && h <= h_max) {
          if (w < w_min) {
            neg_w_min = max(neg_w_min, w);
          } else if (w > w_max) {
            neg_w_max = min(neg_w_max, w);
          }
        } else if (w_min <= w && w <= w_max) {
          if (h < h_min) {
            neg_h_min = max(neg_h_min, h);
          } else if (h > h_max) {
            neg_h_max = min(neg_h_max, h);
          }
        } else {
          int pos = 0;
          if (h < h_min && w < w_min) {
            pos = 0;
          } else if (h > h_max && w < w_min) {
            pos = 1;
          } else if (h < h_min && w > w_max) {
            pos = 2;
          } else if (h > h_max && w > w_max) {
            pos = 3;
          }
          neg_sp_h[pos].push_back(h);
          neg_sp_w[pos].push_back(w);
        }
      }
    }
    //cout << neg_h_min << " " << neg_h_max << " " << neg_w_min << " " << neg_w_max << endl;
    int M;
    cin >> M;
    cout << "Case #" << cas << ":" << endl;
    for (int i = 0; i < M; i++) {
      int h, w;
      cin  >>  h >> w;
      //cout << h << ", " << w << endl;
      if (h_min == -1) {
        if (nbmap.find((long long)h * (HMAX+1) + w) != nbmap.end()) {
          cout << "NOT BIRD" << endl;
        } else {
          cout << "UNKNOWN" << endl;
        }
      } else if (h_min <= h && h <= h_max && w_min <= w && w <= w_max) {
        cout << "BIRD" << endl;
      } else if (h <= neg_h_min || h >= neg_h_max || w <= neg_w_min || w >= neg_w_max) {
        cout << "NOT BIRD" << endl;
      } else {
        for (int j = 0; j < neg_sp_h[0].size(); j++) {
          int nh = neg_sp_h[0][j], nw = neg_sp_w[0][j];
          if (h <= nh && w <= nw) {
            cout << "NOT BIRD" << endl;
            goto found;
          }
        }
        
        for (int j = 0; j < neg_sp_h[1].size(); j++) {
          int nh = neg_sp_h[1][j], nw = neg_sp_w[1][j];
          if (h >= nh && w <= nw) {
            cout << "NOT BIRD" << endl;
            goto found;
          }
        }
        
        for (int j = 0; j < neg_sp_h[2].size(); j++) {
          int nh = neg_sp_h[2][j], nw = neg_sp_w[2][j];
          if (h <= nh && w >= nw) {
            cout << "NOT BIRD" << endl;
            goto found;
          }
        }
        
        for (int j = 0; j < neg_sp_h[3].size(); j++) {
          int nh = neg_sp_h[3][j], nw = neg_sp_w[3][j];
          if (h >= nh && w >= nw) {
            cout << "NOT BIRD" << endl;
            goto found;
          }
        }
        cout << "UNKNOWN" << endl;
      found:;
      }
    }
    
  }

  return 0;
}

