#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <algorithm>
using namespace std;
const double pi=acos(-1.0);
const int L=30000;
const double eps=1e-6;
char str[L];
bool hash[L];
char s[]={"0123456789"};
int fic(int a)
{
    int q=0,i=a,k=0,p,u=a,ans=0;
    while(i>=10)
    {
        str[q++]=s[i%10];
        i/=10;
    }
    str[q++]=s[i];
    char ss[L];
    for(i=0;i<q;i++)
        ss[i]=str[q-i-1];
    strcpy(str,ss);
    k=0;
    bool op=0;
    while(1)
    {
        //cout<<k<<endl;

        p=0;
        for(i=k;i<q+k;i++)
            ss[p++]=str[i%q];
        ss[p]='\0';
        //cout<<k<<' '<<"gfdgdfg   "<<ss<<endl;
        a=0;
        for(i=0;i<p;i++)
            a+=(int)((ss[i]-'0')*pow(10.0,(double)(p-i-1)));

        if(hash[a] && u!=a) {

        //cout<<u<<' '<<a<<endl;
        ans++;}
        if(k>=q-1) break;
        k++;
    }
    return ans;
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);

    int i,j=1,t,a,b,ans;
    scanf("%d",&t);
    while(t--)
    {
        ans=0;
        scanf("%d %d",&a,&b);
        memset(hash,0,sizeof(hash));
        for(i=a;i<=b;i++)
            hash[i]=true;
        for(i=a;i<=b;i++)
        {
            {
                ans+=fic(i);
            }
        }
        printf("Case #%d: %d\n",j++,ans/2);
    }

    return 0;
}
/*
3
ejp mysljylc kd kxveddknmc re jsicpdrysi
rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd
de kr kd eoya kw aej tysr re ujdr lkgc jv
*/
