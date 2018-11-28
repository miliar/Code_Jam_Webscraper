#include<iostream>
#include<vector>
#include<string>
#include<set>
using namespace std;
set<string> se;
vector<string> qs;
int calc()
{
  set<string> used=se;
  int i,rv=0;
  for(i=0;i<qs.size();++i)
  { used.erase(qs[i]);
    if(used.empty()) { used=se; ++rv; used.erase(qs[i]); }
  }
  return rv;
}
int main()
{
  int ci,cn;
  cin>>cn;
  for(ci=1;ci<=cn;++ci)
  { int s,q,i;
    string temp;
    cin>>s;
    se.clear(); qs.clear();
    cin.ignore();
    for(i=0;i<s;++i)
    { getline(cin,temp);
      se.insert(temp);
    }
    cin>>q; cin.ignore();
    for(i=0;i<q;++i)
    { getline(cin,temp);
      qs.push_back(temp);
    }
    cout<<"Case #"<<ci<<": "<<calc()<<endl;
  }
}
