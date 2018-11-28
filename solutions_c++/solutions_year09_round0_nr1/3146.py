/* Sushil Kumar Singh */
#include <cassert>
#include <cctype>
#include <cfloat>
#include <cmath>
#include <cstdarg>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

#include <complex>
#include <deque>
#include <functional>
#include <iostream>
#include <iomanip>
#include <iterator>

#include <list>
#include <map>
#include <memory>
#include <new>
#include <numeric>
#include <queue>
#include <set>

#include <stack>
#include <string>
#include <utility>

#include <vector>

using namespace std;


#define FOR(a,x,y) for(int a = (x); a < (y); ++a)
#define REP(a,n) FOR(a,0,n)
#define FORE(it,x) for(typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define CLEAR(x,with) memset(x,with,sizeof(x))
#define sz size()
typedef long long ll;



template<class T> inline int size(const T&c) { return c.size(); }

int main()
{
  int L,D,N,cas=1;
  cin>>L>>D>>N;
  vector<string>vs(D),vv;
  string str,temp;
  for(int i=0;i<D;i++)
  {
          cin>>str;
          vs[i]=str;
  }
  int len,ret=0,k;
  for(int j=0;j<N;j++)
  {
          cin>>str;
          vv.clear();
          len=str.size();
          ret=0;        
          for(int i=0;i<len;i++)
          {
                  if(str[i]=='(')
                  {
                                 i++;
                                 k=0;
                                 while(str[i+k]!=')')
                                 {
                                                  
                                      k++;
                                 }
                                 
                                 vv.pb(str.substr(i,k));
                                 i+=k;
                                 
                  }
                  else
                  {
                                 vv.pb(str.substr(i,1));
                                 
                  }
          }
          len=vv.size();
          
          
          if(len!=L)
          {
                    cout<<"Case #"<<cas++<<": 0\n";
          }
          else
          {
                    
                    bool flag2=true;
                    for(int i=0;i<D;i++)
                    {
                            flag2=true;
                            for(int k=0;k<L && flag2;k++)
                            {
                                    //cout<<count(vv[k].begin(),vv[k].end(),vs[i][k])<<endl;
                                    //system("pause");
                                    if(!count(vv[k].begin(),vv[k].end(),vs[i][k]))
                                    {
                                        flag2=false;
                                    }
                            }
                            if(flag2)
                            {
                                     ret++;
                            }
                    }
                    cout<<"Case #"<<cas++<<": "<<ret<<endl;;
          }
  }                          
                            
                      
                  
  
                                 
                                     

  return 0;
}

/*

3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
*/

