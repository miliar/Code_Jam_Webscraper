#include<cstdio>
#include<memory.h>
#include<queue>
#define MAX 1010
using namespace std;

int val[MAX];
long long num[MAX];
bool visited[MAX];
int g[MAX];
int k;
int R;
int t;
int n;

int main()
{
    int z=0;
    int i;
    scanf("%d",&t);
    while(t--)
    {
        memset(val,0,sizeof(val));
        long long result=0;
        int c=0;
        int p=1;
        long long count=0;
        int s=0;
        scanf("%d%d%d",&R,&k,&n);
        for(i=0;i<n;i++)
            scanf("%d",&g[i]);
        /*for(i=0;i<n;i++)
            printf("%d\n",g[i]);*/
        
        while(R>0)
        {
            if(val[c]!=0)
            {
                result+=(result-num[c])*(R/(p-val[c]));
                R%=(p-val[c]);
                break;
            }
            else
            {
                //printf("out\n");
                count=0;
                val[c]=p++;
                num[c]=result;
                s=c;
                //printf("%d %d\n",count+g[c],R);
                while(count+g[c]<=k)
                {
                    count+=g[c];
                    c=(c+1)%n;
                    if(c==s)
                        break;
                    //printf("%d %d\n",c,count);
                }
                result+=count;
                //printf("%d %d\n",count,result);
                R--;
            }
        }
        while(R>0)
        {
            s=c;
            count=0;
            while(count+g[c]<=k)
            {
                count+=g[c];
                c=(c+1)%n;
                if(s==c)
                    break;
            }
            result+=count;
            R--;
        }
        printf("Case #%d: %lld\n",++z,result);
    }
    return 0;
}

