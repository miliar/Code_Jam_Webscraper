//
//  main.cpp
//  GCJ
//
//  Created by Bryan Hooi on 14/4/12.
//  Copyright (c) 2012 Clinkle. All rights reserved.
//

#include <iostream>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <fstream>
#include <cassert>

using namespace std;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vi> vvi;
typedef pair<int, int> pii;
typedef vector<pii> vpii;

#define printv(v) for (int q=0;q<v.size();q++) fout << v[q] << " "; fout << endl;
#define printvv(v) for (int w=0;w<v.size();w++){ printv(v[w]); } fout << endl;

#define EPS 0.001
#define PIECES 1501

double dst(double ax, double ay, double bx, double by){
  return sqrt((bx-ax)*(bx-ax)+(by-ay)*(by-ay));
}

int main (int argc, const char * argv[])
{
  ifstream fin("/Users/HOOI/Documents/CS/GCJ/GCJ/in.txt");
  ofstream fout("/Users/HOOI/Documents/CS/GCJ/GCJ/out.txt");
  int cases; fin>>cases;
  for (int cs=1;cs<=cases;cs++){
    double n,wid,len; 
    fin>>n>>wid>>len;
    vd rad(n); for (int i=0;i<n;i++) fin>>rad[i];
    vi ind(n); vpii pr(n);
    for (int i=0;i<n;i++) {
      pr[i] = pii(rad[i], i);
    }
    sort(pr.rbegin(), pr.rend());
    vd r(n);
    for (int i=0;i<n;i++) {
      r[i] = pr[i].first; ind[i]=pr[i].second;
    }
    double wep = 1.0 * wid/(PIECES-1);
    double lep = 1.0 * len/(PIECES-1);
    
    vd xpos(n,0); vd ypos(n,0);
    
    int cur=0;
    for (int i=0;i<PIECES;i++){
      for (int j=0;j<PIECES;j++){
        double px = 1.0 * i * wep; 
        double py = 1.0 * j * lep;

        bool found=false;
        for (int k=0;k<cur;k++) 
          if (dst(px,py,xpos[k],ypos[k])<r[cur]+r[k]+EPS)
          { found = true; break; }
        if (found) continue;

        xpos[cur]=px; 
        ypos[cur]=py;
        cur++;
        if (cur==n){
          vd xfin(n); vd yfin(n);
          for (int l=0;l<n;l++){
            xfin[ind[l]]=xpos[l];
            yfin[ind[l]]=ypos[l];
          }
          fout<<"Case #"<<cs<<": ";
          for (int l=0;l<n;l++){
            fout<<fixed<<showpoint<<setprecision(9)<<xfin[l]<<" "<<yfin[l]<<" ";
          }
          fout<<endl;
          
          cout<<"Case #"<<cs<<": ";
          for (int l=0;l<n;l++){
            cout<<fixed<<showpoint<<setprecision(9)<<xfin[l]<<" "<<yfin[l]<<" ";
          }
          cout<<endl;
          
          goto out;
        }
      }
    }
  out:;
  }
  return 0;
}

