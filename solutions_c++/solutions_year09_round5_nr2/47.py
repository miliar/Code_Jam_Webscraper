#include <iostream>
#include <iomanip>
#include <sstream>
#include <vector>
#include <stack>
#include <queue>
#include <map>
#include <set>
#include <algorithm>
#include <complex>
#include <cmath>
#include <cstdlib>
using namespace std;

typedef long long ll;
typedef complex<double> pt;

vector<string> ps;
vector<string> ss;

int eval(vector<int> &sel, int k)
{
  int tbl[128]={};
  for (int i=0;i<k;i++)
    for (int j=0;j<ss[sel[i]].length();j++)
      tbl[ss[sel[i]][j]]++;

  int ret=0;
  for (int i=0;i<ps.size();i++){
    int term=1;
    for (int j=0; j<ps[i].length(); j++)
      term=(term*tbl[ps[i][j]])%10009;
    ret=(ret+term)%10009;
  }
  return ret;
}

int comb(int i, int k, int n, vector<int> &hist, vector<bool> &use)
{
  if (i==k) return eval(hist, k);

  int ret=0;
  for (int a=0;a<n;a++){
    //if (use[a]) continue;
    use[a]=true;
    hist[i]=a;
    ret=(ret+comb(i+1, k, n, hist, use))%10009;
    use[a]=false;
  }
  return ret;
}

int main()
{
  int cases; cin>>cases;
  for (int c=1; c<=cases; c++){
    string p; cin>>p;
    for (int i=0;i<p.length();i++)
      if (p[i]=='+') p[i]=' ';
    ps.clear();
    istringstream iss(p);
    for (string term; iss>>term; ) ps.push_back(term);
    
    int k; cin>>k;

    int n; cin>>n;
    ss.resize(n);
    for (int i=0;i<n;i++) cin>>ss[i];

    cout<<"Case #"<<c<<":";

    for (int i=1; i<=k; i++){
      vector<int> hist(k);
      vector<bool> use(n, false);
      int ans=comb(0, i, n, hist, use);
      cout<<" "<<ans;
    }
    cout<<endl;
  }
  return 0;
}
