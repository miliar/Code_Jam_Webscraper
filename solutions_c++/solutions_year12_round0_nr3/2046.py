#include <iostream>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <cstring>
#include <vector>
#include <map>
#include <queue>
#include <deque>
#include <stack>
#include <cctype>
#include <set>
#include <cmath>
#include <climits>
#include <sstream>
#include <fstream>
#include <list>
#include <functional>
#include <utility>
#include <iomanip>
#include <ctime>

using namespace std;

#define SZ size()
#define pp push_back

typedef long long LL;
typedef vector <int> vi;
typedef vector <double> vd;
typedef vector <vi> vvi;
typedef vector <string> vs;
typedef pair<int,int> pii;
typedef vector <LL> vll;

map<int, set<int> > mp;
map<int, set<int> >::iterator it;

int isThereTrailingZero(string s) {
    if(s[0] == '0') return 1;
    return 0;
}

set<int> sti;
set<int>::iterator stiIt;

int main() {
    freopen("recycled_numbers.in","r",stdin);
    freopen("recycled_numbers.out","w",stdout);
    int n,m;
    int a,b;
    char s[100];
    char t[100];
    int smallA;
    int bigB;
    string res;
    string x,y;
    int ret;
    scanf("%d",&n);
    for(int i=0;i<n;i++) {
            mp.clear();
            scanf("%d %d",&a,&b);
            sprintf(s,"%d",a);
            smallA = (s[0]-'0');
            sprintf(s,"%d",b);
            bigB = (s[0]-'0');
            for(int j=a;j<=b;j++) {
                    sprintf(s,"%d",j);
                    res =""; res+=s;
                    for(int k=1;k<strlen(s);k++) {
                            x = res.substr(0,k);
                            y = res.substr(k);
                            if((y[0]-'0') > bigB || (y[0]-'0') < smallA) continue;
                            x = y+x;
                            if(isThereTrailingZero(x)) continue;
                            m = atoi(x.c_str());
                            if(m >= a && m<=b) {
                                 int sma = min(m,j);
                                 int bg = max(m,j);
//                                 printf("%d %d\n",sma,bg);
                                 if(sma != bg) {
                                        it = mp.find(sma);
                                        if(it != mp.end())
                                        {
                                              sti = it->second;
                                              sti.insert(bg);
                                              mp[sma] = sti;
//                                              mp.insert(pair<int , set<int> > (sma,sti) );
                                        }
                                        else
                                        {
                                            set<int> stiTemp;
                                            stiTemp.insert(bg);
                                            mp[sma] = stiTemp;
//                                            mp.insert( pair<int , set<int> >(sma,stiTemp) );
                                        }
                                 }
                            }        
                    }
            }
            ret = 0;
            for ( it=mp.begin() ; it != mp.end(); it++ )
            {
                sti = it->second;
/*                for(stiIt = sti.begin(); stiIt != sti.end(); stiIt++)
                {
                          printf("%d %d\n",it->first,*stiIt);
                }
*/
//                printf("\n");
                ret+=sti.size();
            }
            printf("Case #%d: %d\n",i+1,ret);
    }
    return 0;
}
