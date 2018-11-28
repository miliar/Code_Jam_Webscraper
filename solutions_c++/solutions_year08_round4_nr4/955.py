#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <ctime>

#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define tr(c,i) for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++) 
#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end())
#define rep(i,a,n) for(int i = a; i < n; i++)

using namespace std;
int k;
string s;
vector<int> p;

string encode()
{
    string ans = s;
    int t = s.length() / k;
    int len = s.length();
    
    for(int i = 0; i < t; i++)
    {
        for(int j = 0; j < k; j++)
        {
            ans[ i*k + j] = s[i*k + p[j]];  
            
        }        
    }
    //cout<<endl<<ans;
    return ans;           
}

int compress(string ans)
{
       int t = 1;
       int sss = 1;
       string ss = "";
       ss += ans[0];
       for(int i = 1; i < ans.length(); i++)
       {
          if(ans[i] == ans[i-1]) t++;
          else
          {
              if(t != 1)
              {
                   ostringstream sout;
                   sout<<t;
                   ss += sout.str();
              }
              ss += ans[i];
              t = 1;    
              sss++;
          }         
       }
       return sss;       
}
int main()
{
    int cases;
    cin >> cases;
    int cnt = 1;
    int mmm;
    while(cases--)
    {
        cin >> k >> s;
        p.clear();
        for(int i = 0; i < k; i++)
                p.pb(i);
    
        mmm = s.length() + 2;
        //cout<<endl<<endl<<endl;
        do{
              
              //cout<<endl;
              //tr(p, itr) cout<<*itr<<" ";
              
              //string ss = compress(encode());
              //cout<<"\t"<<ss<<" : "<<ss.length();
              int t = compress(encode());
              if(mmm > t) mmm = t;
              
        }while(next_permutation(all(p)));
        
        cout<<"Case #"<<cnt<<": "<<mmm<<endl;
        cnt++;
    }
    return 0;
}

