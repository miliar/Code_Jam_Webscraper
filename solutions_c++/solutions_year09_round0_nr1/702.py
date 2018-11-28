#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <iostream>

#define X real()
#define Y imag()
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )
#define EPS 1e-12
#define EPS2 1e-3

using namespace std;

typedef long long ll;
typedef long double ld;

char dir[5100][20];
char pat[450];
set<char> match[15];


int main()
{
    int l,d,n;
    scanf("%d %d %d\n",&l,&d,&n);
    FR(i,d)
    {
        gets(dir[i]);
    }
    FR(i,n)
    {
        gets(pat);
        int len=strlen(pat);
        int cur=0;
        int j=0;
        for(;j<l;j++)
        {
            if(cur>=len) break;
            match[j].clear();
            if(pat[cur]=='(')
            {
                while(pat[++cur]!=')')
                {match[j].insert(pat[cur]);
           //         cout << "j: " << j << " " << pat[cur] << endl; 
                }
                cur++;
            }
            else
                match[j].insert(pat[cur++]);
        }
        assert(j==l);
        int acum=0;
        FR(j,d)
        {
          //  cout << dir[j] << endl;
            FR(k,l)
            {
                if(match[k].find(dir[j][k])==match[k].end()) break;
                if(k==l-1) acum++;
            }
        }
     //   cout << acum << endl;
        printf("Case #%d: ",i+1);
        cout << acum << endl;
    }
}