#include<stdio.h>
#include<algorithm>
#include<vector>
using namespace std;
int main()
{
    int T;
    scanf("%d",&T);
    for (int itr=1;itr<=T;itr++)
    {
        int N,S,P;
        scanf("%d %d %d",&N,&S,&P);
        vector<int>arr(N);
        for(int i=0;i<N;i++)
        {
            scanf("%d",&arr[i]);
        }
        sort(arr.begin(),arr.end());
        int ans=0;
        for(int i=N-1;i>=0;i--)
        {
            int val=arr[i];
            if(val%3==0)
            {
                if(val/3>=P)
                    ans++;
                else if(val/3+1>=P && S>0 && val!=0)
                {
                    ans++;
                    S--;
                }
            }
            else if(val%3==1)
            {
                if(val/3+1>=P)
                    ans++;
            }
            else if(val%3==2)
            {
                if(val/3+1>=P)
                {
                    ans++;
                }
                else if(val/3+2>=P && S>0)
                {
                     ans++;
                     S--;
                }
            }
        }
        printf("Case #%d: %d\n",itr,ans);
    }
    return 0;
}
