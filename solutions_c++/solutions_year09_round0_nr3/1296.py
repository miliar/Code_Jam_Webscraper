#include<stdio.h>
#include<iostream>
#include<string>
#include<string.h>

using namespace std;

int N,i,j,k,Q,p;
int a[555][22];
string s,gcj;
char c;

main()
{
    gcj="1welcome to code jam";
    freopen("c.in","r",stdin);
    freopen("c.out","w",stdout);
    scanf("%d%c",&N,&c);
    for(Q=1;Q<=N;Q++)
    {
        scanf("%c",&c);
        memset(a,0,sizeof(a));
        s="1";
        while(c!='\n') { s+=c; scanf("%c",&c); }
        a[0][0]=1; p=0;
        for(i=1;i<s.size();i++)
        {
            for(j=0;j<gcj.size();j++)
            {
                a[i][j]=a[i-1][j];
                if(s[i]==gcj[j])
                {
                    a[i][j]+=a[i-1][j-1];
                    a[i][j]%=10000;
                }
            }
        }
        printf("Case #%d: %.04d\n",Q,a[s.size()-1][gcj.size()-1]);
    }
}
