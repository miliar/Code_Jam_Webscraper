#include <iostream>
#include <fstream>
#include <vector>
#include <stdio.h>
using namespace std;
void scan (vector<vector<char> > &v, ifstream &cin)
{
    for (int i=0;i<4;++i)
    {
        for (int j=0;j<4;++j)
        {
            cin>>v[i][j];
        }
    }
}
bool won (vector<vector<char> > &v, char c, bool &emp)
{
    for (int i=0;i<4;++i)
    {
        bool b=1, z=1;
        for (int j=0;j<4;++j)
        {
            if (v[i][j]=='.')
            {
                emp=1;
            }
            if (v[i][j]!=c && v[i][j]!='T')
            {
                b=0;
            }
            if (v[j][i]!=c && v[j][i]!='T')
            {
                z=0;
            }
        }
        if (b || z)
        {
            return 1;
        }
    }
    bool b=1, z=1;
    for (int i=0;i<4;++i)
    {
        if (v[i][i]!=c && v[i][i]!='T')
        {
            b=0;
        }
        if (v[i][3-i]!=c && v[i][3-i]!='T')
        {
            z=0;
        }
    }
    return (b || z);
}
string solve (ifstream &cin)
{
    vector<vector<char> > v(4, vector<char>(4));
    scan(v, cin);
    bool emp = 0;
    if (won(v, 'O', emp))
    {
        return "O won";
    }
    if (won(v, 'X', emp))
    {
        return "X won";
    }
    if (emp)
    {
        return "Game has not completed";
    }
    return "Draw";
}
int main()
{
    ifstream cin ("a.txt");
    ofstream cout("b.txt");
    int t;
    cin>>t;
    for (int i=0;i<t;++i)
    {
        cout<<"Case #"<<i+1<<": "<<solve(cin)<<endl;
    }
    return 0;
}
