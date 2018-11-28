#include <iostream>
#include <cstdio>
#include <algorithm>
#include <cmath>
#include <algorithm>
using namespace std;

int r,c;
char a[100][100];
void print()
{
    for(int i=0;i<r;i++)
    printf("%s\n",a[i]);
}
bool hefa(int i,int j)
{
    if(i>=r||j>=c)return false;
    if(a[i][j]!='#')return false;
    return true;
}
int init()
{
    scanf("%d%d",&r,&c);
    for(int i=0;i<r;i++)
    scanf("%s",a[i]);
    return 0;
}
bool get()
{
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            if(a[i][j]=='#')
            {
                a[i][j]='/';
                if(!hefa(i+1,j))
                return false;
                else a[i+1][j]='\\';

                if(!hefa(i,j+1))
                return false;
                else a[i][j+1]='\\';

                if(!hefa(i+1,j+1))
                return false;
                else a[i+1][j+1]='/';
            }
        }
    }
    return true;
}
int main()
{
    freopen("data.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    for(int i=1;i<=t;i++)
    {
        cout<<"Case #"<<i<<":"<<endl;
        init();
        if(!get())
        {
            cout<<"Impossible"<<endl;
        }
       else print();
    }
    return 0;
}
