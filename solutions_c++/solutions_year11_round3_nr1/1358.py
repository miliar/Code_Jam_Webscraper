#include<iostream>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    int r,c;
    int cc,i,j;
    char in;
    char table[100][100];
    bool judge;
    cin>>t;
    for (cc = 1; cc <= t; cc++)
    {
        cin>>r>>c;
        judge = true;
        for (i = 0; i<r; i++)
        {
                scanf("%s", table[i]);
        }
        
        for (i = 0; i<r; i++)
        {
            for (j = 0; j<c; j++)
            {
                if (table[i][j] == '#' && table[i+1][j] == '#' && 
                   table[i][j+1] == '#' && table[i+1][j+1] == '#')
                {
                    table[i][j] = '/';
                    table[i][j+1] = '\\';
                    table[i+1][j] = '\\';
                    table[i+1][j+1] = '/';
                }
            }
        }
        for (i = 0; i<r; i++)
        {
            for (j = 0; j<c; j++)
            {
                if (table[i][j] == '#')
                   judge = false;
            }
        }
        cout<<"Case #"<<cc<<":"<<endl;
        if (judge)
        {
            for (i = 0; i<r; i++)
            {
                for (j = 0; j<c; j++)
                {
                    cout<<table[i][j];
                }
                cout<<endl;
            }
        }
        else cout<<"Impossible"<<endl;
    }
    return 0;
}
