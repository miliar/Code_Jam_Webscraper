#include<cstdio>
#include<iostream>
#include<cstring>
#include<string>
using namespace std;
const int MAXN=205;
int T,C,D,N;
char s[MAXN];
char ans[MAXN];
typedef struct
{
    char s1,s2,s3;
}node1;
node1 a1[MAXN];
typedef struct
{
    char s1,s2;
}node2;
node2 a2[MAXN];
int main()
{
    freopen("data.in","r",stdin);
    freopen("data.out","w",stdout);
    cin>>T;
    //printf("%d\n",T);
    for(int cas=1;cas<=T;cas++)
    {
        int i,j,k,sum=-1,flag;
        cin>>C;
        for(i=1;i<=C;i++)
            cin>>a1[i].s1>>a1[i].s2>>a1[i].s3;
        cin>>D;
        for(i=1;i<=D;i++)
            cin>>a2[i].s1>>a2[i].s2;
        cin>>N;
        for(i=0;i<N;i++) 
            cin>>s[i];
        //for(i=1;i<=C;i++)
            //printf("%c %c %c\n",a1[i].s1,a1[i].s2,a1[i].s3);
        //for(i=0;i<N;i++)
           // cout<<s[i];
            //cout<<endl;
        memset(ans,0,sizeof(ans));
        for(i=0;i<N;i++)
        {
            ans[++sum]=s[i]; 
            //ans[++sum]=0;
            //cout<<i<<" "<<ans<<" ";
            //sum--;
            if(sum>=1)
            {
                for(j=1;j<=C;j++)
                        if(a1[j].s1==ans[sum]&&a1[j].s2==ans[sum-1]||a1[j].s2==ans[sum]&&a1[j].s1==ans[sum-1]) break;
                //printf("ttt %c %c %c %c ttt ",a1[j].s1,a1[j].s2,ans[sum],ans[sum-1]);
                if(j!=C+1) {ans[--sum]=a1[j].s3;}
            }
            if(sum>=1)
            {
                flag=0;
                for(j=sum-1;j>=0;j--)
                {
                    for(k=1;k<=D;k++)
                    {
                        if(a2[k].s1==ans[sum]&&a2[k].s2==ans[j]||a2[k].s2==ans[sum]&&a2[k].s1==ans[j]) 
                        {
                            sum=-1;
                            flag=1;
                            break;      
                        }
                    }
                    if(flag) break;
                }
            }
            //ans[++sum]=0;
            //cout<<ans<<endl;
            //sum--;
        }
        printf("Case #%d: [",cas);
        for(i=0;i<=sum;i++)
            printf(i==0?"%c":", %c",ans[i]);
        printf("]\n");
        //printf("%d %d %d\n",C,D,N);
    }
    return 0;
}
                    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
