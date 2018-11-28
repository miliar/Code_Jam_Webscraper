#include <iostream>

using namespace std;

char a[100][100];
int r,c;
void init()
{
    cin>>r>>c;
    for(int i=0;i<r;i++)
    {
        cin>>a[i];
    }

}
bool hefa(int i,int j)
{
    if(i>=r||j>=c)return false;
    if(a[i][j]!='#')return false;
    return true;
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
void print()
{
    for(int i=0;i<r;i++)
    cout<<a[i]<<endl;
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out","w",stdout);
    int t;
    cin>>t;
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
