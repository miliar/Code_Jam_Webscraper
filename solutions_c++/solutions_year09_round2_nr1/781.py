#include <iostream>
#include <vector>
#include <sstream>
#include <string>
using namespace std;


int main() {
  int tt;
  scanf("%d", &tt);
  for(int iii=1; iii<=tt; iii++) {
    int l;
    scanf("%d", &l);

    //vector<string> t;
    string ttt;
    char c;
    scanf("%c", &c);
    for(int i=0; i<l; i++) {
      string ll;
      getline(cin, ll);
//      t.push_back(ll);
//      t+=ll;

      for(int j=0; j<ll.size(); j++) {
        if(ll[j]==')') ttt+=' ';
        ttt+=ll[j];
        if(ll[j]=='(') ttt+=' ';
      }
    }

//parse tree

    int a; // #animals
    scanf("%d", &a);


    cout<<"Case #"<<iii<<":"<<endl;
    for(int i=0; i<a; i++) {
      string name;
      cin>>name;
      int n;
      cin>>n;
      vector<string> f;
      f.clear();
      for(int j=0; j<n; j++) {
        cin>>name;
        f.push_back(name);
      }

      string t=ttt;


      double pr=1.0;
      int ok=0;
      int p=0;

      while(ok==0 && p<t.size()-1) {
        p=0;
//cout<<t<<endl;
        while(t[p]!='0' && t[p]!='1') p++;
        t=t.substr(p, t.size());

        stringstream tmp(t);
        double val;
        tmp>>val;
        string feat;
        tmp>>feat;

        pr*=val;


//cout<<val<<"|"<<t<<endl;


        if(feat[0]==')') {
          ok==1;
          break;
        }


        int yesno=0; //no
        for(int j=0; j<f.size(); j++) if(feat==f[j]) {
          yesno=1;
//cout<<"--:|"<<feat<<" "<<f[j]<<endl;
        }

        p=0;
        while(t[p]!='(') p++;
        p++;
        t=t.substr(p, t.size());
        p=0;
        if(yesno==0) {
          int num=1;

//cout<<":"<<t<<endl;
          while(num>0) {
            if(t[p]=='(') num++;
            if(t[p]==')') num--;
            p++;
          }
          t=t.substr(p, t.size());
          p=0;
//cout<<":"<<t<<endl;
        }




      }


//      cout<<pr<<endl;
      printf("%f\n", (float)pr);


    }






  }

  return 0;
}
