#include<iostream>
#include<stdio.h>
#include<math.h>
#include<vector>
#include<string>
#include<algorithm>
using namespace std;
void main2(int f){
    int n,m,c;
    string st;
    cin>>n;
    cin>>m;
    vector<string> v1,v2,v3;
    st="/home/gcj";
    for(int i=0;i<n;i++){
       cin>>st;
       v1.push_back(st);
       }
    for(int j=0;j<m;j++){
       cin>>st;
       for(int i=0;i<st.length();i++){
          if(st[i]=='/' && i!=0){            
             v3.push_back(st.substr(0,i));
          }
       }
       v3.push_back(st);
    }
    sort(v3.begin(),v3.end());
    vector<string>::iterator iter = v3.begin();
    while (iter != v3.end()) {
    while ((iter+1 != v3.end()) &&  (*iter == *(iter+1))) {
    v3.erase(iter+1);
    }
    for(int g=0;g<v1.size();g++)
       if(*iter==v1[g]){
          v3.erase(iter);
          iter--;
          break;
       }
    ++iter;
    }
    
    cout<<"Case #"<<f<<": "<<v3.size()<<"\n";
}
int main(){
   int n;
   freopen("A-large.in","r",stdin);
   freopen("out.out","w",stdout);
   cin>>n;
   for(int i=0;i<n;i++)
      main2(i+1);
   return 0;
}
