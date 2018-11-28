#include <cstdio>
#include <iostream>
#include <cmath>
#include <sstream>
#include <vector>
#include <map>
#include <set>
#include <complex>
#include <algorithm>
#include <functional>
#include <fstream>
#include <numeric>
#include <string>
#include <valarray>


using namespace std;

int main(){
  int ttime;
  cin>>ttime;
  for (int ccount=1;ccount<=ttime;ccount++){
    int n;
    cin>>n;
    vector<int> num;
    for (int i=1;i<=n;i++){
      int x;
      cin>>x;
      num.push_back(x);
    }
    int sx=0;
    for (int i=0;i<num.size();i++)
      sx^=num[i];
    if (sx != 0){
      cout<<"Case #"<<ccount<<": NO"<<endl;
      continue;
    }
    int sum=0;
    sort(num.begin(),num.end());
    for (int i=1;i<num.size();i++)
      sum+=num[i];
    cout<<"Case #"<<ccount<<": "<<sum<<endl;
  }
}

