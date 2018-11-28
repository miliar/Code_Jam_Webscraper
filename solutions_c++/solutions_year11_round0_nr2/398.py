// google code jam B

#include <iostream>
#include <string>
#include <fstream>
using namespace std;

const int MAXC = 40, MAXD = 30;

string combine[MAXC], opposed[MAXD], ans;
int c, d, n;

void solve(string opt)
{
    ans = "";
    for (int i = 0; i < opt.size(); i++)
    {
        char last = ans.size() > 0 ? ans[ans.size() - 1] : char(0);
        bool comflag = false, clrflag = false;
        for (int j = 0; j < c; j++)
            if (combine[j][0] == last && combine[j][1] == opt[i] || combine[j][1] == last && combine[j][0] == opt[i])
            {
                ans[ans.size() - 1] = combine[j][2], comflag = true;
                break;
            }
        for (int j = 0; !comflag && !clrflag && j < d; j++)
            for (int k = 0; !clrflag && k < ans.size(); k++)
                if (opposed[j][0] == opt[i] && opposed[j][1] == ans[k] || opposed[j][1] == opt[i] && opposed[j][0] == ans[k])
                {
                    ans = "", clrflag = true;
                    break;
                }
        if (!comflag && !clrflag)
            ans += opt[i];
    }
}

int main()
{
    char filename[100];
    cin >> filename;
    ifstream fin(filename, ios::in);
    ofstream fout("bout.txt", ios::out);
    int testcase;
    fin >> testcase;
    string s;
    for (int test = 1; test <= testcase; test++)
    {
        fin >> c;
        for (int i = 0; i < c; i++)
            fin >> combine[i];
        fin >> d;
        for (int i = 0; i < d; i++)
            fin >> opposed[i];
        fin >> n >> s;
        solve(s);
        fout << "Case #" << test << ": [";
        for (int i = 0; i < ans.size(); i++)
            if (i == 0)
                fout << ans[i];
            else
                fout << ", " << ans[i];
        fout << "]" << endl;
    }
    fin.close();
    fout.close();
    return 0;
}