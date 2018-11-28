#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <vector>
#include <algorithm>

using namespace std;

//FILE *fin = fopen ("a.in","r");
//FILE *fout = fopen ("a.out","w");

//#define fin stdin
//#define fout stdout

int cal (int n, vector<int> v) {
  int m = v.size ();
  vector<int> pri;
  for (int i = 0;i < n;++i) 
    pri.push_back (i);
 
  int ret = 0;
  for (int i = 0;i < m;++i) {
    int next = v[i]-1;
    pri[next] = -1;
    int j = next,k= next;
    while (j-1>=0 && pri[j-1] >-1) --j;
    while (k+1<n && pri[k+1] > -1) k++;
    ret+=k-j;
  }
  return ret;
}
int main () {
  int T;
  cin>>T;
  for (int run = 1;run<=T;++run) {
    int P,Q;
    cin>>P>>Q;
    vector<int> rel;
    for (int i = 0;i<Q;++i) {
      int x;
      cin>>x;
      rel.push_back (x);
    }
    sort (rel.begin (),rel.end());
    int res = cal (P,rel);
    while (next_permutation (rel.begin (), rel.end()))
      res = min (res, cal(P,rel));
    printf ("Case #%d: %d\n",run,res);
  }
  return 0;
}
