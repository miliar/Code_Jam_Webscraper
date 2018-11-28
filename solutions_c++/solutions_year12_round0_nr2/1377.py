#include <iostream>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
#define maxn 200
int T;
int n,s,p;
int t[maxn];
int main()
{
    int i,ans,cc;
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    while(cin >> T)
    {
        cc = 1;
        while(T--)
        {
            cin >> n;
            cin >> s;
            cin >> p;
            for(i = 0; i < n; i++)
            {
                cin >> t[i];
            }
            sort(t,t+n);
            ans = 0;
            for(i = 0; i < n; i++)
            {
                switch(t[i]%3)
                {
                    case 0:
                        if(s!=0&&t[i]/3-1>=0&&t[i]/3+1<=10)
                        {
                            if(t[i]/3+1 >= p){
                                s--;
                                ans++;

                            }
                        }
                        else
                        {
                            if(t[i]/3 >= p)
                                ans++;
                        }
                        break;
                    case 1:
                        if(s!=0 && t[i]/3-1>=0 && t[i]/3+1<=10)
                        {

                            if(t[i]/3+1 >= p)
                            {
                                s--;
                                ans++;
                            }
                        }
                        else if(t[i]/3+1 <=10)
                        {
                            if(t[i]/3+1 >= p)
                                ans++;
                        }
                        break;
                    case 2:
                        if(s!=0 && t[i]/3 + 2 <= 10 && t[i]/3 >= 0)
                        {

                            if(t[i]/3+2 >= p)
                            {
                                s--;
                                ans++;
                            }

                        }
                        else if(t[i]/3 + 1 <=10)
                        {
                            if(t[i]/3+1 >= p)
                                ans++;
                        }
                        break;
                }
                //cout << ans << endl;
            }
            printf("Case #%d: %d\n",cc++,ans);

        }
    }
    return 0;
}
