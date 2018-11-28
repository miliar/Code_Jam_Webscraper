#include<iostream>
#include<map>
#include<vector>
#define pb push_back
#define mp make_pair
using namespace std;

void print(vector<char> v)
{
   cout<<"[";
    for(int i=0;i<v.size();i++)
    {
      cout<<v[i];
      if(i<v.size()-1)
       cout<<", ";
    }
   cout<<"]"<<endl;
}

int main()
{
  int n; 
  cin>>n;
  for(int tc=0;tc<n;tc++)
  {
    vector<char> v;
    map<pair<char,char>,char> rep;
    map<pair<char,char>,bool> rem;
    int nt;
    cin>>nt;
    char a,b,c;
    for(int i=0;i<nt;i++)
    {
      cin>>a>>b>>c;
       rep[mp(a,b)]=c;
       rep[mp(b,a)]=c;
    }
    cin>>nt;
    for(int i=0;i<nt;i++)
    {
      cin>>a>>b;
       rem[mp(a,b)]=true;
       rem[mp(b,a)]=true;
    }
    cin>>nt;
    for(int i=0;i<nt;i++)
    {
      cin>>c;
      int k=v.size();
      if(k && rep.find(mp(v[k-1],c))!=rep.end())
       {
            a=rep[mp(v[k-1],c)];
            v.pop_back();
            v.pb(a);
            continue;
       }
      bool cls=false;
      for(int j=k-1;j>=0;j--)
       {
         if(rem.find(mp(v[j],c))!=rem.end())
         {
            v.clear(); cls=true; break;
         }
       }
      if(cls) continue;
      v.pb(c);
    }
    cout<<"Case #"<<tc+1<<": ";
    print(v);
  }
}