#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <fstream>
#include <algorithm>
#include <map>
#include <set>
#include <string>
#include <vector>

using namespace std;

typedef long long ll;
typedef pair<int,int> pii;

#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)

int cmp(const void *a,const void *b){return *(int*)b-*(int*)a;}
ll gcd(ll x, ll y) { return y ? gcd(y, x%y) : x; }

int main (int argc, char *argv[]){
  int ti,tn;
  ifstream fin("A-large.in");
  ofstream fout("output.out");
  fin>>tn;
  ll ans;
  int p,k,l,i;
  int ar[1000];
  F1(ti,tn)
  {
    fin>>p>>k>>l;
    F0(i,l)
      fin>>ar[i];
    ans=0;
    qsort(ar,l,sizeof(int),cmp);
    F0(i,l)
      ans+=ar[i]*(i/k+1);
    cout<<"Case #"<<ti<<": "<<ans;
    cout<<endl;
    fout<<"Case #"<<ti<<": "<<ans;
    fout<<endl;
  }
  return 0;
}
