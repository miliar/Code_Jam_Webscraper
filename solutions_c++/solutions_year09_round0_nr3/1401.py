#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
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
#include <ctime>

#define FOR(zzz,a) for(int zzz=0; zzz<(int)(a); zzz++)
#define FORE(zzzz,a) for(int zzzz=1; zzzz<=(int)(a); zzzz++)
#define All(v) (v).begin(), (v).end()
#define zfill(a) memset(&a, 0 , sizeof(a))
#define nfill(a) memset(&a, -1, sizeof(a))
#define S(aaa) scanf("%d",&aaa)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;

int main()
{
int ii,t,j,i;
string cmp="welcome to code jam";
S(t);
cin.ignore (numeric_limits<streamsize>::max(),'\n');
FOR(ii,t)
         {
              string s;
              getline(cin,s,'\n');           
              int final=0,start=0,sol=0;
              int cnt[3][550];
              FOR(j,s.size()+1)cnt[0][j]=1;
              FOR(i,19)
              {
                    final = (final+1)%2;
                    cnt[final][0]=0;
                    FORE(j,s.size())
                    {
                        cnt[final][j]=cnt[final][j-1];
                        if(cmp[i]==s[j-1])cnt[final][j]=(cnt[start][j - 1]+cnt[final][j])%10000;
                    } 
                    start = final;  
              } 
              int pr = cnt[1][s.size()];
              printf("Case #%d: ",ii+1);
              if(pr>999)
              cout<<cnt[1][s.size()]<<endl;
              else
              if(pr>99) 
              cout<<"0"<<cnt[1][s.size()]<<endl;  
              else
              if(pr>9)
              cout<<"00"<<cnt[1][s.size()]<<endl;
              else
              if(pr>0) 
              cout<<"000"<<cnt[1][s.size()]<<endl;
              else
              cout<<"0000"<<endl;             
         }
return 0;
}

