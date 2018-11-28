#include<stdio.h>
#include<string.h>
#include<string>
#include<math.h>
#include<algorithm>
#include<iostream>
#include<vector>
#include<stack>
#include<queue>
#include<map>
#include<set>
#define vvi vector<vector<int> >
#define pii pair<int,int>
#define vpii vector< vector<pair<int,int> > >
#define mp(a,b) make_pair(a,b)
#define ll long long
#define vi vector<int>
#define vs vector<string>
#define sz size()
#define pb push_back
#define all(x) x.begin(),x.end()
#define MAX(a,b) (a>b?a:b)
#define MIN(a,b) (a<b?a:b)
#define ABS(a) (a<0?-1*(a):a)
#define pi 2 * acos (0.0)


using namespace std;
bool f;
char g[10][10];
int c1,c2,c3,ans;
void check()
{
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
            if(g[i][j]=='.'){    f=true;return;}
}
void c_check(int x,int y)
{
    if(g[x][y]=='O')    c1++;
    else if(g[x][y]=='X')   c2++;
    else if(g[x][y]=='T')   c3++;
}
bool check_res()
{
    if((c1==3&&c3==1)|| (c1==4))    return ans=1;
    else if((c2==3&&c3==1)||(c2==4))   return  ans=2;
    return ans;
}

void fun()
{
    int i,j,k;
    if(g[0][0]!='.')
    {
        c1=c2=c3=0;
        for(i=0;i<4;i++)    c_check(i,i);
        if(check_res())     return;
    }
    if(g[0][3]!='.')
    {
        c1=c2=c3=0;
        for(i=0,j=3;i<4;i++,j--)    c_check(i,j);
        if(check_res())     return;
    }
    for(i=0,j=0;i<4;i++)
    {
        if(g[i][j]!='.')
        {
            c1=c2=c3=0;
            for(k=0;k<4;k++)    c_check(i,k);
            if(check_res()) return;
        }
    }
    for(i=0,j=0;i<4;i++)
    {
        if(g[j][i]!='.')
        {
            c1=c2=c3=0;
            for(k=0;k<4;k++)    c_check(k,i);
            if(check_res()) return;
        }
    }

}
int main()
{
    int tcase,i,co=1;
    char str[100];
    scanf("%d",&tcase);
    gets(str);
    freopen("out.txt","w",stdout);
    while(tcase--)
    {
        memset(g,0,sizeof(g));
        for(i=0;i<4;i++)
            gets(g[i]);
        gets(str);
        f=false;
        check();
        ans=0;
        fun();
        printf("Case #%d: ",co++);
        if(ans)
        {
            if(ans==1)
                printf("O won\n");
            else
                printf("X won\n");
        }
        else if(f)  printf("Game has not completed\n");
        else printf("Draw\n");

    }
    return 0;
}

