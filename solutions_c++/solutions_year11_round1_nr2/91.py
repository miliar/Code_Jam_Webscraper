#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <stack>
#include <queue>
#include <algorithm>
#include <complex>
#include <cstdio>
#include <cstdlib>
#include <cassert>
using namespace std;

typedef long long ll;
typedef complex<double> pt;

int main(int argc, char *argv[])
{
  int cases; cin>>cases;
  for (int cn=1; cn<=cases; cn++){
    int n, m; cin>>n>>m;

    vector<string> ss(n);
    for (int i=0; i<n; i++) cin>>ss[i];

    cout<<"Case #"<<cn<<":";

    for (int i=0; i<m; i++){
      string ord; cin>>ord;
      //cout<<ord<<endl;

      vector<vector<map<string, bool> > >
        tbl(11, vector<map<string, bool> >(32));

      for (int j=0; j<n; j++){
        string &w = ss[j];

        int pat=0;
        for (int o=0; o<(int)ord.length(); o++){
          int npat = pat;
          char c = ord[o];
          for (int a=0; a<(int)w.length(); a++)
            if (w[a]==c)
              npat |= (1<<a);

          if (pat != npat){
            //cout<<w<<": "<<c<<": "<<o<<": "<<pat<<" -> "<<npat<<endl;
            string v=w;
            for (int b=0; b<(int)v.length(); b++)
              if (!(pat & (1<<b)))
                v[b] = '_';
            tbl[w.length()][o][v] = true;
            pat = npat;
          }
        }
      }

      int ans = 0, ansp = 0;
      for (int j=0; j<n; j++){
        string &w = ss[j];
        int point = 0;
        string spat(w.length(), '_');
        for (int co = 0; co<(int)ord.length(); co++){
          if (!tbl[w.length()][co][spat]) continue;
          char c = ord[co];

          //cout<<w<<": "<<spat<<": "<<co<<": "<<c<<endl;
          bool any = false;
          for (int k=0; k<(int)w.length(); k++){
            if (w[k] == c){
              spat[k] = w[k];
              any = true;
            }
          }
          if (!any) point++;
        }

        //cout<<w<<": "<<point<<endl;

        if (point > ansp){
          ansp = point;
          ans = j;
        }
      }

      cout<<" "<<ss[ans];
    }
    cout<<endl;
  }
  
  return 0;
}
