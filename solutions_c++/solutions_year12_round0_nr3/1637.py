#include <stdio.h>
#include <iostream>
#include <cstring>
#include <string>
#include <map>
#include <stdlib.h>

using namespace std;

int t;
char test[10];
int aa,bb,v_test,status[10];

bool isexist(int* array, int v,int length)
{
    for(int i=0;i<=length;++i)
    {
        if(array[i]==v)
            return true;
    }
    return false;
}

int count()
{
    char tmp[10];
    memset(status,-1,sizeof(status));

    strcpy(tmp,test);

    int ans=0,l=strlen(test),loc=0;

    for(int i=1;i<l;++i)
    {
        char last=tmp[l-1];
        for(int j=l-1;j;--j)
            tmp[j]=tmp[j-1];
        tmp[0]=last;
        int v=atoi(tmp);
        if(v>v_test && v<=bb &&! isexist(status,v,loc))
        {
            ans++;
            status[++loc]=v;
        }
    }
    return ans;
}

int solve()
{
    int ans=0;
    for(int i=aa;i<bb;++i)
    {
        v_test=i;
        itoa(i,test,10);
        ans+=count();
    }
    return ans;
}

int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    freopen("C-large.in","r",stdin);
    //freopen("t.txt","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
    freopen("C-large.out","w",stdout);

    scanf("%d",&t);

    for(int i=1;i<=t;++i)
    {
        printf("Case #%d: ",i);
        scanf("%d%d",&aa,&bb);
        printf("%d\n",solve());
    }
}
