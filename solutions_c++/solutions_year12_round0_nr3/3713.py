/*
TASK: Recycled Numbers
LANG: C++
*/
#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<math.h>
#include<algorithm>
#include<map>
#include<set>
#include<list>
#include<queue>
#include<iostream>
using namespace std;
#define X first
#define Y second
int N,M,T;
char str[15];
set<pair<int,int> > s;
pair<int,int> pr;
int main()
{
    freopen("C-large.in","r",stdin);
    freopen("xxx.out","w",stdout);
    int i,j,k;
    scanf("%d",&T);
    int x,y,z,ii=0;
    int a,b,c;
    while(T--)
    {
        scanf("%d%d",&x,&y);
        z=0;
        sprintf(str,"%d",x);
        k=strlen(str);
        for(i=x;i<=y;i++)
        {
            N=i;    M=0;    c=10;
            for(j=1;j<k;j++)
            {
                M=i%c;
                N/=10;
                c*=10;
                sprintf(str,"%d%d",M,N);
                sscanf(str,"%d",&b);
                pr.X=i; pr.Y=b;
                if(x<=b && b<=y && i<b && s.find(pr)==s.end())
                {
                    s.insert(pr);
                    z++;
                }
            }
        }
        s.clear();
        ii++;
        printf("Case #%d: %d\n",ii,z);
    }
}
