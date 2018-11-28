#include <stdio.h>
#include <string>
#include <iostream>
#include <vector>
#include <assert.h>

using namespace std;

string problem = "A";

bool check(int i, int j, vector<string>& m, int K, char c)
{
    int dx[] = {1, -1, 0, 0, 1, 1, -1, -1};
    int dy[] = {0, 0, 1, -1, 1, -1, 1, -1};

    int M = m.size();
    int N = m[0].size();
    for (int d = 0; d < 8; ++d)
    {
        bool found = true;
        int ti = i;
        int tj = j;
        for (int k = K - 1; k >= 1; --k)
        {
            ti = i + dx[d] * k;
            tj = j + dy[d] * k;

            if (ti < 0 || ti >= M || tj <0 || tj >= N || m[ti][tj] != c)
            {
                found = false; break;
            }
        }
        if (found) 
        {
            // cerr << "found " << c << ", i,j,d = " << i << "," << j << "," << d << endl;
            return true;
        }
    }
    return false;
}

string proc(vector<string>& m, int K)
{
    int i,j;
    for (i = 0; i < m.size(); ++i)
    {
        int N = m[i].size();
        string tmp;
        for (j = 0; j < N; ++j)
        {
            if (m[i][j] != '.') tmp += m[i][j];
        }
        int k = tmp.size();
        for (; k < N; ++k)
        {
            tmp = "." + tmp;
        }
        assert(tmp.size() == N);
        m[i] = tmp;
        // cerr << i << ":" << m[i] << "\n";
    }

    bool foundR = false;
    bool foundB = false;
    for (i = 0; i < m.size(); ++i)
    {
        for (j = 0; j < m[i].size(); ++j)
        {
            if (m[i][j] != '.')
            {
                if (!foundR && m[i][j] == 'R' && check(i, j, m, K, 'R'))
                {
                    foundR = true;
                }
                if (!foundB && m[i][j] == 'B' && check(i, j, m, K, 'B'))
                {
                    foundB = true;
                }
                if (foundB && foundR) break;
            }
        }
        if (foundB && foundR) break;
    }

    if (foundB && foundR) return "Both";
    else if (foundR) return "Red";
    else if (foundB) return "Blue";
    return "Neither";
}

int main(int argc, char** argv)
{
    if (argc == 2)
    {
        problem = argv[1];
        string last3 = problem.substr(problem.size() - 3, 3);
        if (last3 == ".in")
            problem = problem.substr(0, problem.size() - 3);
    }

    string inPath = problem + ".in";
    string outPath = problem + ".out";

    cout << "doing " << inPath << endl;
    cout << "to    " << outPath << endl;
    
    freopen(inPath.data(), "r", stdin);
    freopen(outPath.data(), "w", stdout);

    int Ti,T;
    cin >> T;
    int i,j;
    for (Ti = 0; Ti < T; ++Ti)
    {
        int N,K;
        cin >> N >> K;
        vector<string> m;
        m.reserve(N);
        string line;
        for (i = 0; i < N; ++i) 
        {
            cin >> line;
            m.push_back(line);
        }        

        cout << "Case #" << Ti+1 << ": " << proc(m, K) << endl;
    }
    return 0;
}
