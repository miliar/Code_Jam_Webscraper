#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

vector<vector<int>> inputTest(ifstream& in)
{
    vector<vector<int>> res;
    for (int i = 0; i < 4; ++i)
    {
        string s;
        getline(in, s);

        res.push_back(vector<int>(4, 0));

        for (int j = 0; j < 4; ++j)
        {
            if (s[j] == 'O')
                res[i][j] = -1;
            else if (s[j] == 'X')
                res[i][j] = 1;
            else if (s[j] == 'T')
                res[i][j] = 10;
            else
                res[i][j] = 0;
        }
    }

    string s;
    getline(in, s);

    return res;
}

string processTest(const vector<vector<int>>& test)
{
    vector<int> sums;
    for (int i = 0; i < 4; ++i)
    {
        int sum = 0;
        for (int j = 0; j < 4; ++j)
            sum += test[i][j];

        sums.push_back(sum);
    }

    for (int i = 0; i < 4; ++i)
    {
        int sum = 0;
        for (int j = 0; j < 4; ++j)
            sum += test[j][i];

        sums.push_back(sum);
    }

    {
    int sum = 0;
    for (int i = 0; i < 4; ++i)
        sum += test[i][i];

    sums.push_back(sum);
    }

    {
        int sum = 0;
        for (int i = 0; i < 4; ++i)
            sum += test[i][3 - i];

        sums.push_back(sum);
    }

    for(auto &s : sums)
    {
        if (s == -4 || s == 7)
            return "O won";
        if (s == 4 || s == 13)
            return "X won";
    }

    for (int i = 0; i < 4; ++i)
        for (int j = 0; j < 4; ++j)
            if (test[i][j] == 0)
                return "Game has not completed";

    return "Draw";
}

void outputTest(ofstream& out, int t, const string& res)
{
    out << "Case #" << t + 1 << ": " << res << endl;
}

int main()
{
    ifstream in("input.txt");
    if (!in.is_open())
        return 1;

    ofstream out("ouput.txt");
    if (!out.is_open())
        return 1;

    int testCases;
    in >> testCases;
    string s;
    getline(in, s);

    for (int t = 0; t < testCases; ++t)
    {
        vector<vector<int>> test;
        test = inputTest(in);
        string res = processTest(test);
        outputTest(out, t, res);
    }

	return 0;
}

