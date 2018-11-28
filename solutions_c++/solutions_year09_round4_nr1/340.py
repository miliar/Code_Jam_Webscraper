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
#define PB push_back
#define MP make_pair
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )
#define EPS 1e-9
using namespace std;

typedef long double ld;
typedef long long ll;
typedef pair<int,int> pii;

vector<bool> mat[40];

int main()
{
    int t;
    scanf("%d",&t);
    FR(i,t)
    {
        int n;
        printf("Case #%d: ",i+1);
        scanf("%d",&n);
     //   cout << "n: " << n << endl;
        FR(j,n)
        {
            mat[j].clear();
            string s;
            cin >> s;
        //    cout << s << endl;
            FR(k,n)
            {
           //     cout << "k: " << k << endl;
                mat[j].PB(s[k]=='1');
           //     cout << mat[j].size() << endl;
            }            
        }
        
        vector<int> c(n,0);
        FR(i,n) c[i]=i;
        int minns=100000;
        do
        {
            vector<bool> mat2[40];
            FR(i,n)
            {
                mat2[c[i]]=mat[i];
            }
            int curr=0;
            vector<int> cur=c;

            for(int r=0;r<n;r++)
                for(int c=r+1;c<n;c++)
                {
                    if(mat2[r][c])
                    {
                        goto CC;
                    }
                }
            
            FR(i,n)
            {
                for(int k=i-1;k>-1;k--)
                {
                    if(cur[k]>cur[k+1])
                    {
                        swap(cur[k],cur[k+1]);
                        curr++;
                    }
                }
            }
            
            minns=min(minns,curr);
            
        CC:;
            
        }
        while(next_permutation(c.begin(),c.end()));
              
        cout << minns<< endl;
                            
    }

}