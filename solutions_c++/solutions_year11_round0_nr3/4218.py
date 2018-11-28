////anmolkapooor
//// HI !!!!! TRYING TO CODE... IF POSSIBLE.. PLEASE IGNORE THE ERRORS..!!1
//// QUESTION:

#include <cmath>
#include <cstdio>
#include <cctype>
#include <iostream>
#include <string>
#include <sstream>
#include <algorithm>
#include <vector>
using namespace std;
#define GI ({int _t; scanf("%d", &_t); _t;})
#define FOR(i, a, b) for (int i=a; i<b; i++)
#define REP(i, a) FOR(i, 0, a)
#define sz size()
#define pb push_back
#define cs c_str()
#define DBGV(_v) { REP(_i, _v.sz) { cout << _v[_i] << "\t";} cout << endl;}
#define tr(container, it) \
for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
typedef long long lld;

int main()
{
int test;
  cin>>test;
  int i=1;
   while(test--){
   int N;       
       cin>>N;
      lld xorsum=0;lld sum=0;
       lld num=9999999;
       FOR(ii,0,N){
           lld temp;
           cin>>temp;
           sum+=temp;
           xorsum^=temp;
           if(temp<num)
               num=temp;
           
       }
       
//cout<<num<<" "<<sum<<" "<<xsum<<" "<<endl;
cout<<"Case #"<<i++<<": ";
if(xorsum!=0) cout<<"NO"<<endl;
else cout<<sum-num<<endl;
}

    return 0;
}
