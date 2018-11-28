#include <iostream>
#include <cstdio>
#include <cstring>
#include <map>
#include <algorithm>
using namespace std;
int s[550];
bool bool1[550],bool2[550];
void print(bool b1[],bool b2[],int n)
{
    int j=0;
    while (j<n)
    {
        if(b1[j] && !b2[j])
        {
            printf("%d",s[j]);
            break;
        }
        j++;
    }
    j++;
    while (j<n)
    {
        if(b1[j] && !b2[j])
            printf(" %d",s[j]);
        j++;
    }
    printf("\n");
}
int main()
{
    //freopen("C-small-attempt0.in","r",stdin);
    //freopen("C-small-attempt0.out","w",stdout);
    int n,Cas;
    scanf("%d",&Cas);
    for (int cas=1; cas<=Cas; cas++)
    {
        map<int,int> m;
        m.clear();
        scanf("%d",&n);
        for(int i=0; i<n; i++)
            scanf("%d",&s[i]);
        int num=1<<n;
        for(int i=1; i<=num; i++)
        {
            int sum=0;
            for(int j=0; j<n; j++)
                if((1<<j)&(i-1))
                    sum+=s[j];
            if(m[sum]==0)
            {
                m[sum]=i;
                memset(bool1,0,sizeof(bool1));
                memset(bool2,0,sizeof(bool2));
                for(int j=0; j<n; j++)
                    if((1<<j) & (i-1))
                        bool1[j]=1;
                for(int j=0; j<n; j++)
                    if((1<<j) & (m[sum]-1))
                        bool2[j]=1;
                printf("Case #%d:\n",cas);

                print(bool1,bool2,n);
                print(bool2,bool1,n);
                break;
            }
            m[sum]=i;
        }
    }
    return 0;
}
