// =============================================================================
// 
//       Filename:  A.cpp
// 
//    Description:  Speaking in Tongues
// 
//        Version:  1.0
//        Created:  04/14/2012 02:40:51 PM
//       Revision:  none
//       Compiler:  g++
// 
//         Author:  SphinX (Whisper), TopCoderSphinX@Gmail.com
//        Company:  HFUT
// 
// =============================================================================

#include <string>
#include <cstdio>
#include <cstdlib>
#include <iostream>
using namespace std;

void ace()
{
    char hs[] = {'y', 'h', 'e', 's', 'o', 'c', 'v', 'x', 'd', 'u', 'i', 
    'g', 'l', 'b', 'k', 'r', 'z', 't', 'n', 'w', 'j', 'p', 'f', 'm', 'a', 'q'};
    int test;
    string str;
    int cas = 1;
    for (cin >> test, getchar(); test--; ++cas) 
    {
        getline(cin, str);
        cout << "Case #" << cas << ": ";
        for (int i = 0; i < static_cast<int>(str.length()); ++i) 
        {
            if ('a' <= str[i] && str[i] <= 'z') 
            {
                cout << hs[static_cast<int>(str[i]) - 'a'];
            }
            else
            {
                cout << str[i];
            }
        }
        cout << endl;
    }
    
    return ;
}
int main(int argc, char *argv[]) 
{
    freopen("A-small-attempt2.in", "r", stdin);
    freopen("A-small-attempt2.out", "w", stdout);
    ace();
    return EXIT_SUCCESS;
}
