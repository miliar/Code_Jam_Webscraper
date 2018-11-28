#include<iostream>
#include<vector>
#include<map>
#include<string>
#include<sstream>
#include<cmath>
#include<algorithm>
#include<queue>
#include<deque>
#include<set>
using namespace std;
//cout.setf(ios::fixed, ios::floatfield); cout.precision(8);
//double PI =  3.14159265358979323846;
#define ll long long
#define VI vector<int>
#define PI pair<int,int>
#define MP make_pair
#define PB push_back
#define VVI vector<VI >

int main() {
    int cases;
    cin>>cases;
    for (int tt=0;tt<cases;tt++) {
       int k;cin>>k;
       string s; cin>>s;
       VI p = VI(k,0);
       for (int i=0;i<k;i++) p[i]=i;
       int ret=999999;
       do {
           int pocet=s.size()/k;
           string ns=s;
           for (int i=0;i<pocet;i++) {
               for (int j=0;j<k;j++) {
                   ns[i*k+j]=s[i*k+p[j]];
               }    
           }
           int val=0;
           for (int i=0;i<ns.size();i++) {
               if (i==0||ns[i]!=ns[i-1]) val++;
           }
           if (val<ret) ret=val;
           
       } while (next_permutation(p.begin(),p.end()));     
       cout<<"Case #"<<tt+1<<": "<<ret<<endl; 
    }
}
