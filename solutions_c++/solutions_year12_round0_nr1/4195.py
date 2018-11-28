#include <iostream>
#include <algorithm>
#include <fstream>
#include <vector>
#include <map>
#include <set>

using  namespace std;

const string S = "yhesocvxduiglbkrztnwjpfmaq";

#define small
//#define large
int main()
{
#ifdef small
    freopen("A-small.in", "rt", stdin);
    freopen("A-small.out", "wt", stdout);
#endif

#ifdef large
    freopen("A-large.in", "rt", stdin);
    freopen("A-large.out", "wt", stdout);
#endif
    
    string s;
    int T, Case = 1;
    cin >> T;
    getchar();
    while(T --)
    {
        getline(cin, s);
        for(int i = 0; i != s.size(); i ++)
        {
            if(s[i] != 32)
                s[i] = S[s[i] - 'a'];
        }
        cout << "Case #" << Case ++ << ": " << s << endl;
    }
    return 0;
}
