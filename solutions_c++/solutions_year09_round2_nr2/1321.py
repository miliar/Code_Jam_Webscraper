#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;

int main() {
  int tt;
  scanf("%d", &tt);
  char c;
  scanf("%c", &c);
  for(int iii=1; iii<=tt; iii++) {
    string l;
    getline(cin, l);

/*
    int found=0;
    for(int i=0; i<l.size(); i++) {
      int mmin=10;
      int minp=-1;


      if(found==1) {
        for(int j=i+1; j<l.size(); j++) {
          if(l[j]<l[i] && l[j]-'0'<mmin) {
            mmin=l[j]-'0';
            minp=j;
          }
        }
        if(minp>-1) {
          char t=l[minp];
          l[minp]=l[i];
          l[i]=t;
        }
      }

      if(found==0) {
        for(int j=i+1; j<l.size(); j++) {
          if(l[j]>l[i] && l[j]-'0'<mmin) {
            mmin=l[j]-'0';
            minp=j;
          }
        }

        if(minp!=-1) {
          found=1;
          char t=l[minp];
          l[minp]=l[i];
          l[i]=t;
        }
      }


    }
*/


stringstream a(l);
double a1;
a>>a1;

string l1=l;

      char v[30];
      int n=l.size();

      for(int i=0; i<l.size(); i++) v[i]=l[i];
      next_permutation(v, v+n);

      l="";
      for(int i=0; i<n; i++) l+=v[i];


stringstream b(l);
double a2;
b>>a2;


if(a2<=a1) {
  sort(v, v+n);

if(v[0]=='0') {
  for(int i=0; i<n; i++) if(v[i]!=v[0]) {
    v[0]=v[i];
    v[i]='0';
    break;
  }
}

      l="";
      l+=v[0];
      l+='0';
      for(int i=1; i<n; i++) l+=v[i];

}
//if(a2<=a1) l=l1+'0';
      cout<<"Case #"<<iii<<": "<<l<<endl;


  }

  return 0;
}
