#include <iostream>
#include <string>
using namespace std;

typedef struct engine
{
    char name[200];
};

char s[200][200];
engine a[1001];

int main()
{
    int n;
    int p,q;
    int sum=0;
    int max=0;
    int tp=0;
    int i=0,j=0;
    while(cin>>n)
    {
    for(int count=0;count<n;count++)
    {
        cin>>p;
        getchar();
        memset(s,0,sizeof(s));
        for(i=0;i<p;i++)
        {
            gets(s[i]);
        }
        cin>>q;
        getchar();
        if(q==0)
        {
            printf("Case #%d: 0\n",count+1);
            continue;
        }
        memset(a,0,sizeof(a));
        for(i=0;i<q;i++)
        {
            gets(a[i].name);
        }
        int tp1=0;
        int i=0;
        int j=0;
        int swith=0;
        int num=0;
        while(num<q)
        {
            max=0;
            tp=tp1;
            for(i=0;i<p;i++)
            {
                sum=0;
                
                for(j=tp1;j<q;j++)
                {
                    if(strcmp(s[i],a[j].name)==0)
                    {
                        break;
                    }
                    else
                    {
                        sum++;
                    }
                }
                if(sum>max)
                {
                    max=sum;                   
                    tp=j;
                }
            } 
            tp1=tp;
            num+=max;
            swith++;          
        }
        printf("Case #%d: %d\n",count+1,swith-1);
        
    }
}
}
