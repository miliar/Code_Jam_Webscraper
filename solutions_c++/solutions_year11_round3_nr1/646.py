#include <iostream>
#include <stdio.h>

using namespace std;

int r,c;


char inp[53][53];
char tep[53][53];

bool mypos(int x,int y)
{
    if(x==r-1) return false;
    if(y==c-1) return false;
    if(inp[x][y+1]!='#') return false;
    if(inp[x+1][y]!='#') return false;
    if(inp[x+1][y+1]!='#') return false;
    return true;
}



int main()
{
freopen("a.in","r",stdin);
freopen("a.out","w",stdout);

int t,ti=0;
cin>>t;
for(int ti=1;ti<=t;ti++)
{
    cin>>r>>c;
    for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
        {
            cin>>inp[i][j];
            tep[i][j]=inp[i][j];
        }

bool flg=0;
    for(int i=0;i<r;i++)
        for(int j=0;j<c;j++)
    {
        if(tep[i][j]=='#')
        {
          if(mypos(i,j))
          {
              tep[i][j]='/';
              tep[i][j+1]='\\';
              tep[i+1][j]='\\';
              tep[i+1][j+1]='/';

          }
         else {flg=1;break;}
        }

    }

    cout<<"Case #"<<ti<<":\n";
    if(flg==1) cout<<"Impossible\n";
    else
    {
        for(int i=0;i<r;i++)
        {
            for(int j=0;j<c;j++) cout<<tep[i][j];
            cout<<endl;
        }
    }



}
return 0;
}
