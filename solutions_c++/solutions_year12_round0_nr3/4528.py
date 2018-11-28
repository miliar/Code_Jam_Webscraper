#include<iostream>
#include<cstdlib>
#include<iostream>
#include<cmath>
#include<cstring>
#include<vector>
using namespace std;
int znm[10];
vector<pair<int,int> > v;
int dodaj(int a,int b){
  pair<int,int> p=make_pair(a,b);
  for (int i=0; i<v.size(); ++i){
    if (p==v[i]) {/*cout<<p.first<<" "<<p.second<<endl;*/ return 0;}
  }
  v.push_back(p);
  return 1;
}

int main(){
  int t,a,b,rj;
  cin>>t;
  for (int tt=0; tt<t; ++tt){
    v.clear();
    cin>>a>>b;rj=0;
    for (int i=a; i<=b; ++i){
      //memset(znm,0,sizeof(znm));
      int c=i,j=0;
      for (j=0; c; ++j){
        znm[j]=c%10;
        c/=10;
      }
      for (int k=0; k<j/2; ++k){
        int p=znm[k]; znm[k]=znm[j-k-1]; znm[j-k-1]=p;}
      for (int k=0; k<j; ++k){
        int mem=znm[0];
        for (int l=0; l<j; ++l){
          znm[l]=znm[l+1];
        }
        znm[j-1]=mem;

        int tr=0;
        for (int l=0; l<j; ++l){
          tr*=10; tr+=znm[l];
        }
        if (!znm[0]) continue;
        if (i<tr&&a<=tr&&tr<=b) {if (dodaj(i,tr))  ++rj;}
      }
    }
    cout<<"Case #"<<tt+1<<": "<<rj<<endl;
  }
  return 0;
}
