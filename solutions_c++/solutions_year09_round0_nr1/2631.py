#include <iostream>
#include <list>
#include <string>
#include <vector>
#include <cstdlib>
#include <cstdio>
using namespace std;
#include <stdio.h>
#include <string.h>

int main()
{
    int L, D, N;
    int i = 0;
    int j = 0;
    int x, y, z, k, count;
    bool found = false;
    string str;
    const char *strChar = NULL;
    cin >> L >> D >> N;

    string *words = new string[D];
    for( i = 0; i < D; i++ )
    {
        cin >> words[i];
    }

    for( i = 0; i < N; i++ )
    {
        cin >> str;
        strChar = str.c_str();

        count = 0;

        for( j = 0; j < D; j++ )
        {
            x = y = z = k = 0;
            const char *wordsChar = words[j].c_str();
            while(k < str.size())
            {
                if(strChar[k] == '(')
                {
                    x = k + 1;
                    //Find the closing brace
                    while(strChar[x] != ')')
                        x++;
                }
                else
                {
                    x = k;
                }

                found = false;
                for( y = k; y <= x; y++ )
                {
                    if(wordsChar[z] == strChar[y])
                    {
                        found = true;
                        break;
                    }
                }

                k = ++x;
                z++;
                if( found != true )
                {
                    break;
                }
            }

            if( found != true )
                continue;
            else
            {
                count++;
                //cout << "Case #" << i + 1 << ": " << count << endl;
            }
        }

        cout << "Case #" << i + 1 << ": " << count << endl;
    }


    return 0;
}
