#include <iostream>
#include <cstdio>
#include <algorithm>

#define MAX 2000

using namespace std;

int ta;
int na,nb;

int la[MAX],aa[MAX],lb[MAX],ab[MAX];

pair<int,int> solve() {
  pair<int,int> needed;
  needed.first=needed.second=0;
  int traina=0,trainb=0;
  for (int i=0;i<24*60;i++) {
    /*if (aa[i]) cout << i << " chegou A " << aa[i] << endl;
    if (ab[i]) cout << i << " chegou B " << ab[i] << endl;
    if (la[i]) cout << i << " saiu A " << la[i] << endl;
    if (lb[i]) cout << i << " saiu B " << lb[i] << endl;*/
    traina+=aa[i];
    trainb+=ab[i];
    if (la[i]>traina) {
      needed.first+=la[i]-traina;
      traina=0;
    }
    else
      traina-=la[i];

    if (lb[i]>trainb) {
      needed.second+=lb[i]-trainb;
      trainb=0;
    }
    else
      trainb-=lb[i];
  }
  return needed;
}

int main() {
  int nc;
  int dh,dm,ah,am;
  cin >> nc;
  for (int t=1;t<=nc;t++) {
    memset(la,0,sizeof(la));
    memset(aa,0,sizeof(aa));
    memset(lb,0,sizeof(lb));
    memset(ab,0,sizeof(ab));
    cin >> ta; 
    cin >> na >> nb;
    for (int i=0;i<na;i++) {
      scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
      la[dh*60+dm]++;
      ab[ah*60+am+ta]++;
    }    
    for (int i=0;i<nb;i++) {
      scanf("%d:%d %d:%d",&dh,&dm,&ah,&am);
      lb[dh*60+dm]++;
      aa[ah*60+am+ta]++;
    }
    pair<int,int> res=solve();
    cout << "Case #" << t << ": " << res.first << " " << res.second << endl;
  }
}
