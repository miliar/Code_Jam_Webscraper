#include<iostream>
#define MIN(a,b) ((a)>(b)?(b):(a))
using namespace std;

int main(){
  int cas;
  cin>>cas;

  for(int ca=1;ca<=cas;++ca){
    cout<<"Case #"<<ca<<": ";
    int n,s,p,cur;
    cin>>n>>s>>p;

    int yes=0;
    int maybe=0;
    for (int i=0; i<n; ++i) {
      cin>>cur;

      if (cur==p+p+p-4 || (p!=1 && cur == p+p+p-3)) {
        maybe++;
      } else if (cur>p+p+p-3 && cur <= 30) {
        yes++;
      }
    }

    cout<<(yes+MIN(maybe, s))<<endl;
  }
}
