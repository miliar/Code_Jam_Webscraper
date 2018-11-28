#include <iostream>
#include <string>
#include <set>

using namespace std;

int main()
{
    int N, S, Q;
    int asw;
    set<string> names;

    cin >> N;

    for ( int c = 1; c <= N; c++ )
    {
        string s;
        names.clear();
        asw = 0;

        cin >> S; getline(cin, s);
        for ( int i = 0; i < S; i++ ) getline(cin, s);

        cin >> Q; getline(cin, s);
        for ( int i = 0; i < Q; i++ )
        {
            getline(cin, s);
            names.insert(s);
            if ( names.size() == S )
            {
                asw++;
                names.clear();
                names.insert(s);
            }
        }
        cout << "Case #" << c << ": " << asw << endl;
    }

    return 0;
}
