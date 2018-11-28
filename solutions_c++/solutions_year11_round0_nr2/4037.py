#include <iostream>
#include <fstream>
#include <vector>
using namespace std;

void data() {
//  ifstream r2;
  int T,C,D,N;
  char c1[4];
  char d1[3];
  char n1[10];
//  ifstream r2("data");
  ifstream r2("B-small-attempt1 (1).in");
  r2>>T;

 for(int a=0;a<T;a++) {
  r2>>C;
  if (C<=1) { 
     if(C==1){
     for(int i=0;i<3;i++) {
        r2>>c1[i];
     }}
     r2>>D;
     if (D<=1){
        if(D==1){
        for(int i=0;i<2;i++) {
           r2>>d1[i];
        }}
        r2>>N;
        for(int i=0;i<N;i++) {
           r2>>n1[i];
        }
     }
  }
  int cnt=0;
  vector <char> cset;
  for(int i=0;i<N;i++,cnt++) {
     cset.push_back(n1[i]);
     if (cnt>=1) {
        if (((cset[cnt-1]==c1[0]) && (cset[cnt]==c1[1])) || 
            ((cset[cnt-1]==c1[1]) && (cset[cnt]==c1[0]))) {
            cset.pop_back();
            cset.pop_back();
            cset.push_back(c1[2]);
            cnt--;
        }
        vector<char>::iterator it;
        int m=cnt;
        for(int j=0;j<m;j++) {
           if(((cset[j]==d1[1]) && (cset[cnt]==d1[0])) ||
               (((cset[j]==d1[0])) && (cset[cnt]==d1[1]))){
              cset.clear();
              cnt=-1;
              break;
           }
        }
     }
  }
  vector<char>::iterator it, in;
  cout<<"Case #"<<a+1<<": [";
  for(it=in=cset.begin();it<cset.end();it++) {
     in++;
     if (!(in<cset.end()))
        cout<<*it;
     else
        cout<<*it<<", ";
  }
  cout<<"]";
  cout<<endl;
 }
  r2.close();
}

int main() {

  data();

return 0;
}
