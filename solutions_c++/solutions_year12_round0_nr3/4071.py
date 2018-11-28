#include <fstream>
#include <sstream>
#include <map>
using namespace std;

ifstream cin("c.in");
ofstream cout("c.out");

int ans = 0;
int t, a, b;
map<string, bool> opt;

int s2i(string value)
{
    std::istringstream stream(value);
    int ret = 0;
    stream >> ret;
    return ret;
}

string i2s(int value)
{
    std::ostringstream stream;
    string ret = "";
    stream << value;
    ret = stream.str();
    return ret;
}

void solve(int k)
{
    string s = i2s(k);

    for(int i = 1; i < s.size(); ++i)
    {
        string s1 = s.substr(0, i);
        string s2 = s.substr(i, s.size() - i);

        if( s2i(s2 + s1) >= a && s2i(s2 + s1) <= b && s2i(s2 + s1) != k)
        {
            if(!opt.count(s2+s1+s) && !opt.count(s+s2+s1))
            {
                opt[s2+s1+s] = true;
                opt[s+s2+s1] = true;
                ans++;
            }
        }

    }

    return;
}

int main()
{
    cin >> t;

    for(int k = 1; k <= t; ++k)
    {
        opt.clear();
        ans = 0;
        cin >> a >> b;
        for(int i = a; i <= b; i++)
        {
            solve(i);
        }
        cout << "Case #" << k << ": "<< ans << endl;
    }

    return 0;
}
