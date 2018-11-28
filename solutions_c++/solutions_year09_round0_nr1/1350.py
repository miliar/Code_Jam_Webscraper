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
string dic[5001];

map <string,int> mp;
int l,d,n,i,j,k,h;
scanf("%d%d%d",&l,&d,&n);
 FOR(i,d)  
         cin>>dic[i];      
 FOR(i,n)
   {
         string let[16],input;
         cin>>input;
         int bo=0,k=0,sol=0;
         
         
         FOR(j,input.size())
         {
                    if(input[j]=='(')
                    {
                             bo=1;
                             continue;   
                    }  
                    if(bo==1 && input[j]!=')')
                    {
                             let[k].push_back(input[j]);
                             continue;
                    }  
                    if(input[j]==')')
                    {
                              bo=0;k++;
                              continue;       
                    } 
                    let[k++].push_back(input[j]);
                     
         }     
                  
         FOR(k,d)
               {
                    int mm;
                    for(mm=0;mm<l;mm++)
                    if(let[mm].find(dic[k][mm])==string::npos)
                    break;
                    if(mm==l)sol++;
               }
               printf("Case #%d: %d\n",i+1,sol);  
   }

return 0;
}
