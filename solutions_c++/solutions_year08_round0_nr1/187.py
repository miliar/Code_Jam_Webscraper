#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <map>

using namespace std;

typedef map<string, unsigned> Map;
const size_t MAX_BUF = 120;

int main()
{
    char c[MAX_BUF];
    unsigned tCount;
    ifstream is("test.in");
    is >> tCount;
    for (unsigned i = 0; i < tCount; ++i)
    {
        Map Ss;
        
        unsigned sc, qc;
        is >> sc;
        do 
        {
            is.get(c[0]);
        } while (c[0] != '\n');
        for (unsigned j = 0; j < sc; ++j)
        {
            is.getline(c, MAX_BUF);
            Ss[c] = j;
        }
        vector<bool> Qq(sc);

        unsigned cntr = sc;
        unsigned ans = 0;
        
        is >> qc;
        do 
        {
            is.get(c[0]);
        } while (c[0] != '\n');
        for (unsigned j = 0; j < qc; ++j)
        {
            is.getline(c, MAX_BUF);
            unsigned s = Ss[c];
            if (!Qq[s])
            {
                if (--cntr == 0)
                {
                    ++ans;
                    cntr = sc - 1;
                    fill(Qq.begin(), Qq.end(), false);
                }
                Qq[s] = true;
            }
        }
        cout << "Case #" << (i + 1) << ": " << ans << std::endl;
    }
    return 0;
}

