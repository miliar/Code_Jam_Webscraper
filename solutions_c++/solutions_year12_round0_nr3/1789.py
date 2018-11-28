#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
using namespace std;
typedef long long ll;
const int N=2000010;
int used[N];
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("hello.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int st=1;st<=t;st++)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        int cnt=0;
        memset(used,0,N*sizeof used[0]);
        for(int i=a;i<=b;i++)
        {
            int r=i,n=i;
            vector <int> v;
            while (r)
            {
                v.push_back(r%10);
                r/=10;
            }
            reverse(v.begin(),v.end());
            for(int j=1;j<v.size();j++)
            {
                if (!v[j])
                    continue;
                int cur=0;
                for(int q=j;q<v.size();q++)
                    cur=cur*10+v[q];
                for(int q=0;q<j;q++)
                    cur=cur*10+v[q];
                if (cur>n && cur>=a && cur<=b && used[cur]!=n)
                {
                    used[cur]=n;
                    cnt++;
                }
            }
        }
        printf("Case #%d: %d\n",st,cnt);
    }
    return 0;
}
