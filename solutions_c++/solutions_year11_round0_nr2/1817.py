#include <iostream>
#include <vector>
#include <cstdio>
#include <cstring>
using namespace std;
#define f first
#define s second
#define mp make_pair
#define pb push_back
#define ll long long
char add[28][28];
vector <pair<int,int> > er;
string solve(string s,int n)
{
  string st;
  int uk[28]={0};
  for(int i=0;i<n;i++)
  {
    st=st+s[i];
    uk[s[i]-'A']++;
    if (st.size()!=1)
    {
      char t=add[st[st.size()-2]-'A'][st[st.size()-1]-'A'];
      if (t!=0)
      {
        uk[st[st.size()-2]-'A']--;
        uk[st[st.size()-1]-'A']--;
        st.erase(st.size()-2,2);
        st=st+t;
        uk[t-'A']++;
      }
    }
    for(int j=0;j<(int)er.size();j++)
      if (uk[er[j].f] && uk[er[j].s])
      {
        st.erase(0,st.size());
        for(int k=0;k<26;k++)uk[k]=0;
        break;
      }
  }
  er.clear();
  for(int i=0;i<26;i++)
    for(int j=0;j<26;j++)add[i][j]=0;
  return st;
}
int main()
{
  int t,n,c,d;
  //freopen("B-large.in","r",stdin);
  //freopen("output.txt","w",stdout);
  cin>>t;
  string s;
  for(int i=0;i<t;i++)
  {
    cin>>c;
    for(int j=0;j<c;j++)
    {
      cin>>s;
      add[s[0]-'A'][s[1]-'A']=add[s[1]-'A'][s[0]-'A']=s[2];
    }
    cin>>d;
    for(int j=0;j<d;j++)cin>>s,er.pb(mp(s[0]-'A',s[1]-'A'));
    cin>>n>>s;
    string ans=solve(s,n);
    cout<<"Case #"<<i+1<<": [";
    for(int j=0;j<(int)ans.size()-1;j++)cout<<ans[j]<<", ";
    if (ans.size()!=0)cout<<ans[ans.size()-1];
    cout<<"]\n";
  }
  return 0;
}
/*
1
1 QRI 0 4 RRQR

1
1 QFT 1 QF 7 FAQFDFQ

1
1 ASG 1 AS 10 AQWERASDFS
*/
