#include <iostream>
using namespace std;

int N, T, Ti, tot;
int a[20], c[10], d[10];

void init()
{
    char ch;

    tot = 0;
    memset(c, 0, sizeof(c));
    while (1)
    {
        cin.get(ch);
        if (ch == '\n') break;
        a[++tot] = ch - 48;
        c[ch - 48]++;
    }
}

bool check(int s)
{
    memset(d, 0, sizeof(d));
    while (s > 0)
    {
        d[s % 10]++;
        s = s / 10;
    }

    int i;
    for (i = 1; i <= 9; i++)
        if ((c[i] >= 1 || d[i] >= 1) && c[i] != d[i])
            return false;

    return true;
}

void work()
{
    int s, i;

    s = 0;
    for (i = 1; i <= tot; i++)
        s = s * 10 + a[i];

    s = s + 1;
    while (!check(s)) s++;

    cout << "Case #" << Ti << ": " << s << endl;
}

int main()
{
    cin >> T;
    cin.ignore();
    for (Ti = 1; Ti <= T; Ti++)
    {
        init();
        work();
    }

  //  system("pause");
    return 0;
}