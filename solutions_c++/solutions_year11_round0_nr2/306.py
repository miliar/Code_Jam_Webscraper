#include <iostream>
#include <string>
#include <vector>
using namespace std;
int main(){
  int T;cin >> T;
  for(int c=1;c<=T;++c){
    int C;cin >> C;
    vector<string> combine(C);
    for(int i=0;i<C;++i)cin>>combine[i];
    int D;cin >> D;
    vector<string> opposed(D);
    for(int i=0;i<D;++i)cin>>opposed[i];
    int N;cin >> N;
    string invoke;cin >> invoke;
    vector<char> res;
    for(int i=0;i<invoke.size();++i){
      res.push_back(invoke[i]);
      bool flag=true;
      while(flag){
        flag=false;
        for(int j=0;j<C;++j){
          if(res.size()>1&&combine[j][0]==res.back()&&combine[j][1]==res[res.size()-2]){
            res.pop_back();
            res.pop_back();
            res.push_back(combine[j][2]);
            flag=true;
          }
          if(res.size()>1&&combine[j][1]==res.back()&&combine[j][0]==res[res.size()-2]){
            res.pop_back();
            res.pop_back();
            res.push_back(combine[j][2]);
            flag=true;
          }
        }
        for(int j=0;j<D;++j){
          for(int k=0;k<res.size();++k)for(int l=0;l<res.size();++l)if(res[k]==opposed[j][0]&&res[l]==opposed[j][1]){
                res.clear();
                flag=true;
          }
        }
      }
    }
    cout << "Case #"<<c<<": [";
    for(int i=0;i<res.size();++i){
      cout << res[i];
      if(i<res.size()-1)cout<<", ";
    }
    cout <<"]"<< endl;
  }
}

