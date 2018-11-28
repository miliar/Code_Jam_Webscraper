#include <iostream>

using namespace std;

char linia(string s)
{

    int czy = 0;
    char c = s[0];
    char c1 = 'D';
    if(s[0]=='T')
    {
        s[0] = s[1];
        s[1] = c;
        c = s[0];

    }
    for(int i=0; i<4; i++)
    {
        if(s[0]=='.') c1 = '.';
        if(c!=s[i]&&(c!='T'&&s[i]!='T'))
            return c1;
    }
    //cout << "<<"<< s <<">>" << endl;
    if (c!='T')
        return c;
    else
        return s[1];

}

int main()
{
    int n;
    cin >> n;
    for(int k=0;k<n;k++)
    {
cout << "Case #"<< k+1 << ": ";

        string p[4];
        cin >> p[0];
        cin >> p[1];
        cin >> p[2];
        cin >> p[3];

        char tab[10];
        int l=0;
        char c = 'D';
        string s;
        for(int i=0;i<4;i++)
        {
            s= "";
           s += p[i][0];
           s += p[i][1];
           s += p[i][2];
           s += p[i][3];
           c=linia(s);
           tab[l++]=c;
           if(c!='D'&&c!='.') break;

            s= "";
           s += p[0][i];
           s += p[1][i];
           s += p[2][i];
           s += p[3][i];
           c=linia(s);
           tab[l++]=c;
           if(c!='D'&&c!='.') break;

        }
        if(c=='D'||c=='.')
        {s= "";
           s += p[0][0];
           s += p[1][1];
           s += p[2][2];
           s += p[3][3];
           c=linia(s);
           tab[l++]=c;
        }
        if(c=='D'||c=='.')
        {
            s= "";
           s += p[0][3];
           s += p[1][2];
           s += p[2][1];
           s += p[3][0];
           c=linia(s);
           tab[l++]=c;
        }
        if(c == 'X')
        {
            cout << "X won" << endl;
            continue;
        }
        if(c == 'O')
        {
            cout << "O won" << endl;
            continue;
        }
        int z = 0;
        for(int i=0;i<10;i++)
            if(tab[i]=='.')
            {
                 cout << "Game has not completed" << endl;
                 z = 1;
                 break;
            }
        if(z==1) continue;
        cout << "Draw" << endl;

    }
    return 0;
}
