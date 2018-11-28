#include<cstdlib>
#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>
#include<algorithm>
#include<set>
#include<map>
#include<list>
#include<queue>
#include<vector>
#define LL long long
#define inf 0x7fffffff
#define E 1e-9
#define M 100
#define N 5
using namespace std;
int m,n,t;
char ma[N][N];
int al[200];
int dx[4]= {-1,0,1,0};
int dy[4]= {0,1,0,-1};
int flag;
int ok()
{
    for (int i=0; i<n; ++i )
    {
        memset(al,0,sizeof(al));
        for(int j=0; j<n; ++j)
            {
                al[ma[i][j]]++;
            }
        if(al['X']+al['T']==4)return 1;
        if(al['O']+al['T']==4)return 2;
        if(al['.'])flag=1;
    }
//    cout<<"flag="<<flag<<endl;

    for (int i=0; i<n; ++i )
    {
        memset(al,0,sizeof(al));
        for(int j=0; j<n; ++j)
            al[ma[j][i]]++;
        if(al['X']+al['T']==4)return 1;
        if(al['O']+al['T']==4)return 2;
    }
//    cout<<"flag="<<flag<<endl;
    int x=0,y=0;
    memset(al,0,sizeof(al));
    for (int i=0; i<n; ++i )
    {
        al[ma[x][y]]++;
        x+=1;
        y+=1;
    }
    if(al['X']+al['T']==4)return 1;
    if(al['O']+al['T']==4)return 2;
//    cout<<"flag="<<flag<<endl;
    x=0,y=3;
        memset(al,0,sizeof(al));
    for (int i=0; i<n; ++i )
    {
        al[ma[x][y]]++;
        x+=1;
        y-=1;
    }
    if(al['X']+al['T']==4)return 1;
    if(al['O']+al['T']==4)return 2;
    return 0;
}
int main()
{
#ifndef ONLINE_JUDGE
    freopen("ex.in","r",stdin);
    freopen("ex.out","w",stdout);
#endif
    scanf("%d%*c",&t);
    int ncase=0;
    while(t--)
    {
        n=4;
        for (int i=0; i<n; ++i )
                {
                    gets(ma[i]);
                }
        scanf("%*c");
        flag=0;
        int ans=ok();
        printf("Case #%d: ",++ncase);
        if(ans==1)
        printf("X won\n");
        else if(ans==2)
        printf("O won\n");
        else if(flag==1)
        printf("Game has not completed\n");
        else
        printf("Draw\n");

    }
    return 0;
}
