/*

This program can successfully run in BORLAND C++ BUILDER 6.
without file input/output in code.
you can run this program like this way(in WINDOWS command prompt):

p1.exe < inputfile.txt > outputfile.txt

And then take the outputfile.txt :)  

*/

#include <iostream>
#include <string>
using namespace std;

long long T, Ti, base, len;
long long num[130];
bool used[130];
long long list[100];
long long Min;
string str;

void init()
{
    long long i, j;
    char temp = '0';

    list[1] = 1;
    list[2] = 0;
    for (i = 3; i < 100; i++)
        list[i] = i - 1;

    getline(cin, str);
    len = str.length();
    memset(used, 0 , sizeof(used));
    for (i = 0; i < str.length(); i++)
    {
        used[str[i]] = true;
    /*    if (str[i] >= '0' & str[i] <= '9')
            num[i + 1] = str[i] - 48;
        else
            num[i + 1] = str[i] - 'a' + 10;  */      
    }

    base = 0;
    for (i = 0; i < 130; i++)
        if (used[i]) base++;
    if (base == 1) base = 2;

    Min = 0;
    memset(used, 0, sizeof(used));
    for (i = 0; i < str.length(); i++)
    {
        if (!used[str[i]])
        {
            ++Min;
            for (j = 0; j < str.length(); j++)
                if (str[j] == str[i])
                {
                    num[str[i]] = list[Min];
                }
            used[str[i]] = true;
        }   
    }
}

void work()
{
    long long i, j = 1;
    long long ans = 0;

    i = len;
    for (i = len - 1; i >= 0; i--)
    {
        ans += num[str[i]] * j;
        j *= base;
    }

    cout << "Case #" << Ti << ": " << ans << endl;
}

long long main()
{
    cin >> T;
    cin.ignore();
    for (Ti = 1; Ti <= T; Ti++)
    {
        init();
        work();
    }

    //system("pause");
    return 0;
}
