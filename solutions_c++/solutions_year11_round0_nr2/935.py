#include<iostream>
#include<stack>
#include<vector>
using namespace std;

typedef stack<int> si;
typedef vector<int> vi;
typedef vector<vi> vvi;

const int nlet='Z'-'A'+1;

void pr(si& list) {
  if (list.size()>1) {
    char c='A'+list.top();
    list.pop();
    pr(list);
    cout<<", "<<c;
  } else if (list.size()==1) cout<<char('A'+list.top());
}

int main() {
  int t;
  cin>>t;
  for (int ncase=1;ncase<=t;++ncase) {
    int nc,no,n;
    cin>>nc;
    vvi gives(nlet,vi(nlet,-1));
    for (int i=0;i<nc;++i) {
      char ca,cb,cc;
      cin>>ca>>cb>>cc;
      gives[ca-'A'][cb-'A']=cc-'A';
      gives[cb-'A'][ca-'A']=cc-'A';
    }
    cin>>no;
    vvi dis(nlet);
    for (int i=0;i<no;++i) {
      char ca,cb;
      cin>>ca>>cb;
      dis[ca-'A'].push_back(cb-'A');
      dis[cb-'A'].push_back(ca-'A');
    }
    vi seen(nlet,0);
    si list;
    string s;
    cin>>n>>s;
    for (int i=0;i<n;++i) {
      int c=s[i]-'A';
      if (list.size()) {
        int d=list.top();
        if (gives[c][d]!=-1) {
          --seen[d];
          list.pop();
          ++seen[gives[c][d]];
          list.push(gives[c][d]);
        } else {
          bool found=false;
          for (int j=0;j<dis[c].size() and not found;++j) found=seen[dis[c][j]]>0;
          if (found) {
            seen=vi(nlet,0);
            while (list.size()) list.pop();
          } else {
            ++seen[c];
            list.push(c);
          }
        }
      } else {
        ++seen[c];
        list.push(c);
      }
    }
    cout<<"Case #"<<ncase<<": [";
    pr(list);
    cout<<']'<<endl;
  }
}
