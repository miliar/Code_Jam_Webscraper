#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;

vector<string> dict;

vector<string> parse(const string& s)
{
  vector<string> rv;
  for(int i=0;i<s.size();++i)
  { rv.push_back("");
    if(s[i]!='(') rv.back()+=s[i];
    else
    { while(s[++i]!=')') rv.back()+=s[i];
      sort(rv.back().begin(),rv.back().end());
      rv.back().erase(unique(rv.back().begin(),rv.back().end()),
          rv.back().end());
    }
  }
  return rv;
}

int count(const vector<string>& s)
{ vector<bool> valid(dict.size(),true);
  int i,j,n=dict.size(),rv=dict.size();
  for(i=0;i<s.size();++i)
    for(j=0;j<n;++j) if(valid[j])
      if(!binary_search(s[i].begin(),s[i].end(),dict[j][i]))
        valid[j]=false, rv--;
  return rv;
}

int main()
{
  int i,l,d,n;
  while(cin>>l>>d>>n)
  { dict.clear();
    for(i=0;i<d;++i) 
    { string s;
      cin>>s;
      dict.push_back(s);
    }
    for(i=0;i<n;++i)
    { string s;
      cin>>s;
      cout<<"Case #"<<i+1<<": "<<count(parse(s))<<endl;
    }
  }
}
