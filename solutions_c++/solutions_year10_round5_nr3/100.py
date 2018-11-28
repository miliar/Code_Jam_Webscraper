#include <cstdio>
#include <vector>
#include <map>

using namespace std;

int tst()
{
    int n;
    scanf("%d",&n);
    int ans=0;
    map<int,int> m;
    for(int i=0;i<n;i++)
    {
        int a,b;
        scanf("%d%d",&a,&b);
        m[a]+=b;
    }
    for(;;)
    {
        bool ok=true;

        for(map<int,int>::iterator it=m.begin();it!=m.end();++it)
        {
            if(it->second>1)
            {
                ok = false;
                int k = it->first;
                m[k] -= 2;
                m[k+1]+=1;
                m[k-1]+=1;
                ans++;
                break;
            }
        }


        if(ok)
            return ans;
    }




}
int main()
{
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
        printf("Case #%d: %d\n",i,tst());
}
