/*

This program can successfully run in BORLAND C++ BUILDER 6.
without file input/output in code.
you can run this program like this way(in WINDOWS command prompt):

p3.exe < inputfile.txt > outputfile.txt

And then take the outputfile.txt :)  

*/

#include <iostream>
#include <string>
using namespace std;

int N, Ni, Len;
string s, d = "welcome to code jam";
int opt[510][21];

void init()
{
    s = "";
    do
    {
        getline(cin, s);
    }while(s == "");
    memset(opt, 0, sizeof(opt));
}

void work()
{
    int ans[5];
    int i, j, k;
    int tot = 0;

    Len = s.length();
    for (i = 0; i < Len; i++)
        if (s[i] == d[18])
            opt[i][18] = 1;

    for (i = Len - 2; i >= 0; i--)
        for (j = 17; j >= 0; j--)
            if (s[i] == d[j])
                for (k = i + 1; k < Len; k++)
                    opt[i][j] = (opt[i][j] + opt[k][j + 1]) % 10000;

            
    for (i = 0; i < Len; i++)
        tot = (tot + opt[i][0]) % 10000;

    memset(ans, 0, sizeof(ans));
    for (i = 4; i >= 1; i--)
    {
        ans[i] = tot % 10;
        tot = tot / 10;
    }

    cout << "Case #" << Ni << ": ";
    for (i = 1; i <= 4; i++)
        cout << ans[i];
    cout << endl;
}

int main()
{
    cin >> N;
    for (Ni = 1; Ni <= N; Ni++)
    {
        init();
        work();
    }

    //system("pause");
    return 0;
}
