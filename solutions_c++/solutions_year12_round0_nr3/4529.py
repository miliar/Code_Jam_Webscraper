#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <map>
#include <utility>
#include <set>
using namespace std;

#define sz size

string rot(string s, int r)
{
    string ret(s.sz(), '.');
    for(int i = 0; i < s.sz(); ++i)
    {
        ret[i] = s[(i + r) % s.sz()];
    }

    if (ret[0] != '0')
        return ret;

    int n = 0;
    for(n = 0; n < ret.sz(); ++n)
    {
        if (ret[n] != '0')
            break;
    }
    ret.erase(0, n);
    return ret;
}

string itos(int a)
{
    stringstream out;
    out << a;
    return out.str();
}

int main()
{
    int T = 0;
    cin >> T;
    for(int t = 1; t <= T; ++t)
    {
        int A = 0;
        int B = 0;
        cin >> A >> B;
        int acc = 0;
        map< string, set<string> > check;
        for(int a = A; a < B; ++a)
        {
            for(int b = a + 1; b <= B; ++b)
            {
                string str_a = itos(a);
                string str_b = itos(b);
                for(int i = 1; i < str_b.sz(); ++i)
                {
                    string r = rot(str_b, i);
                    if(r.sz() != str_a.sz())
                        continue;

                    //they match
                    if(str_a.compare(r) == 0)
                    {
                        //we have already seen a
                        if(check.count(str_a) > 0)
                        {

                            if((check[str_a]).count(str_b) == 0)
                            {
                                (check[str_a]).insert(str_b);
                                ++acc;
                            }
                        }
                        else
                        {
                            (check[str_a]).insert(str_b);
                            ++acc;
                        }
                    }
                }
            }
        }
        cout << "Case #" << t << ": " << acc << endl;
    }
    return 0;
}
