#include <cstdio>
#include <cstring>
#include <string>
using namespace std;
string pat = "welcome to code jam";
int main()
{
    char inp[501];
    
    int n;
    scanf("%d\n",&n);
    for(int i=1;i<=n;i++)
    {
        gets(inp);

        int ile[20];
        bzero(ile,sizeof(ile));
        ile[0]=1;
        for(int j=0;inp[j];j++)
        {
            for(int k=19;k>0;k--)
            {
                if(inp[j]==pat[k-1])
                {
                    ile[k]+=ile[k-1];
                    ile[k]%=10000;
                }
            }
        }
        printf("Case #%d: ",i);
        if(ile[19]<1000) putchar('0');
        if(ile[19]<100) putchar('0');
        if(ile[19]<10 ) putchar('0');
        printf("%d\n",ile[19]);
    }
}
