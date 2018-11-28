/*

This program can successfully run in BORLAND C++ BUILDER 6.
without file input/output in code.
you can run this program like this way(in WINDOWS command prompt):

p1Large.exe < inputfile.txt > outputfile.txt

And then take the outputfile.txt :)  

*/

#include <iostream>
#include <string>
using namespace std;

int L, D, N;
string words[5100];
bool s[20][127];

void init()
{
    int i;
    string str;

    cin >> L >> D >> N;
    cin.ignore();
    for (i = 1; i <= D; i++)
        getline(cin, words[i]);
}

void work()
{
    bool flag;
    int i, j, c, ans;
    char ch;

    for (i = 1; i <= N; i++)
    {
        flag = true;
        memset(s, 0, sizeof(s));
        c = 0;
        while (true)
        {
            cin >> ch;
            if (ch == '(')
                while (true)
                {
                    cin >> ch;
                    if (ch == ')') break;
                    s[c][ch] = true;
                }
            else
                s[c][ch] = true;
            c++;
            if (c == L) break;
        }

        ans = 0;
        for (j = 1; j <= D; j++)
        {
            for (c = 0; c < L; c++)
                if (!s[c][words[j][c]])
                    break;
            if (c == L)
                ans++;
        }
        cout << "Case #" << i << ": " << ans << endl;  
    }
}

int main()
{
    init();
    work();

   // system("pause");
    return 0;
}
