#include <iostream>
#include <fstream>
#include <string>
#include <algorithm>

using namespace std;
const double eps = 0.00001;
const int n =4;

inline void checker (char** mas, bool &X, bool &O)
{
    X = false; O = false;
    for (int i=0;i<n;++i)
        for (int j=1;j<n;++j)
        {
            if (mas[i][j]!=mas[i][j-1] || mas[i][j]=='.')
                break;
            else if (j==n-1)
            {
                if (mas[i][j]=='X')
                    X = true;
                else
                    O = true;
                return;
            }
        }
    for (int j=0;j<n;++j)
        for (int i=1;i<n;++i)
        {
            if (mas[i][j]!=mas[i-1][j] || mas[i-1][j]=='.')
                break;
            else if (i==n-1)
            {
                if (mas[i][j]=='X')
                    X = true;
                else
                    O = true;
                return;
            }
        }
    for (int i=1;i<n;++i)
    {
        if ((mas[i-1][i-1]!=mas[i][i]) || (mas[i][i]=='.'))
            break;
        else if (i==n-1)
        {
                 if (mas[i][i]=='X')
                 X=true;
                 else
                 O=true;
                     return;
        }
    }
    for (int i=n-1;i>=1;--i)
    {
        if (mas[n-i-1][i]!=mas[n-i][i-1] || mas[n-i][i-1]=='.')
            break;
        else if (i==1)
        {
            if (mas[n-i-1][i]=='X')
                X=true;
                    else
                    O=true;
                    return;}
        }
    }


int main()
{
    ifstream cin ("/home/misha/A-large.in");
    ofstream cout ("/home/misha/aaa");
    cin.sync_with_stdio (false);
    cout.sync_with_stdio(false);
    string s;
    int t;
    char **mas = new char *[n], **mas2 = new char *[n];
    for (int i=0;i<n;++i)
        mas[i] = new char [n];
    for (int i=0;i<n;++i)
        mas2[i] = new char [n];
    cin>>t;

    for (int j=0;j<t;++j)
    {
        bool X=false, O=false, CON=false;
        for (int i=0;i<n;++i)
            for (int j=0;j<n;++j)
            {
                cin>>mas[i][j];
                mas2[i][j] = mas[i][j];
                if (mas[i][j]=='T')
                {
                    mas[i][j]='X';
                    mas2[i][j]='O';
                }
                if (mas[i][j]=='.') CON = true;
            }
        cin.get();
        checker(mas,X,O);
        if ((!X) && (!O))
            checker(mas2,X,O);
        cout<<"Case #"<<j+1<<": ";
        if (X) cout<<"X won"<<endl;
        else if (O) cout<<"O won"<<endl;
        else if (CON) cout<<"Game has not completed"<<endl;
        else cout<<"Draw"<<endl;
    }
    return 0;
}

