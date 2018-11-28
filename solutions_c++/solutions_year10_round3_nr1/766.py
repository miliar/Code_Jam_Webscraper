#include <iostream>
#include <vector>
#include <string>
#include <regex.h>
#include <algorithm>
#include <queue>
#include <stack>
using namespace std;


int main() {
  int t;
  scanf("%d", &t);
  for(int iii=1; iii<=t; iii++) {
    int n;
    scanf("%d", &n);
    vector<int> a;
    vector<int> b;
    for(int i=0; i<n; i++) {
      int a_, b_; cin>>a_; cin>>b_; a.push_back(a_); b.push_back(b_);
    }

    int inter=0;
    for(int i=0; i<a.size(); i++) {
      for(int j=i+1; j<a.size(); j++) {
        if((a[i]>a[j] && b[i]<b[j]) || (a[i]<a[j] && b[i]>b[j] )) inter++;


      }
    }

    cout<<"Case #"<<iii<<": "<<inter<<endl;


  }

  return 0;
}




