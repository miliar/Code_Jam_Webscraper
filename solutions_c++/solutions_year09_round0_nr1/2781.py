// {{{
#include <cmath>
#include <string>
#include <vector>
#include <cstring>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <cctype>
using namespace std;
// }}}
// {{{
typedef vector<string> vs;
typedef pair<int, int> pii;
#define forit(i,c) for (typeof((c).end()) i=(c).begin(); i!=(c).end(); ++i)
#define forn(i,c)  for (int i=0; i<c; ++i)
int main()
{
    
    freopen("in.txt","r",stdin);
    freopen("o.txt","w",stdout);
    int L,D,N;
    cin>>L>>D>>N;
    getchar();
    vs v;
    while(D--)
    {
      string t;
      getline(cin,t);
      v.push_back(t);
    }
    int n=0;
    while(N--)
    {
      n++;
      string s;
      getline(cin,s);
      vs vr;
      for(int i=0;i<s.length();)
      {
        string t="";
        while(i<s.length() && s[i]!='(')
        {
         t=s[i++];
         vr.push_back(t);
        }
        //if(t.length()!=0)  vr.push_back(t); 
        if(i==s.length()) break;
        t="";
        i++;
        while(i<s.length() && s[i]!=')')
        {
          t+=s[i++];
        }
        i++;
        vr.push_back(t);
      }
      int count=0;
      //forn(i,vr.size()) cout<<vr[i]<<"\n";
      forn(i,v.size())
      {
        string t=v[i];
        int flag=1;
        forn(j,t.length())
        {
            string m=vr[j];
            //cout<<vr[j]<<"--vr[]\n";
            int k=(int)m.find(t[j]);
            //cout<<k<<" for "<<t<<" at "<<j<<"\n";
            
            if(k==-1)
            {
              flag=0;
              break;
            }
        }
        if (flag) count++;
      }
            
      cout<<"Case #"<<n<<": "<<count<<"\n";
    }
    //getchar();
}
    























