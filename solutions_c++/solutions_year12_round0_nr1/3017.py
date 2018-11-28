#include<cstdio>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<cstring>
#include<string>

using namespace std;
char s[111];
int main()
{
    int t,T,n,i,j;
    freopen("A-small-attempt0.in","r",stdin);
   freopen("output.txt","w",stdout);   
    char a[]="yhesocvxduiglbkrztnwjpfmaq";
    scanf("%d ",&T);
    for(t=1;t<=T;t++)
    {
        gets(s);
        for(i=0;s[i];i++)
            if(s[i]!=' ')
            s[i]=a[s[i]-'a'];
        printf("Case #%d: %s\n",t,s);
    }
//system("pause");
    return 0;
}
