#include <cstdlib>
#include <iostream>
#include <string>
#include <cstring>
#include <algorithm>

#define N

using namespace std;

int main(int argc, char *argv[])
{
    int t;
    int i,j,k;
    int o,x;
    
    bool end;
    char win;
    string s[10];
    
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "w+t", stdout);
    
    cin>>t;
    for(i=1;i<=t;i++)
    {
        win='.';
        for(j=0;j<4;j++)
        {
            cin>>s[j];
        }
        for(j=0,end=true;j<4;j++)
        {
            for(k=0,o=0,x=0;k<4;k++)
            {
                switch(s[j][k])
                {
                    case '.' :
                        end=false;
                        break;
                    case 'O' :
                        o++;
                        break;
                    case 'X' :
                        x++;
                        break;
                    case 'T' :
                        o++;
                        x++;
                        break;
                }
            }
            if(o==4)
            {
                win='O';
                break;
            }
            if(x==4)
            {
                win='X';
                break;
            }
            for(k=0,o=0,x=0;k<4;k++)
            {
                switch(s[k][j])
                {
                    case 'O' :
                        o++;
                        break;
                    case 'X' :
                        x++;
                        break;
                    case 'T' :
                        o++;
                        x++;
                        break;
                }
            }
            if(o==4)
            {
                win='O';
                break;
            }
            if(x==4)
            {
                win='X';
                break;
            }
        }
        if(win=='.')
        {
            for(j=0,o=0,x=0;j<4;j++)
            {
                switch(s[j][j])
                {
                    case 'O' :
                        o++;
                        break;
                    case 'X' :
                        x++;
                        break;
                    case 'T' :
                        o++;
                        x++;
                        break;
                }
            }
            if(o==4)
            {
                win='O';
            }
            if(x==4)
            {
                win='X';
            }
        }
        if(win=='.')
        {
            for(j=0,o=0,x=0;j<4;j++)
            {
                switch(s[j][3-j])
                {
                    case 'O' :
                        o++;
                        break;
                    case 'X' :
                        x++;
                        break;
                    case 'T' :
                        o++;
                        x++;
                        break;
                }
            }
            if(o==4)
            {
                win='O';
            }
            if(x==4)
            {
                win='X';
            }
        }
        cout<<"Case #"<<i<<": ";
        if(win=='.')
        {
            if(end==true)
                cout<<"Draw"<<endl;
            else
                cout<<"Game has not completed"<<endl;
        }
        else
        {
            cout<<win<<" won"<<endl;
        }
    }
    
    //system("PAUSE");
    return EXIT_SUCCESS;
}
