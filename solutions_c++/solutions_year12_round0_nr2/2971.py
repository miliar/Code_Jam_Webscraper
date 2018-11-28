#include <iostream>
#include <vector>
#include <fstream>
#include <string>
using namespace std;

int main() {
 ifstream r1("B-large.in");
 int T,N,S,p;
 vector<int> v1;
 vector<int>::iterator it;
 int vnum;

 r1>>T;
 for(int i=0;i<T;i++){
  int max=0,modu=0,val1;
  r1>>N;
  r1>>S;
  r1>>p;
  v1.clear();
  for(int j=0;j<N;j++){
   r1>>vnum;
   v1.push_back(vnum);
  }
  for(it=v1.begin();it<v1.end();it++) {
   modu = *it%3;
   val1 = *it/3;
   if((modu == 1) || (modu == 2))
     val1++;
   if (val1>=p){
    max++;
   }
   else if (((modu == 2) || (modu == 0)) && (S > 0)){
    if(*it > 0)
     val1++;
    S--;
    if(val1>=p)
     max++;
    else
     S++;
   }
  }
  cout<<"Case #"<<i+1;
  cout<<": "<<max<<endl;
 }

 return 0;
}
