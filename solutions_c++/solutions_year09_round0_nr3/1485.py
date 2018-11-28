#include <string>
#include <fstream>
#include <sstream>

using namespace std;

fstream fin_test = fstream("test.in", ios_base::in);
fstream fout_test = fstream("test.out", ios_base::out);
fstream fin_small = fstream("c-small.in", ios_base::in);
fstream fout_small = fstream("c-small.out", ios_base::out);
fstream fin_large = fstream("c-large.in", ios_base::in);
fstream fout_large = fstream("c-large.out", ios_base::out);

string welcome = "welcome to code jam";

void solve(fstream& fin, fstream& fout)
{
    string sn;
    getline(fin, sn);
    int n;
    stringstream(sn) >> n;
    for (int nn = 1; nn <= n; nn++)
    {
        string s;
        getline(fin, s);
        int cnt[505][55];
        memset(cnt, 0, sizeof(cnt));
        cnt[0][0] = 1;
        for (int i = 0; i < s.size(); i++)
        {
            for (int j = 0; j <= welcome.size(); j++)
            {
                if (cnt[i][j] > 0)
                {
                    cnt[i + 1][j] += cnt[i][j];
                    cnt[i + 1][j] %= 10000;
                    if (s[i] == welcome[j])
                    {
                        cnt[i + 1][j + 1] += cnt[i][j];
                        cnt[i + 1][j + 1] %= 10000;
                    }
                }
            }
        }
        stringstream ss;
        ss << cnt[s.size()][welcome.size()];
        string answer = ss.str();
        while (answer.size() < 4) answer = '0' + answer;
        fout << "Case #" << nn << ": " << answer << endl;
    }
}

void main()
{
    solve(fin_test, fout_test);
    solve(fin_small, fout_small);
    solve(fin_large, fout_large);
}