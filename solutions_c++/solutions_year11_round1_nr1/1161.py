#include <cstring>
#include <string>
#include <iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
#include <set>
#include <map>
#include <queue>
#include <sstream>
#include <cmath>
#include <cstdlib>
#include <climits>

using namespace std;
typedef long long int64;

int tcase;
int64 n,pd,pg;

int64 gcd(int64 a,int64 b){
  if(a%b==0) return b;
  return gcd(b,a%b);
}

int main(){
  
  cin>>tcase;
  for(int tc=1;tc<=tcase;++tc){
     cin>>n>>pd>>pg;
     int64 a = pd; int64 b = 100;
     int64 c = pg; int64 d = 100;
     int64 gd1 = gcd(a,b);  int64 gd2 = gcd(c,d);
     a /= gd1; b /= gd1; c /= gd2; d/=gd2;
     int64 mx1 = b; int64 mx2 = d;
     bool gd = true;
     if(n<mx1) gd = false;
     if(pd!=0 && pg==0) gd = false;
     if(pd!=100 && pg==100) gd = false;
     cout<<"Case #"<<tc<<": ";
     if(gd) cout<<"Possible"<<endl;
     else cout<<"Broken"<<endl;
  }  

  return 0;
}
