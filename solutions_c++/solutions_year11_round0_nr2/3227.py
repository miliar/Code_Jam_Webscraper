#include <iostream>
#include <string>
#include <cstring>
using namespace std;

const int MAX = 256;

int T, C, D, N;
char combine [MAX][MAX];
bool opposed [MAX][MAX];
string magic;

string reduce (string s)
{
    int n = s.length ();

    if (n >= 2 && combine [s [n - 2]][s [n - 1]] != '\0')
        return reduce (s.substr (0, n - 2) + combine [s [n - 2]][s [n - 1]]);

    for (int i = 0; i < n - 1; i++)
        if (opposed [s [i]][s [n - 1]])
            return "";

    return s;
}

string solve ()
{
    memset (combine, '\0', sizeof (combine));
    memset (opposed, false, sizeof (opposed));

    string s;
    cin >> C;

    for (int i = 0; i < C; i++)
    {
        cin >> s;
        combine [s [0]][s [1]] = combine [s [1]][s [0]] = s [2];
    }

    cin >> D;

    for (int i = 0; i < D; i++)
    {
        cin >> s;
        opposed [s [0]][s [1]] = opposed [s [1]][s [0]] = true;
    }

    cin >> N >> magic;
    string answer = "";

    for (int i = 0; i < N; i++)
        answer = reduce (answer + magic [i]);

    string list = "[";

    for (int i = 0; i < (int) answer.length (); i++)
        list += string (1, answer [i]) + (i + 1 < (int) answer.length () ? ", " : "");

    list += "]";
    return list;
}

int main ()
{
    cin >> T;

    for (int tc = 1; tc <= T; tc++)
        cout << "Case #" << tc << ": " << solve () << '\n';

    return 0;
}
