#include<iostream>
#include<sstream>
#include<cstdio>
#include<cstring>
#include<string>
#include<vector>
#include<map>
#include<algorithm>

#define N 100009
#define ll long long

using namespace std;

char s[10][10];
int check(int x,int y,int dx,int dy)
{
    char c=0;
    for(int i=0;i<4;i++)
        if(s[x+i*dx][y+i*dy]=='X'||s[x+i*dx][y+i*dy]=='O')
        {
            c=s[x+i*dx][y+i*dy];
            break;
        }
    if(c==0) return 0;
    for(int i=1;i<4;i++)
        if(s[x+i*dx][y+i*dy]!='T'&&s[x+i*dx][y+i*dy]!=c)
                return 0;

    if(c=='O') return 1;
    if(c=='X') return 2;
    return 0;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int T,cas=0;
    cin>>T;
    while(T--)
    {
        for(int i=0;i<4;i++) cin>>s[i];
        int cnt=0,X=0,O=0;
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(s[i][j]=='.')
                    cnt++;
        int res=0,t;
        for(int i=0;i<4;i++)
        {
            if(t=check(i,0,0,1)) res=t;
            if(t=check(0,i,1,0)) res=t;
        }
        if(t=check(0,0,1,1)) res=t;
        if(t=check(3,0,-1,1)) res=t;
        printf("Case #%d: ",++cas);
        if(!res){
            if(cnt) puts("Game has not completed");
            else puts("Draw");
        }
        else if(res==1){
            puts("O won");
        }
        else
            puts("X won");
    }
    fclose(stdout);
    return 0;
}
