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

map<string,int> m;

int main() {
    int N, M, T;
    cin>>T;
    for (int t=0;t<T;t++) {
             m.clear();
            int ret=0;
            cin>>N>>M;
            for (int i=0;i<N;i++) {
                string s;
                cin>>s;
                m[s]=1;    
            }
            for (int i=0;i<M;i++) {
                string s;
                cin>>s;
                s+="/";
                if (s.size()<=1) continue;
                VS v;
                string ss="";
                
                for (int i=0;i<s.size();i++) {
                    if (s[i]=='/'&&i!=0) {
                      v.PB(ss);    
                      ss+=s[i];               
                    } else {
                      ss+=s[i];       
                    } 
                }

                for (int i=v.size()-1;i>=0;i--) {
                  //  cout<<v[i]<<" ::"<<endl;
                    if (m.find(v[i])==m.end()) {
                       ret++; m[v[i]]=1;                         
                    } 
                    //else {
                    //   break;       
                    //}   
                }
                    
            }
            cout<<"Case #"<<t+1<<": "<<ret<<endl;
        
        
    } 
 
    
}
