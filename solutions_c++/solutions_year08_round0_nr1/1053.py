#include <iostream>
#include <string>
#include <map>
#include <vector>
using namespace std;

int main()
{
    freopen("A.in","r",stdin); freopen("out.txt","w",stdout);
    char input[100000];
    int n;
    sscanf(gets(input), "%d", &n);
    for(int t=1; t<=n; t++)
    {
        //input search engines
        int s;
        sscanf(gets(input), "%d", &s);
        map <string, int> idx;
        vector <string> v;
        for(int i=1; i<=s; i++)
        {
            gets(input);
            idx[input] = i;
            v.push_back(input);
        }
        
        //input queries
        int q;
        sscanf(gets(input), "%d", &q);
        bool vis[s+1];
        memset(vis, 0, sizeof(vis));
        int total_vis = 0;
        
        //calculate
        int swt = 0;
        for(int i=0; i<q; i++)
        {
            gets(input);
            int pos = idx[input];
            if(pos > 0 && vis[pos] == 0)
            {
                total_vis ++;
                vis[pos] = 1;
                if(total_vis == s)
                {
                    total_vis = 0;
                    memset(vis, 0, sizeof(vis));
                    vis[pos] = 1;
                    total_vis = 1;
                    swt ++;
                }
            }
        }
        
        printf("Case #%d: %d\n", t, swt);
    }
}
