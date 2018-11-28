#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<deque>
#include<set>
using namespace std;
#define ll long long
#define VI vector<int>
#define VS vector<string>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back

int main() {

int T;
cin>>T;
for (int t=0;t<T;t++) {
    int N; cin>>N;
    VI b;
    VI o;
    VS farba;
    VI all;
    int posb=0;
    int poso=0;
    for (int i=0;i<N;i++) {
        string r; int p;
        cin>>r>>p;
        all.PB(p);
        farba.PB(r);
        if (r=="O") o.PB(p); else b.PB(p);
    }    
    int steps =0;
    int rb=1;
    int ro=1;
    int pos=0;
    while (pos<all.size()) {
          //cout<<"@ "<<steps<<" "<<pos<<" "<<poso<<" "<<posb<<" ; "<<farba[pos]<<" "<<all[pos]<<endl;
          steps++;
          if (farba[pos]=="O") {
             if (ro==all[pos]) {
                pos++;
                poso++;                     
             } else if (ro<all[pos]) {
                ro++;
             } else {
                ro--;       
             }
             if (posb<b.size()) {
                if (rb<b[posb]) rb++;
                else if (rb>b[posb]) rb--;
             }
             
             
          } else {


             if (rb==all[pos]) {
                pos++;
                posb++;                     
             } else if (rb<all[pos]) {
                rb++;
             } else {
                rb--;       
             }
             if (poso<o.size()) {
                if (ro<o[poso]) ro++;
                else if (ro>o[poso]) ro--;
             }

                 
          }
          
          
    }
    
    cout<<"Case #"<<t+1<<": "<<steps<<endl;
    
    
} 
    
}
