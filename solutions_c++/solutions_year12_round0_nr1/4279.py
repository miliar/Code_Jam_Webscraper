#include <iostream>
#include <fstream>
#include <sstream>
#include <string>

using namespace std;

//string abs="abcdefghijklmnopqrstuvwxyz";
string ans="yhesocvxduiglbkrztnwjpfmaq";

int conv(string x)
{
    int n;
    stringstream ss(x);
    ss >> n;
    return n;
}

int main()
{
    freopen("ss.in", "r", stdin);
    freopen("ss.out", "w", stdout);
    string x;
    getline(cin, x);
    int n=conv(x), i;
    for (i=0; i<n; i++)
    {
        getline(cin, x);
        cout << "Case #" << i+1 << ": ";
        int j, m=x.size();
        for (j=0; j<m; j++)
        {
            char a;
            a=x[j];
            if (a != ' ') a=ans[a-'a'];
            cout << a;
        }
        cout << endl;
    }
}
