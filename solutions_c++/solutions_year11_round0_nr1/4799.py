#include<iostream> 
#include<cstdio> 
#include<algorithm> 
#include<cstring> 
#include<string>
#include<cmath> 
#include<vector> 
#include<queue> 
#include<map>
#include<ctime>
#include<set>
typedef __int64 lld; 
using namespace std; 
#define debug(x) cout<<#x<<"="<<x<<endl;
#define here cout<<"_______________here "<<endl;
#define clr(NAME,VALUE) memset(NAME,VALUE,sizeof(NAME)) 
#define MAX 0x7f7f7f7f
#define PI 3.14159265358979323 
#define N 110
int a[N];
int num[N];
int main() {
    freopen("3","r",stdin);
    freopen("4","w",stdout);
    int T,n;
    int pos,ans;
    int cas=1;
    char str[10];
    int po,pb;
    scanf("%d",&T);
    while(T--)
    {
        clr(a,0);
        clr(num,0);
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%s",&str);
            if(str[0]=='O')
            {
                a[i]=0;
            }
            else
            {
                a[i]=1;
            }
            scanf("%d",&num[i]);
        }
        ans=0;
        po=1,pb=1;
        int j;
        int tot=0;
        for(int i=0;i<n;) {
            if(a[i]==0) {
                tot=abs(num[i]-po)+1;
                po=num[i];
                for(j=i+1;j<n;j++)
                {
                    if(a[j]==1)
                    {
                        break;
                    }
                    else
                    {
                        tot+=abs(num[j]-po)+1;
                        po=num[j];
                    }             
                }
                //cout<<"tot "<<tot<<" j "<<j<<endl;
                ans+=tot;
                i=j;
                if(pb>num[j])
                {
                    if(num[j]+tot>pb)
                    {
                        pb=num[j];
                    }
                    else {
                        pb=pb-tot;
                    }    
                } else {
                    if(pb+tot>num[j]) {
                        pb=num[j];
                    } else {
                        pb=pb+tot;
                    }
                }
            } else {
                tot=abs(num[i]-pb)+1;
                pb=num[i];
                for(j=i+1;j<n;j++)
                {
                    if(a[j]==0)
                    {
                        break;
                    }
                    else
                    {
                        tot+=abs(num[j]-pb)+1;
                        pb=num[j];
                    }             
                }
                //cout<<"tot "<<tot<<" j "<<j<<endl;
                ans+=tot;
                i=j;
                if(po>num[j])
                {
                    if(num[j]+tot>po)
                    {
                        po=num[j];
                    }
                    else {
                        po=po-tot;
                    }    
                } else {
                    if(po+tot>num[j]) {
                        po=num[j];
                    } else {
                        po=po+tot;
                    }
                }    
            }
            //printf("%d %d %d\n",po,pb,ans);
        }
        printf("Case #%d: %d\n",cas++,ans);
    }
    //while(1);
    return 0;
}              
                
                    
            
 
