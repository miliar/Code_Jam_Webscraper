#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<ctime>
#include<iostream>
#include<list>
#include<string>
#include<vector>
#include<map>
#include<set>
#include<iterator>
#include<algorithm>
#include<stack>
#include<queue>
using namespace std;

char a[4][4];
int win(int i,int j)
{
    int r=1;
    while(i+r<4 || i-r>=0)
    {
        if(i+r<4&&a[i+r][j]!=a[i][j]&&a[i+r][j]!='T')
            break;
        if(i-r>=0&&a[i-r][j]!=a[i][j]&&a[i-r][j]!='T')
            break;
        r++;
    }
    if(i+r>=4&&i-r<0)
        return 1;
    int c=1;
    while(j+c<4 || j-c>=0)
    {
        if(j+c<4&&a[i][j+c]!=a[i][j]&&a[i][j+c]!='T')
            break;
        if(j-c>=0&&a[i][j-c]!=a[i][j]&&a[i][j-c]!='T')
            break;
        c++;
    }
    if(j+c>=4&&j-c<0)
        return 1;
    if(i==j)
    {
        r=1,c=1;
        while(i+r<4&&j+c<4 || i-r>=0&&j-c>=0)
        {
            if(i+r<4&&j+c<4&&a[i+r][j+c]!=a[i][j]&&a[i+r][j+c]!='T')
                break;
            if(i-r>=0&&j-c>=0&&a[i-r][j-c]!=a[i][j]&&a[i-r][j-c]!='T')
                break;
            r++;c++;
        }
        if((i+r>=4||j+c>=4) && (i-r<0||j-c<0))
            return 1;
    }
    if(i+j==3)
    {
        r=1,c=1;
        while(i-r>=0&&j+c<4 || i+r<4&&j-c>=0)
        {
            if(i-r>=0&&j+c<4&&a[i-r][j+c]!=a[i][j]&&a[i-r][j+c]!='T')
                break;
            if(i+r<4&&j-c>=0&&a[i+r][j-c]!=a[i][j]&&a[i+r][j-c]!='T')
                break;
            r++;c++;
        }
        if((i-r<0||j+c>=4) && (i+r>=4||j-c<0))
            return 1;
    }
    return 0;
}
char judge()
{
    int i,j,dot=0;
    for(i=0;i<4;i++)
        for(j=0;j<4;j++)
        {
            if(win(i,j))
                return a[i][j];
            if(a[i][j]=='.')
                dot++;
        }
    if(dot==0)
        return 'D';
    return 'G';
}
int main()
{
    int t,cas=1;;
    cin>>t;
    while(t--)
    {
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                cin>>a[i][j];
        cout << "Case #" << cas++ <<": ";
        char ans=judge();
        if(ans=='O')
            cout<<"O won"<<endl;
        else if(ans=='X')
            cout<<"X won"<<endl;
        else if(ans=='D')
            cout<<"Draw"<<endl;
        else
            cout<<"Game has not completed"<<endl;;

    }
    return 0;
}
