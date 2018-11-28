#include <iostream>
#include <fstream>
using namespace std;

int r[1000001];

int main() {
  /*r[1] = 2;
  for (int i=2;i<1000001;i++) {
    if (i%1000==0)cerr<<i<<endl;
    for (int j=i+1;;j++) {
      int jj = j-i;
      if (jj==i){r[i]=j;break;}
      if (i<r[jj]){r[i]=j;break;}
    }
  }*/
  ifstream is("out");
  for (int i=1;i<1000001;i++)is>>r[i];
  int ca;
  cin>>ca;
  for (int c=0;c<ca;c++) {
    int a1,b1,a2,b2;
    cin>>a1>>a2>>b1>>b2;
    int count = 0;
    for (int i=a1;i<=a2;i++)
    for (int j=b1;j<=b2;j++) {
      if (i==j)continue;
      int max = (i>j?i:j);
      int min = (i<j?i:j);
      count+=(max>=r[min]);
    }
    cout<<"Case: #"<<c+1<<": "<<count<<endl;
  }
  return 0;
}
