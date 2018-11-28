#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;

int ok(int a,int b)
{
    char sa[11],sb[11];
    sprintf(sa,"%d",a);
    sprintf(sb,"%d",b);
    string s1(sa),s2(sb);
    if(s1.size()!=s2.size()) return 0;
    for(int i=1;i<s1.size();i++){
        if(s1[i]!='0'&&s2==s1.substr(i) + s1.substr(0,i))
            return 1;
    }
    return 0;
}

int main()
{
    int t,T,a,b,i,j;
    freopen("C-small-attempt0.in","r",stdin);
    freopen("output.txt","w",stdout);   
    scanf("%d",&T);
    for(t=1;t<=T;t++)
    {
        scanf("%d%d",&a,&b);
        int ans=0;
        for(i=a;i<=b;i++)
            for(j=i+1;j<=b;j++)
            {
                if(ok(i,j)) ans++;                   
            }
        printf("Case #%d: %d\n",t,ans);
    }
//system("pause");
    return 0;
}
