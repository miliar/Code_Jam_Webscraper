#include <iostream>
using namespace std;

const int phlen = 19;
const int module = 10000;
const char phrase[phlen + 1] = "welcome to code jam";

int kresults[32];

char mas[2048];

int main()
{
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    int n;
    scanf("%d",&n);
    char c;
    while (c!='\n')
        scanf("%c",&c);
    for(int nowt=0;nowt<n;nowt++)
    {
        memset(kresults,0,sizeof(kresults));
        kresults[0]=1;
        gets(mas);
        for(char *now = mas; *now != 0; now++)
            for(int i=0;i<phlen;i++)
                if (kresults[i]>0 && phrase[i] == *now)
                    kresults[i+1] = (kresults[i+1]+kresults[i]) % module;
        printf("Case #%d: ",nowt+1);
        if (kresults[19]==0)
            printf("0000\n"); 
        else
        {
            int temp = module/10;
            while (kresults[19]<temp)
            {
                printf("0");
                temp=temp/10;                
            }        
            printf("%d\n",kresults[19]);
        }
    }
    return 0;
}
