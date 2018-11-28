#include<iostream>
#include<vector>
#include<cmath>

using namespace std;

int combine[256][256];
int oppose[256][256];

void convert(string S) {
  string ans;
  for(int i =0;i< S.size();i++) {
    ans.push_back(S[i]);
    while (ans.size()>=2) {
      if(combine[ans[ans.size()-1]][ans[ans.size()-2]]!=-1) {
        int c = combine[ans[ans.size()-1]][ans[ans.size()-2]];
        ans.erase(ans.begin() + ans.size()-1);
        ans.erase(ans.begin() + ans.size()-1);
        ans.push_back(c);
      } else {
        break;
      }
    }
    for(int j=(int)ans.size()-2;j>=0;j--) {
      if(oppose[ans[ans.size() - 1]][ans[j]] == 1) {
        ans.clear();
        break;
      }
    }
  }
  cout<<"[";
  for(int i = 0;i<ans.size();i++) {
    if(i==0)
      cout<<ans[i];
    else
      cout<<", "<<ans[i];
  }
  cout<<"]"<<endl;
}
int main() {
  int cas = 0;
  int T;
  cin>>T;
  for(cas = 1; cas <=T ; cas++) {
    memset(combine,0xff,sizeof(combine));
    memset(oppose,0xff,sizeof(oppose));
    int C;cin>>C;
    string p;
    for(int i=0;i<C;i++){ 
      cin>>p;
      combine[p[0]][p[1]] = p[2];
      combine[p[1]][p[0]] = p[2];
    }
    int D;cin>>D;
    for(int i =0;i<D;i++) {
      cin>>p;
      oppose[p[0]][p[1]] = 1;
      oppose[p[1]][p[0]] = 1;
    }
    string S;
    int N;cin>>N;
    cin>>S;
    cout<<"Case #"<<cas<<": ";
    convert(S);
  }
}
