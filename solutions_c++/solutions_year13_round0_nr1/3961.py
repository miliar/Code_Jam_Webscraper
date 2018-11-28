#include<iostream>
#include<cstdio>
using namespace std;

#define getcx getchar//getchar_unlocked
inline void s( char &n )
{
    n=0;
    int ch=getcx();
    if(ch=='\n')
    ch=getcx();
    n=ch;
}

int isEqual(char a[4],char c)
{
    int flag=1;
    for(int i=0;i<4;i++)
    {
        if(!(a[i]==c||a[i]=='T'))
        {
            flag=0;
            break;
        }
    }
   // cout<<flag<<endl;

    return flag;
}

int check(char a[4][4],char c)
{
    for(int i=0;i<4;i++)
    {
        if(isEqual(a[i],c))
        return 1;
    }
    for(int i=0;i<4;i++)
    {
        char b[4]={a[0][i],a[1][i],a[2][i],a[3][i]};
        if(isEqual(b,c))
        return 1;

    }
    char b[4]={a[0][0],a[1][1],a[2][2],a[3][3]};

    if(isEqual(b,c))
        return 1;

    char d[4]={a[0][3],a[1][2],a[2][1],a[3][0]};
    if(isEqual(d,c))
        return 1;

    return 0;
}

void isEmpty(char a[4][4],bool &empty)
{
    for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        if(a[i][j]=='.')
        {
            empty=true;
            return;
        }

}
int main()
{
    freopen("A-large.in","r", stdin);
    freopen("output.in","w", stdout);
    int t;
    cin>>t;
    int c=t;
    while(t--)
    {
        char a[4][4];
        for(int i=0;i<4;i++)
        for(int j=0;j<4;j++)
        s(a[i][j]);
        getchar();

        bool empty_cell=false;
        int p1=check(a,'X');
        int p2=check(a,'O');

        cout<<"Case #"<<c-t<<": ";

        if(p1>p2)
        {
            cout<<"X won"<<endl;
            continue;
        }
        if(p1<p2)
        {
            cout<<"O won"<<endl;
            continue;
        }
        isEmpty(a,empty_cell);
        if(p1==p2&&empty_cell==false)
        {
            cout<<"Draw"<<endl;
            continue;
        }
        if(p1==p2&&empty_cell==true)
        {
            cout<<"Game has not completed"<<endl;
            continue;
        }
    }
}
