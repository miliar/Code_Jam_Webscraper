#include <iostream>

using namespace std;

int main() {
  int num_case;
  cin>>num_case;
  for (int c=0;c<num_case;c++) {
    int n,k;
    cin>>n>>k;
    cout<<"Case #"<<c+1<<": ";
    int i;
    for(i=0;i<n;i++) {
      if(k%2==0)break;
      k /= 2;
    }
    if (i==n)cout<<"ON";
    else cout<<"OFF";
    cout<<endl;
  }
  return 0;
}
