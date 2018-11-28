#include<iostream>
#include<string>
#include<cstdio>
using namespace std;
bool check(char t,char a, char b, char c, char d)
{
    return ((a == t or a == 'T') and (b == t or b == 'T') and (c == t or c == 'T') and (d == t or d == 'T'));
}
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int casos,cont = 1;
    string t[4];
    bool X,O,D;
    cin>>casos;
    while(casos--)
    {
        X = false;
        O = false;
        D = false;
        cin>>t[0]>>t[1]>>t[2]>>t[3];
        for(int i=0;i<4;i++)
            for(int j=0;j<4;j++)
                if(t[i][j] == '.')
                    D = true;
        for(int i=0;i<4;i++)
        {
            X = ( X or check('X',t[i][0],t[i][1],t[i][2],t[i][3]));
            O = ( O or check('O',t[i][0],t[i][1],t[i][2],t[i][3]));
            X = ( X or check('X',t[0][i],t[1][i],t[2][i],t[3][i]));
            O = ( O or check('O',t[0][i],t[1][i],t[2][i],t[3][i]));
        }
        X = ( X or check('X',t[0][0],t[1][1],t[2][2],t[3][3]));
        O = ( O or check('O',t[0][0],t[1][1],t[2][2],t[3][3]));
        X = ( X or check('X',t[0][3],t[1][2],t[2][1],t[3][0]));
        O = ( O or check('O',t[0][3],t[1][2],t[2][1],t[3][0]));
        cout<<"Case #"<<cont<<": ";
        if(X or O)
        {
            if(X)
                cout<<"X won"<<endl;
            else
                cout<<"O won"<<endl;
        }
        else if(D)
        {
            cout<<"Game has not completed"<<endl;
        }
        else
        {
            cout<<"Draw"<<endl;
        }
        cont++;
    }
    return 0;
}
