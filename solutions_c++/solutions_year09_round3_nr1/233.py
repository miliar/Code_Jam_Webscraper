#include <iostream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;


int main() {
  int tt;
  scanf("%d", &tt);
  char c;
  scanf("%c", &c);
  for(int iii=1; iii<=tt; iii++) {
    string l;
    getline(cin, l);
    if(l[l.size()-1]<'0') l=l.substr(0, l.size()-1);

    int base=0;
    vector<char> cc;
    for(int i=0; i<l.size(); i++) {
      int found=0;
      for(int j=0; j<cc.size(); j++) if(cc[j]==l[i]) { found=1; break; }
      if(found==0) {
        cc.push_back(l[i]);
        base++;
      }
    }
    if(base==1) base=2;

//cout<<base<<endl;
    //fix first 2:
    long long sol=0;
    if(l.size()==1) sol=1;
//    if(l.size()==2) sol=base;

    if(l.size()>1) {
      vector<int> s(l.size(), -1);

      //first is 1
      //second is 0

      for(int i=0; i<l.size(); i++) {
        if(l[i]==l[0]) s[i]=1;
        if(l[i]==l[1] && l[0]!=l[1]) s[i]=0;
      }

      int n=2;
      if(l[0]==l[1]) n=0;
      for(int i=2; i<l.size(); i++) {
        //replace l[i] with n
        if(s[i]==-1) {
          for(int j=0; j<l.size(); j++) {
            if(l[j]==l[i]) s[j]=n;
          }
          n++;
          if(n==1) n++;
        }
      }


      long long bb=1;
      for(int i=s.size()-1; i>=0; i--) {
        if(s[i]==-1) s[i]=0;
        sol+=bb*s[i];
        bb*=base;
      }
/*
      for(int i=0; i<s.size(); i++) {
cout<<s[i]<<endl;
      }
cout<<endl;
//*/

    }



    cout<<"Case #"<<iii<<": "<<sol<<endl;
//return 0;

  }

  return 0;
}
