#include <set>
#include <vector>
#include <cstdio>
#include <iostream>
#include <algorithm>
#include <stack>
using namespace std;
#define all(v) v.begin(),v.end()



int main(){
   int l,d,n;
   cin>>l>>d>>n;
   
   vector<string> cads(d);
   for(int i=0;i<d;i++) cin>>cads[i];
   
   
   
   for(int t=1;t<=n;t++){
    string s;
    cin>>s;
    bool dentro=false;
    int index=0;
    vector<set<char> > lista(l);
   
    for(int j=0;j<s.size();j++){
      if(s[j]==')'){dentro=false;index++;}
      else if(s[j]=='(') dentro=true;
      else if(dentro) lista[index].insert(s[j]);
      else lista[index++].insert(s[j]);
      
    }
    //for(int i=0;i<l;i++) cout<<lista[i].size()<<endl;
    int conta=0;
     for(int i=0;i<d;i++){
     bool puede=true;
     for(int j=0;j<l;j++) if(lista[j].count(cads[i][j])==0){puede=false;break;}
     if(puede) conta++;
     }
     printf("Case #%d: %d\n",t,conta);
     
   }
   
   
}