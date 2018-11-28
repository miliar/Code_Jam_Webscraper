#include<iostream>
#include<cstdio>
using namespace std;
char a[5005][18];

int main()
{
    freopen( "input.in", "r", stdin );
    freopen( "output.out", "w", stdout );
    
    int l,d,n,i,j,k,cnt,flag,p;
    char s[1000];
    while(scanf("%d%d%d",&l,&d,&n)!=EOF)
    {
        for(i=0;i<d;i++)
            scanf("%s",a[i]);
        for(i=0;i<n;i++)
        {
            int ans=0;
            scanf("%s",s);
            for(j=0;j<d;j++)
            {
                cnt=0;
                flag=0;
                k=0;
                p=0;
                while(k<l)
                {
                    while(s[cnt]!=a[j][k]&&cnt<strlen(s))
                    {
                        if(s[cnt]=='(')
                            p=1;
                        if(s[cnt]==')')
                        {
                            flag=1;
                            break;
                        }
                        cnt++;
                    }
                    if(flag||cnt==strlen(s))
                    {
                        flag=1;
                        break;
                    }
                    while(s[cnt]!=')'&&p)
                        cnt++;
                    if(s[cnt]==')')
                        p=0;
                    cnt++;
                    k++;
                }
                if(k==l&&!flag)
                {
                    ans++;
//                    cout<<a[j]<<endl;
                }
            }
            printf("Case #%d: %d\n",i+1,ans);
        }
    }
    return 0;
}
