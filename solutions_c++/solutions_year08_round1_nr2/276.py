#include <stdio.h>
#include <vector>
#include <iostream>
#include <algorithm>
#define dos pair<int,int>
#define a first
#define b second
using namespace std;

int n,m;
vector<dos>ma[101];
int v[20];
int fin[20];
int maxi;

void re(int pos)
{
    if(pos<n)
    {
        v[pos]=0;
        re(pos+1);
        v[pos]=1;
        re(pos+1);
    }else
    {
        int cont;
        for(int i=0;i<m;i++)
        {
            cont=0;
            for(int k=0;k<ma[i].size();k++)
            {
                if(v[ma[i][k].a-1]!=ma[i][k].b)
                {
                    cont++; 
                }
                else
                    break;
            }
            if(cont==ma[i].size())
            {
                return;
            }
        }
        cont=0;
        for(int i=0;i<n;i++)
        {
            if(v[i])
                cont++;
        }
        if(maxi>=cont)
        {
            maxi=cont;
            for(int i=0;i<n;i++)
                fin[i]=v[i];
        }
    }
}

int main()
{
    freopen("input.txt","r",stdin);
    freopen("output.txt","w",stdout);
    int N;
    scanf("%d",&N);
    for(int I=0;I<N;I++)
    {
        int t;
        int a,b;
        dos c;
        scanf("%d%d",&n,&m);
        for(int i=0;i<m;i++)
        {
            ma[i].clear();
            scanf("%d",&t);
            for(int k=0;k<t;k++)
            {
                scanf("%d%d",&a,&b);
                c.a=a; c.b=b;
                ma[i].push_back(c);
            }
        }
        maxi=100;
        re(0);
        printf("Case #%d: ",I+1);
        if(maxi!=100)
        {
            for(int i=0;i<n;i++)
                printf("%d ",fin[i]);
        }
        else
            printf("IMPOSSIBLE");
        printf("\n");
    }
}
