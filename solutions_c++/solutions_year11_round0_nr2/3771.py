#include<vector>
#include<iostream>
#include<string>
using namespace std;

int main() {
  int T;
  cin>>T;
for (int t = 1; t<=T; ++t) {
int c[100][100],d[100][100];
    for (char i =0;i<='Z';++i) 
    for(char j=0;j<='Z';++j) {
c[i][j] = d[i][j]=0; }
int cc,dd,nn; string x,xx;
    cin>>cc;
    while (cc-->0) {cin>>xx; c[xx[0]][xx[1]]=c[xx[1]][xx[0]]=xx[2];}
cin>>dd;    
while (dd-->0) {cin>>xx; d[xx[0]][xx[1]]=d[xx[1]][xx[0]]=1;}
    vector<int> o;
cin>>nn;
cin>>x;

for (int i = 0; i<nn;++i) {
int c2 = x[i];
      while (1) {

if (!o.size()) { break; }
        int c1 = o[o.size()-1];
        if (c[c1][c2]) {
          o.pop_back();
          c2 = c[c1][c2];
        } else { break; }
      
}
  o.push_back(c2);
  for (int j = 0; j < o.size() -1; ++j) if (d[o[j]][c2]) {o.clear(); break;}     
}
    cout<<"Case #"<<t<<": [";
    for (int j = 0; j < o.size(); ++j) cout<<(j ? ", " : "")<<(char)o[j];
    cout<<"]"<<endl;  
}
  return 0;
}
