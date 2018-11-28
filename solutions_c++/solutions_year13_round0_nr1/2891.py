#include<iostream>
#include<cstdio>
using namespace std;
int n;char c[5][5];
int hang(int x)
{
    char ch=' ';int f=1;
    for(int i=0;i<=3;++i)
        if(c[x][i]!='T')
        {
            if(ch==' ') ch=c[x][i];
            else if(ch!=c[x][i]) {f=0;break;}
        }
    if(f)
    {
        if(ch=='X') return 1;
        else if(ch=='O') return 2;
    }
    return 0;
}
int lie(int x)
{
    char ch=' ';int f=1;
    for(int i=0;i<=3;++i)
        if(c[i][x]!='T')
        {
            if(ch==' ') ch=c[i][x];
            else if(ch!=c[i][x]) {f=0;break;}
        }
    if(f)
    {
        if(ch=='X') return 1;
        else if(ch=='O') return 2;
    }
    return 0;
}
int duijiao1()
{
    char ch=' ';int f=1;
    for(int i=0;i<=3;++i)
        if(c[i][i]!='T')
        {
            if(ch==' ') ch=c[i][i];
            else if(ch!=c[i][i]) {f=0;break;}
        }
    if(f)
    {
        if(ch=='X') return 1;
        else if(ch=='O') return 2;
    }
    return 0;
}
int duijiao2()
{
    char ch=' ';int f=1;
    for(int i=0;i<=3;++i)
        if(c[i][3-i]!='T')
        {
            if(ch==' ') ch=c[i][3-i];
            else if(ch!=c[i][3-i]) {f=0;break;}
        }
    if(f)
    {
        if(ch=='X') return 1;
        else if(ch=='O') return 2;
    }
    return 0;
}
bool youdian()
{
    int f=0;
    for(int i=0;i<=3;++i)
        for(int j=0;j<=3;++j)
            if(c[i][j]=='.') {f=1;break;}
    if(f) return true;
    return false;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.txt","w",stdout);
    cin>>n;int x,y;
    for(int i=1;i<=n;i++)
    {
        cout<<"Case #"<<i<<": ";
        x=0;y=0;
        for(int j=0;j<=3;++j) scanf("%s",c[j]);
        for(int i=0;i<=3;++i) {int tt=hang(i);if(tt==1) x=1; else if(tt==2) y=1;}
        for(int i=0;i<=3;++i) {int tt=lie(i);if(tt==1) x=1; else if(tt==2) y=1;}
        int tt=duijiao1();if(tt==1) x=1; else if(tt==2) y=1;
        tt=duijiao2();if(tt==1) x=1; else if(tt==2) y=1;
        if(x) cout<<"X won"<<endl;
        else if(y) cout<<"O won"<<endl;
        else if(x==0&&y==0)
        {
            if(youdian()) cout<<"Game has not completed"<<endl;
            else cout<<"Draw"<<endl;
        }
    }
    return 0;
}
