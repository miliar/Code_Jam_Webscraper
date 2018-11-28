#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const double pi=acos(-1.0);
const int L=1001;
const double eps=1e-6;
char str[]={"yhesocvxduiglbkrztnwjpfmaq"};
int main()
{
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    char s[L];
    int i,j=1,t;
    scanf("%d",&t);
    getchar();
    while(t--)
    {
        gets(s);
        //cout<<s<<endl;
        int n=strlen(s);
        printf("Case #%d: ",j++);
        for(i=0;i<n;i++)
        {
            if(s[i]<='z' && s[i]>='a')
            {

                printf("%c",str[s[i]-'a']);
            }
            else printf("%c",s[i]);
        }
        cout<<endl;
    }
    return 0;
}
/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
*/
