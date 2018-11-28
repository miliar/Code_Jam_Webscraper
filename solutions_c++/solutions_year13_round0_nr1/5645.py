#include <iostream>
#include <string>
#include <cmath>
#include <algorithm>
#include <map>
#include <fstream>
#include <vector>

using namespace std;

ifstream in;
ofstream out;

void Solve(vector <vector<int> > A, int Tp, int Num)
{
    for (int j = 0; j < 4; ++j)
    {
        for (int k = 0; k < 4; ++k)
        {
            cout << A[j][k] << " ";
        }
        cout << endl;
    }
    cout << "_____" << endl;
    if (Tp != -1)
    {
        A[Tp / 10][Tp % 10] = 1;
    }
    for (int z = 0; z < 4; ++z)
    {
        int i = 0;
        bool q = 0;
        while(q != 1 && i < 4)
        {
            if (A[z][i] != 1)
            {
                q = 1;
            }
            ++i;
        }
        if (q == 0)
        {
            out << "Case #" << Num <<": X won" << endl;
            return;
        }
    }
    for (int z = 0; z < 4; ++z)
    {
        int i = 0;
        bool q = 0;
        while(q != 1 && i < 4)
        {
            if (A[i][z] != 1)
            {
                q = 1;
            }
            ++i;
        }
        if (q == 0)
        {
            out << "Case #" << Num <<": X won" << endl;
            return;
        }
    }
    if (A[0][0] == A[1][1] && A[1][1] == A[2][2] && A[2][2] == A[3][3] && A[3][3] == 1)
    {
        out << "Case #" << Num <<": X won" << endl;
        return;
    }
    cout << A[0][3] << A[1][2] << A[2][1] << A[3][0] << endl;
    if (A[0][3] == A[1][2] && A[1][2] == A[2][1] && A[2][1] == A[3][0] && A[3][0] == 1)
    {
        out << "Case #" << Num <<": X won" << endl;
        return;
    }
    if (Tp != -1)
    {
        A[Tp / 10][Tp % 10] = 2;
    }
    for (int z = 0; z < 4; ++z)
    {
        int i = 0;
        bool q = 0;
        while(q != 1 && i < 4)
        {
            if (A[z][i] != 2)
            {
                q = 1;
            }
            ++i;
        }
        if (q == 0)
        {
            out << "Case #" << Num <<": O won" << endl;
            return;
        }
    }
    for (int z = 0; z < 4; ++z)
    {
        int i = 0;
        bool q = 0;
        while(q != 1 && i < 4)
        {
            if (A[i][z] != 2)
            {
                q = 1;
            }
            ++i;
        }
        if (q == 0)
        {
            out << "Case #" << Num <<": O won" << endl;
            return;
        }
    }
    if (A[0][0] == A[1][1] && A[1][1] == A[2][2] && A[2][2] == A[3][3] && A[3][3] == 2)
    {
        out << "Case #" << Num <<": O won" << endl;
        return;
    }
    else if (A[0][3] == A[1][2] && A[1][2] == A[2][1] && A[2][1] == A[3][0] && A[3][0] == 2)
    {
        out << "Case #" << Num <<": O won" << endl;
        return;
    }
    for (int j = 0; j < 4; ++j)
    {
        for (int k = 0; k < 4; ++k)
        {
            if (A[j][k] == 0)
            {
                out << "Case #" << Num <<": Game has not completed" << endl;
                return;
            }
        }
    }
    out << "Case #" << Num <<": Draw" << endl;
    return;
}

int main()
{
    in.open("input.in");
    out.open("output.txt");
    long long T;
    int Tp = -1;
    char c;
    vector <vector<int> > A;
    A.resize(4);
    A[0].resize(4);
    A[1].resize(4);
    A[2].resize(4);
    A[3].resize(4);
    in >> T;
    for (long long i = 0; i < T; ++i)
    {
        Tp = 0;
        for (int j = 0; j < 4; ++j)
        {
            for (int k = 0; k < 4; ++k)
            {
                in >> c;
                if (c == '.')
                {
                    A[j][k] = 0;
                }
                else if (c == 'X')
                {
                    A[j][k] = 1;
                }
                else if (c == 'O')
                {
                    A[j][k] = 2;
                }
                else
                {
                    A[j][k] = 3;
                    Tp = j * 10 + k;
                }
            }
        }
        Solve(A, Tp, i + 1);
    }
    return 0;
}
