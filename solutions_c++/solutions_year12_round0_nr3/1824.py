#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

const int N=2000009;
vector<int> t[N];

void jum(const int n){
  int taille=0;
  int lb=10;
  int lh=1;

  while(n/(lh*10)>0){
    lh*=10;
    taille++;
  }
  
  for(int i=1;i<=taille;++i){
    int nn=(n%lb)*lh+n/lb;
    lh/=10;
    lb*=10;
    if(nn>n)
      t[n].push_back(nn);
  }
  
  sort(t[n].begin(), t[n].end());
  t[n].resize(unique(t[n].begin(), t[n].end())-t[n].begin());
}

int find(int n, int a, int b){
  int res=0;
  for(int i=0;i<t[n].size();++i)
    if(t[n][i]>=a && t[n][i]<=b)
      res++;
  return res;
}

int main(){

  for(int i=0;i<N;++i)
    jum(i);

  int T;
  cin >> T;
  for(int cas=1;cas<=T;++cas){
    int res=0;
    int a, b;
    cin >> a >> b;
    for(int i=a;i<=b;++i)
      res+=find(i,a,b);
    cout << "Case #" << cas << ": " << res << endl;
  }
}
