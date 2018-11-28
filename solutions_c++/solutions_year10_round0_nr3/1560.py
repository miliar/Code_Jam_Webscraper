#include<iostream>
#include<algorithm>
using namespace std;

long long q[1100];
long long num[1100];
int p[1100];
int main(void)
{
    freopen("1.in","r",stdin);
    freopen("1.out","w",stdout);
    int T;
    int CAS=1;
    scanf("%d",&T);
    while(T--)
    {
        long long sum=0;
        long long R,K;
        int N;
        cin>>R>>K>>N;
        for(int i=0;i<N;i++)
        {
           cin>>num[i];
           sum+=num[i];
        }
        long long ans=0;
        if(sum<=K)
        {
            ans=sum*R;
        }
        else
        {
            int t=0;
            int k=1;
            long long tmp=0;
            memset(p,0,sizeof(p));
            memset(q,0,sizeof(q));
            p[0]=1;
            while(true)
            {
                while(tmp+num[t]<=K)
                {
                    tmp+=num[t];
                    t=(t+1)%N;
                }
                q[k++]=tmp;
                tmp=0;
                if(!p[t])
                   p[t]=k;
                else
                   break;
                
                
            }
         /*   cout<<k<<endl;
            for(int i=1;i<k;i++)
               cout<<q[i]<<" ";
            cout<<endl;
            cout<<p[t]<<endl;*/
            if(R<k)
            {
                for(int i=1;i<=R;i++)
                    ans+=q[i];
            }
            else
            {
             //  cout<<"2s"<<endl;
               for(int i=1;i<k;i++)
               {
                   ans+=q[i];
               }
               int sk=k-p[t];
               long long xy=0;
               for(int i=p[t];i<k;i++)
                   xy+=q[i];
               
               int m=R-k+1;
               ans+=xy*(m/sk);
               m%=sk;
               for(int i=0,j=p[t];i<m;i++,j++)
               {
                    ans+=q[j];
               }
            }
           
        }
        printf("Case #%d: ",CAS++);
        cout<<ans<<endl;
    
    }
    return 0;
}
