#include <iostream>
#include <cstdio>
#include <cstdlib>
using namespace std;
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define F(i,a) FOR(i,0,a)
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("output-large.out","w",stdout);
    int t;
    char a[4][4];
    cin>>t;
    F(z,t)
    {
        int cg=0,cx,co;
        char r='D';
        bool draw=false;
        F(i,4) F(j,4) cin>>a[i][j];
        //F(i,4){F(j,4) cout<<a[i][j]; cout<<endl;}
        F(i,4)
        {
            cx=0; co=0;
            F(j,4)
            {
                if(a[i][j]!='.')
                {
                    cg++;
                    if(a[i][j]=='X') cx++;
                    else if(a[i][j]=='O') co++;
                    else if(a[i][j]=='T'){cx++; co++;}
                }
            }
            if(cx==4){r='X'; break;}
            if(co==4){r='O'; break;}
        }

        if(r=='D')
        {
            F(i,4)
            {
                cx=0; co=0;
                F(j,4)
                {
                    if(a[j][i]!='.')
                    {
                        if(a[j][i]=='X') cx++;
                        else if(a[j][i]=='O') co++;
                        else if(a[j][i]=='T'){cx++; co++;}
                    }
                }
                if(cx==4){r='X'; break;}
                if(co==4){r='O'; break;}
            }
        }

        if(r=='D')
        {
            cx=0; co=0;
            F(i,4)
            {
                F(j,4)
                {
                    if(a[i][j]!='.' && (i+j)==3)
                    {
                        if(a[i][j]=='X') cx++;
                        else if(a[i][j]=='O') co++;
                        else if(a[i][j]=='T'){cx++; co++;}
                    }
                }
                if(cx==4){r='X'; break;}
                if(co==4){r='O'; break;}
            }
        }

        if(r=='D')
        {
            cx=0; co=0;
            F(i,4)
            {
                F(j,4)
                {
                    if(a[i][j]!='.' && i==j)
                    {
                        if(a[i][j]=='X') cx++;
                        else if(a[i][j]=='O') co++;
                        else if(a[i][j]=='T'){cx++; co++;}
                    }
                }
                if(cx==4){r='X'; break;}
                if(co==4){r='O'; break;}
            }
        }
        if(r=='X') cout<<"Case #"<<z+1<<": X won"<<endl;
        else if(r=='O') cout<<"Case #"<<z+1<<": O won"<<endl;
        else if(cg==16) cout<<"Case #"<<z+1<<": Draw"<<endl;
        else cout<<"Case #"<<z+1<<": Game has not completed"<<endl;
    }
}
