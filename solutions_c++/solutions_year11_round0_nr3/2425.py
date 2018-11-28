#include<iostream>
#include<algorithm>

using namespace std;

int main(){
  int T;
  cin >> T;
  for(int t=1;t<=T;t++){
    int N,sum,xsum,m;
    sum=xsum=0;
    m=0x7FFFFF;
    cin >> N;
    for(int i=0;i<N;i++){
      int tmp;
      cin >> tmp;
      sum+=tmp;
      xsum^=tmp;
      m=min(m,tmp);
    }
    cout << "Case #" << t << ": ";
    if(xsum==0){
      cout << sum-m << endl;
    }else{
      cout << "NO" << endl;
    }
  }
}
