#include <iostream>
#include <algorithm>
using namespace std;
int Da[5];
bool pp[105];
int p,q;
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("out.txt","w",stdout);
    int Cs;
    cin>>Cs;
    int t;
    int i;
    int ans,cnt;
    for(t=1;t<=Cs;t++)
    {
        ans=0x7fffffff;
        cin>>p>>q;
        for(i=0;i<q;i++)
        {
            cin>>Da[i];
        }
        sort(Da,Da+q);
        for(i=0;i<q;i++)
        {

            cnt=0; memset(pp,0,sizeof(pp));
            for(i=0;i<q;i++)
            {
                int l=Da[i]-1;int r=Da[i]+1;
                while(l>=1&&!pp[l])
                {

                    l--;
                    cnt++;
                }
                while(r<=p&&!pp[r])
                {
                    r++;
                    cnt++;
                }
                pp[Da[i]]=1;
            }
            ans=min(ans,cnt);
        }
        while(next_permutation(Da,Da+q))
        {
            memset(pp,0,sizeof(pp));
            cnt=0;
            for(i=0;i<q;i++)
            {
                int l=Da[i]-1;
                int r=Da[i]+1;
                while(l>=1&&!pp[l])
                {

                    l--;
                    cnt++;
                }
                while(r<=p&&!pp[r])
                {

                    r++;
                    cnt++;
                }
                pp[Da[i]]=1;
            }
            ans=min(ans,cnt);
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
