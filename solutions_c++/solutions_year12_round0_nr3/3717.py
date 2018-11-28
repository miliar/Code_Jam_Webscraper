#include <cstdio>
#include <map>
#include <cmath>

using namespace std;
int main (int argc, char const* argv[])
{

    int t;
    scanf("%d",&t);
    char str[200];
    map<int,bool> mmap;
    int i,j,k;
    int a,b;
    int t1,t2,p;
    int ans;
    int len;
    for ( i = 1; i <= t; i += 1)
    {
        scanf("%d%d%n",&a,&b,&len);
        len--;
        len/=2;
        ans=0;
        if(len==1)
        {
            printf("Case #%d: %d\n",i,ans);
            continue;
        }
        
        for ( j = a; j <= b; j += 1)
        {
            t1=j;
            p=pow(10,len-1);
            mmap.clear();
            for (k = 0; k < len; k += 1)
            {
                if(t1>j && t1>=a && t1<=b)
                {
                    if(!mmap[t1])
                        ans++;
                    mmap[t1]=1;
                }
                t1=t1%p*10+t1/p;
            }
        }
        printf("Case #%d: %d\n",i,ans);


    }
    return 0;
}
