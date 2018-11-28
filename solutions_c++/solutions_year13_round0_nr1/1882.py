#define _USE_MATH_DEFINES

#include <iostream>
#include <fstream>

#include <algorithm>
#include <functional>
#include <utility>
#include <vector>
#include <set>
#include <map>
#include <stack>
#include <queue>
#include <string>
#include <sstream>
#include <iterator>
#include <cmath>

template<typename T> T fromString(const std::string &str)
{
    T x;
    std::stringstream(str) >> x;
    return x;
}

class MakeString
{
public:
    MakeString() : stream(){}
    template<class T>
    MakeString& operator<< (const T &arg)
    {
        stream << arg;
        return *this;
    }
    operator std::string() const
    {
        return stream.str();
    }
protected:
    std::stringstream stream;
};

/*
SOLUTION BEGIN
*/
using namespace std;

bool check(const vector<string> &m, char c)
{
    for(int i = 0; i < 4; ++i)
    {
        int cnt = 0;
        for(int j = 0; j < 4; ++j)
        {
            if(m[i][j] == 'T')
                cnt++;
            if(m[i][j] == c)
                cnt++;
        }
        if(cnt == 4)
            return true;
    }

    for(int i = 0; i < 4; ++i)
    {
        int cnt = 0;
        for(int j = 0; j < 4; ++j)
        {
            if(m[j][i] == 'T')
                cnt++;
            if(m[j][i] == c)
                cnt++;
        }
        if(cnt == 4)
            return true;
    }
    int cnt = 0;
    for(int i = 0; i < 4; ++i)
    {
        if(m[i][i] == 'T')
            cnt++;
        if(m[i][i] == c)
            cnt++;
    }
    if(cnt == 4)
        return true;

    cnt = 0;

    for(int i = 0; i < 4; ++i)
    {
        if(m[i][3 - i] == 'T')
            cnt++;
        if(m[i][3 - i] == c)
            cnt++;
    }
    if(cnt == 4)
        return true;

    return false;
}

bool wasF(const vector<string> &m)
{
    for(int i = 0; i < 4; ++i)
        for(int j = 0; j < 4; ++j)
            if(m[i][j] == '.')
                return false;
    return true;
}

int main(int argc, char **argv, char **envp)
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(false);

    int T;
    cin >> T;

    vector<string> VS(4, "    ");
    for(int t = 0; t < T; ++t)
    {
        for(int i = 0; i < 4; ++i)
            cin >> VS[i];
        cout << string(MakeString() << "Case #" << t + 1 << ": ");
        if(check(VS, 'X'))
            cout << "X won" << endl;
        else if(check(VS, 'O'))
            cout << "O won" << endl;
        else if(wasF(VS))
            cout << "Draw" << endl;
        else if(!wasF(VS))
            cout << "Game has not completed" << endl;
    }

    return 0;
}