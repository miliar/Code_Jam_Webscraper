#include<iostream>
#include<string.h>
#include<string>
#include<string.h>
#include<map>
#include<stdio.h>
#include<queue>

using namespace std;

int A,B;
int ans;
int a[8];
void findsum(int k,int n)
{
    for(int i=1;i<n;++i)
    {
        int w=(k%a[i]*a[n-i]+(k/a[i]));
        if(w<=B&&w>=A&&w!=k)
        ans++;
    }
}
int main()
{
    freopen("C-small-attempt0.in","r",stdin);
    freopen("C-small-attempt0.out","w",stdout);
    a[0]=1;
    for(int i=1;i<8;++i)
    {
        a[i]=a[i-1]*10;
    }
    string stemp1,stemp2;
    int T;
    cin>>T;
    for(int l=1;l<=T;++l)
    {
        cin>>stemp1>>stemp2;
        int n=stemp1.size();
        A=B=0;
        for(int i=0;i<n;++i)
        {
            A=(A*10)+stemp1[i]-'0';
            B=(B*10)+stemp2[i]-'0';
        }
        if(n<2)
        {
            printf("Case #%d: 0\n",l);
            continue;
        }
        ans=0;
        for(int i=A;i<=B;++i)
        {
            findsum(i,n);

        }
        printf("Case #%d: %d\n",l,ans/2);
    }
    return 0;
}
