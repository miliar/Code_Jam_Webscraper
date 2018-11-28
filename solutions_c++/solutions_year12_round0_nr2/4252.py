#include<iostream>
#include<cstring>
#include<algorithm>
#include<stack>
#include<queue>
#include<map>
#include<vector>
#include<sstream>
#include<cctype>
using namespace std;
int main()
{
        int t;
        cin>>t;
        int j=1;
        while(t--)
        {
                int N,S,p,ti,ans=0;
                scanf("%d %d %d",&N,&S,&p);
                for(int i=1;i<=N;i++)
                {
                        scanf("%d",&ti);
                        int avg=ti/3;
                        if(p>ti) continue;
                        if(avg>=p){ ans++; continue; }
                        int c=(ti-p)/2;
                        if(p-c<=1){ ans++; continue; }
                        if((p-c==2)&&S>0){ ans++; S--; continue; }
                }
                printf("Case #%d: %d\n",j,ans);
                j++;
        }               
        return 0;
}
