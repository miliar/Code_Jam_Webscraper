#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <algorithm>

using namespace std;

char m[100][100];

int main()
{
    int nCase;
    cin >> nCase;

    for (int iCase = 1; iCase <= nCase; ++iCase) {

        memset(m, 0, sizeof(m));

        unsigned R, C;
        cin >> R >> C;
        for (size_t i = 0; i < R; ++i) {
            string s;
            cin >> s;
            //cout << "Row " << i << ": " << s << endl;
            strncpy(m[i], s.c_str(), C);
        }

        cout << "Case #" << iCase << ":" << endl;

        while (true) {
            bool any = false;
            for (size_t i = 0; i < R; ++i) {
                for (size_t j = 0; j < C; ++j) {
                    if (m[i][j] == '#')
                        any = true;
                }
            }
            
            if (!any) {
                for (size_t i = 0; i < R; ++i) {
                    cout << string(m[i]) << endl;
                }
                goto done;
            }

            for (size_t i = 0; i < R; ++i) {
                for (size_t j = 0; j < C; ++j) {
                    if (m[i][j] == '#') {
                        if (i+1 >= R || j+1 >= C)
                            goto impossible;

                        m[i][j] = '/';

                        if (m[i+1][j] != '#')
                            goto impossible;
                        else
                            m[i+1][j] = '\\';

                        if (m[i][j+1] != '#')
                            goto impossible;
                        else
                            m[i][j+1] = '\\';

                        if (m[i+1][j+1] != '#')
                            goto impossible;
                        else
                            m[i+1][j+1] = '/';

                        goto next;
                    }
                }
            }
        next:
            ;
        }

    impossible:
        cout << "Impossible" << endl;

    done:
        ;
    }
}

