#include <cstdio>
#include <vector>
#include <utility>
#include <cstring>
#include <stack>
#include <algorithm>
using namespace std;

const int N=2000;
bool b[N];
int a[N];

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    //
    int Tests;
    scanf("%d",&Tests);
    for(int Test=1;Test<=Tests;Test++)
    {
        printf("Case #%d: ", Test);
        //
        int n;
        scanf("%d",&n);
        for(int i=0;i<n;i++)
        {
            scanf("%d",a+i);
            a[i]--;
        }
        int res=0;
        memset(b,0,sizeof(bool)*n);
        for(int i=0;i<n;i++)
            if(!b[i])
            {
                b[i]=false;
                int t=a[i];
                if(t!=i)
                {
                    res++;
                    while(t!=i)
                    {
                        b[t]=true;
                        t=a[t];
                        res++;
                    }
                }
            }
        printf("%d.000000",res);
        //
        printf("\n");
    }
    return 0;
}
