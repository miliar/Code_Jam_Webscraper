#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#define FOR(a,b,c) for(int (a) = (b), _n = (c); (a) <= _n ; (a)++)
#define FORD(a,b,c) for(int (a) = (b), _n = (c) ; (a) >= _n ; (a)--)
#define FOR_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) <= _n ; (a)+= _m )
#define FORD_N(a,b,c,n) for(int (a) = (b), _m = (n), _n = (c) ; (a) >= _n ; (a)-= _m)
#define EACH(v,it) for(__typeof(v.begin()) it = v.begin(); it != v.end() ; it++)
#define INF 200000000
#define MAX 40

using namespace std;

int c,d,n;
char comb[300][300];
bool oppose[300][300];
string str;
bool oppf[300];

int main()
{
  int t;
  freopen("B-large.in","r",stdin);
  freopen("Blarge.out","w",stdout);
  scanf("%d",&t);
  FOR(ca,1,t)
  {
    scanf("%d",&c);
    memset(oppose,false,sizeof(oppose));
    memset(comb,0,sizeof(comb));
    FOR(i,0,c-1)
    {
      string s;
      cin >> s;      
      comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2];
    }
    scanf("%d",&d);
    
    FOR(i,0,d-1)
    {
      string s;
      cin >> s;
      oppose[s[0]][s[1]] = oppose[s[1]][s[0]] = true;
    }
    scanf("%d",&n);
    cin >> str;  
    string res = "";
    int ind = 0;
    FOR(i,0,n-1)
    {
      if(ind == 0) 
      {
        res += str[i];
        ind++;
      }
      else if(comb[res[ind-1]][str[i]] != 0) res[ind-1] = comb[res[ind-1]][str[i]];
      else 
      {
        bool b = false;
        FOR(j,0,ind-1)
        {
          if(oppose[res[j]][str[i]]) 
          {
            b = true;
            break;
          }
        }
        if(b)
        {
          ind = 0;
          res = "";
        }
        else 
        {
          res += str[i];
          ind++;
        }
      }
    }
    printf("Case #%d: [",ca);
    FOR(i,0,ind-2)
    {
      printf("%c, ",res[i]);
    }
    if(res.length() > 0) printf("%c",res[ind-1]);
    puts("]");
  }
  return 0;
}
