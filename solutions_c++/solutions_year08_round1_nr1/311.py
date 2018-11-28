#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main(){
  vector<long long> a,b;
  int N;
  int n=0;
  cin>>N;
  while(n++<N){
    int t;
    cin>>t;
    a.resize(t);
    b.resize(t);
    for (int i=0;i<t;i++){
      cin>>a[i];
    }
    for (int i=0;i<t;i++){
      cin>>b[i];
    }
    sort(a.begin(),a.end());
    sort(b.begin(),b.end());
    reverse(b.begin(),b.end());
    long long total=0;
    for (int i=0;i<t;i++){
      total+=a[i]*b[i];
    }
    printf("Case #%d: %lld\n",n,total);
  }
}
