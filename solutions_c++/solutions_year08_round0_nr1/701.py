#include <stdio.h>
#include <string>
#include <map>
#include <set>
using namespace std;

map<string,int> mp;
set<int> st;
int main()
{
    freopen("1.out","w",stdout);
    int t,c=1;
    char tmp[110];
    scanf("%d",&t);
    while(t--)
    {
        int s,q,ans=0;
        mp.clear();
        st.clear();
        scanf("%d",&s);
        getchar();
        for(int i=1;i<=s;i++)
        {
            gets(tmp);
            mp[tmp]=i;
        }
        scanf("%d",&q);
        getchar();
        for(int i=0;i<q;i++)
        {
            gets(tmp);
            st.insert(mp[tmp]);
            if(st.size()==s)
            {
                ans++;
                st.clear();
                st.insert(mp[tmp]);
            }
        }
        printf("Case #%d: %d\n",c++,ans);
    }
}
