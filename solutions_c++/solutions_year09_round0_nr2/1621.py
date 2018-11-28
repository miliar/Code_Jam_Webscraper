#include <iostream>
#include <vector>
#include <string>
#include <list>

// #include "cout.h"
using namespace std;

#define sz(a)  int((a).size())
#define pb  push_back
#define all(c)  (c).begin(),(c).end()
#define tr(c,i)  for(typeof((c).begin()) i=(c).begin(); i!=(c).end(); i++)
#define rep(var,n)  for(int var=0;var<(n);var++)

vector<vector<int> > m; // source map
vector<vector<int> > d; // N=0 W=1 E=2 S=3 // sink=-1
vector<pair<int,int> > sink;
vector<vector<vector< pair<int,int> > > > chain;
vector<vector<int> > sm;

void paint(int h, int w, int sid)
{
  tr(chain[h][w],it) {
    int h2=it->first, w2=it->second;
    sm[h2][w2] = sid;
    paint(h2,w2,sid);
  }
}

main()
{
  int T, H, W, sid;

  cin >> T;

  rep(t,T){
    printf("Case #%d:\n", 1+t);

    sid = 0;
    
    cin >> H >> W;

    m.resize(H+2);
    sm.resize(H+2);
    d.resize(H+2);
    chain.resize(H+2);
    sink.resize(0);
    rep(h,H+2){
      m[h].resize(W+2);
      sm[h].resize(W+2);
      d[h].resize(W+2);
      chain[h].resize(W+2);
      rep(w,W+2) {
        m[h][w] = 99999;
        sm[h][w] = 99999;
        d[h][w] = -1;
        chain[h][w].resize(0);
      }
    }

    for(int h=1;h<=H;h++){
      for(int w=1;w<=W;w++){
        cin >> m[h][w];
      }
    }

    for(int h=1;h<=H;h++){
      for(int w=1;w<=W;w++){
        int a=m[h][w], dir=-1;
        if (m[h-1][w]<a) { dir=0; a=m[h-1][w]; }
        if (m[h][w-1]<a) { dir=1; a=m[h][w-1]; }
        if (m[h][w+1]<a) { dir=2; a=m[h][w+1]; }
        if (m[h+1][w]<a) { dir=3; a=m[h+1][w]; }
        d[h][w] = dir;

        switch(dir){
          case -1: sink.push_back( make_pair(h,w) ); sm[h][w] = sid++; break;
          case 0: chain[h-1][w].push_back( make_pair(h,w) ); break;
          case 1: chain[h][w-1].push_back( make_pair(h,w) ); break;
          case 2: chain[h][w+1].push_back( make_pair(h,w) ); break;
          case 3: chain[h+1][w].push_back( make_pair(h,w) ); break;
        }

      }
    }

    rep(s,sid){
      int h=sink[s].first, w=sink[s].second;
      paint(h,w,s);
    }
    // cout << "map: " << m << endl;
    // cout << "dir: " << d << endl;
    // cout << "sink at: " << sink << endl;
    // cout << "painted: " << sm << endl;

    // allocate characters [a-z]
    vector<int> corr(sid,0); int ch='a';
    for(int h=1;h<=H;h++){
      for(int w=1;w<=W;w++){
        int id=sm[h][w];
        if (corr[id]) continue;
        corr[id]=ch++;
      }
    }
    // cout << "corr: " << corr << endl;

    // replace & output
    rep(h,H){
      string o; o.resize(W*2-1);
      rep(i,W*2-1) o[i]=' ';
      rep(w,W){
        o[w*2] = corr[sm[h+1][w+1]];
      }
      cout << o << endl;
    }
  }
}
