#include <vector>
#include <utility>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <stack>
#include <queue>
#include <string>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <cstdio>
#include <list>
#include <bitset>

using namespace std;

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> vint;
typedef vector<string> vstr;
typedef pair<int, int> pint;

#define TWO(k)  (1<<k)
#define TWOL(k) (((LL)(1)<<(k)))
#define MP make_pair
#define MIN(a,b) ( (a)<(b)?(a):(b) )
#define MAX(a,b) ( (a)>(b)?(a):(b) )
#define LS(x) 	 ((x)<<1)
#define RS(x) 	 (((x)<<1)+1)

const double PI = acos(-1.0);
const double EPS = 1e-9;
const int oo = 210000000;

int main()
{
    //freopen("B-small-attempt0.in.txt","r",stdin);freopen("out.txt","w",stdout);
    int t, test = 0;
    scanf("%d", &t);
    while(t--)
    {
        pair<char, char> p1;
        map<pair<char,char>, char> m1;
        int hash[140][140];
        int n; scanf("%d", &n);
        char tmp[110];
        memset(hash, 0, sizeof(hash));
        for(int i = 0; i < n; i++)
        {
           scanf("%s", tmp); //cout<<tmp<<endl;
           p1 = MP(tmp[0], tmp[1]);
           m1[p1] = tmp[2];
           p1 = MP(tmp[1], tmp[0]);
           m1[p1] = tmp[2];
        }
        scanf("%d", &n);
        for(int i = 0; i < n; i++)
        {
            scanf("%s", tmp);
            hash[tmp[0]][++hash[tmp[0]][0]] = tmp[1];
            hash[tmp[1]][++hash[tmp[1]][0]] = tmp[0];
        }
        scanf("%d", &n);
        scanf("%s", tmp);
        n = strlen(tmp);
        char ans[140];
        int top = -1;
        for(int i = 0; i < n; i++)
        {
            ans[++top] = tmp[i];
            if( top >= 1)
            {
                p1 = MP(ans[top], ans[top-1]);
                if( m1.find(p1) != m1.end())
                {
                    ans[--top] = m1[p1];
                    continue;
                }
                bool flag = 0;
                for(int j = 0; j < top; j++)
                {
                    for(int k = 1; k <= hash[ans[top]][0]; k++)
                    {
                       if( hash[ans[top]][k] == ans[j])
                       {
                           flag = 1;
                           break;
                       }
                    }
                }
                if(flag) top = -1;
            }
        }
        cout<<"Case #"<<++test<<": [";
        for(int i = 0; i < top; i++) cout<<ans[i]<<", ";
        if(top >= 0) cout<<ans[top];
        cout<<"]\n";
    }
    return(0);
}
            
            
        
