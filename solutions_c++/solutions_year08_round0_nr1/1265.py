#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

ifstream in("input.txt");
ofstream out("output.txt");

const int MAXQ = 1500, MAXS = 150;

void solve(int case_n)
{
    string t;
    int S, Q;
    int A[MAXQ][MAXS];
    vector<string> names;

    in >> S; getline(in, t);
    for (int i = 0; i < S; i++)
    {
        string s;
        getline(in, s);
        names.push_back(s);
    }

    for (int i = 0; i < S; i++)
        A[0][i] = 0;

    in >> Q; getline(in, t);

    for (int i = 1; i <= Q; i++)
    {
        string q;
        getline(in, q);
        for (int j = 0; j < S; j++)
        {
            A[i][j] = -1;
            if (names[j] == q) continue;
            for (int k = 0; k < S; k++)
            {
                if (A[i-1][k] == -1) continue;
                if (k == j)
                {
                    if ((A[i][j] == -1) || (A[i-1][k] < A[i][j]))
                        A[i][j] = A[i-1][k];
                }
                else
                {
                    if ((A[i][j] == -1) || (A[i-1][k]+1 < A[i][j]))
                        A[i][j] = A[i-1][k]+1;
                }
            }
        }
    }

    int m = 100000000;
    for (int i = 0; i < S; i++)
        if ((m > A[Q][i]) && (A[Q][i] != -1))
            m = A[Q][i];
    out << "Case #" << case_n << ": " << m << endl;
}

int main()
{
    int n;
    in >> n;
    for (int i = 0; i < n; i++)
        solve(i+1);
}
