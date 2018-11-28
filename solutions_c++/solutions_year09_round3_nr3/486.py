#include <iostream>
#include <algorithm>
using namespace std;
int data[5];
bool prison[105];
int p,q;
int main()
{
    freopen("C-small-attempt1.in","r",stdin);
    freopen("out.txt","w",stdout);
    int Case;
    cin>>Case;
    int t;
    int i;
    int ans,cnt;
    for(t=1;t<=Case;t++)
    {
        ans=0x7fffffff;
        cin>>p>>q;
        for(i=0;i<q;i++)
        {
            cin>>data[i];
        }
        sort(data,data+q);
        for(i=0;i<q;i++)
        {
            memset(prison,0,sizeof(prison));
            cnt=0;
            for(i=0;i<q;i++)
            {
                int l=data[i]-1;
                int r=data[i]+1;
                while(l>=1&&!prison[l])
                {

                    l--;
                    cnt++;
                }
                while(r<=p&&!prison[r])
                {

                    r++;
                    cnt++;
                }
                prison[data[i]]=1;
            }
            //cout<<cnt<<endl;
            ans=min(ans,cnt);
        }
        while(next_permutation(data,data+q))
        {
            memset(prison,0,sizeof(prison));
            cnt=0;
            for(i=0;i<q;i++)
            {
                int l=data[i]-1;
                int r=data[i]+1;
                while(l>=1&&!prison[l])
                {

                    l--;
                    cnt++;
                }
                while(r<=p&&!prison[r])
                {

                    r++;
                    cnt++;
                }
                prison[data[i]]=1;
            }
            //cout<<cnt<<endl;
            ans=min(ans,cnt);
        }
        printf("Case #%d: %d\n",t,ans);
    }
    return 0;
}
