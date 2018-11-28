#include<iostream>
#include<cmath>
using namespace std;
bool use[150];
char str[100];
int dy[150];
bool dd[150];
int main()
{
    int cases;
    int ca=0;
    scanf("%d",&cases);
    while(getchar()!='\n');
    while(cases--)
    {
        ca++;
        memset(use,0,sizeof(use));
        gets(str);
        int len=strlen(str);
        int pp=0;
        for(int i=0;i<len;i++)
            if(!use[str[i]])
            {
                pp++;
                use[str[i]]=true;
            }
        if(pp==1)
        pp=2;
        __int64 res=0;
        memset(dd,0,sizeof(dd));
        dd[str[0]]=true;
        dy[str[0]]=1;
        int p=0;
        for(int i=1;i<len;i++)
        {
            if(!dd[str[i]])
            {
                if(!p)
                {
                    dd[str[i]]=true;
                    dy[str[i]]=0;
                    p=2;
                }
                else
                {
                    dd[str[i]]=true;
                    dy[str[i]]=p;
                    p++;
                }
            }
        }
        for(int i=0;i<len;i++)
           res+=dy[str[i]]*ceil( pow((double)pp,len-i-1));
        printf("Case #%d: %I64d\n",ca,res);
    }
}
        
