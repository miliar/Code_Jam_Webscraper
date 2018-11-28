#include <iostream>
#include <vector>

using namespace std;

int answer(const vector<int>& miss,const vector<vector<int> >& prices,int p);
const int P=10;
const int T=1<<P,infinity=999999999;

int main(){
  assert(infinity>1024*100000);
  int t;
  cin>>t;
  for(int i=0;i<t;i++){
    int p;
    cin>>p;
    int teams=1<<p;
    vector<int> miss(teams);
    for(int j=0;j<teams;j++)
      cin>>miss[j];
    vector<vector<int> > prices(p);
    int row=teams;
    for(int j=0;j<p;j++){
      row/=2;
      prices[j].resize(row);
      for(int k=0;k<row;k++)
        cin>>prices[j][k];
    }
    reverse(prices.begin(),prices.end());
    cout<<"Case #"<<i+1<<": "<<answer(miss,prices,p)<<'\n';
  }
}

int key=0;

int memo(const vector<int>& miss,const vector<vector<int> >& prices,int p,int d,int t,int m);

int answer(const vector<int>& miss,const vector<vector<int> >& prices,int p){
  key++;
  return memo(miss,prices,p,0,0,0);
}

int cache[T][P][P];
int cached[T][P][P];

int memo(const vector<int>& miss,const vector<vector<int> >& prices,int p,int d,int t,int m){
  if(d==p){
    if(m>miss[t])
      return infinity;
    return 0;
  }
  if(cached[t][d][m]==key)
    return cache[t][d][m];
  cached[t][d][m]=key;
  int& ret=cache[t][d][m]=infinity;
  int nd=d+1,nt=2*t;
  int misses=memo(miss,prices,p,nd,nt,m+1)+memo(miss,prices,p,nd,nt+1,m+1);
  int make=memo(miss,prices,p,nd,nt,m)+memo(miss,prices,p,nd,nt+1,m)+prices[d][t];
  ret=min(misses,make);
  ret=min(ret,infinity);
  return ret;
}
