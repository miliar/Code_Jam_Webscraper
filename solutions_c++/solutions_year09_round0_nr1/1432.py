#include <fstream>
#include <set>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

fstream fin_small("small.in", ios_base::in);
fstream fout_small("small.out", ios_base::out);
fstream fin_big("big.in", ios_base::in);
fstream fout_big("big.out", ios_base::out);
fstream fin_test("test.in", ios_base::in);
fstream fout_test("test.out", ios_base::out);

template <typename T>
T read(fstream& fin)
{
    string s;
    getline(fin, s);
    T t;
    stringstream(s) >> t;
    return t;
}

vector<set<char>> split(string pattern, int count)
{
    vector<set<char>> result(count);
    int group = 0;
    bool insideGroup = false;
    for (int i = 0; i < pattern.length(); i++)
    {
        if (pattern[i] == '(')
            insideGroup = true;
        else if (pattern[i] == ')')
        {
            insideGroup = false;
            group++;
        }
        else
        {
            if (insideGroup)
                result[group].insert(pattern[i]);
            else
                result[group++].insert(pattern[i]);
        }
    }
    return result;
}

void solve(fstream& fin, fstream& fout)
{
    string ldn;
    getline(fin, ldn);
    int l, d, n;
    stringstream(ldn) >> l >> d >> n;
    vector<string> words;
    for (int i = 0; i < d; i++)
        words.push_back(read<string>(fin));
    for (int nn = 1; nn <= n; nn++)
    {
        string pattern = read<string>(fin);
        vector<set<char>>& patternseq = split(pattern, l);
        int answer = 0;
        for (int w = 0; w < d; w++)
        {
            bool ok = true;
            for (int k = 0; k < l; k++)
                if (patternseq[k].find(words[w][k]) == patternseq[k].end())
                {
                    ok = false;
                    break;
                }
            if (ok)
                answer++;
        }
        fout << "Case #" << nn << ": " << answer << endl;
    }
}

void genTest()
{
    fstream test("test.in");
    test << 15 << " " << 5000 << " " << 500 << endl;
    for (int i = 0; i < 5000; i++)
        test << "abcdefghijklmno" << endl;
    for (int i = 0; i < 500; i++)
    {
        for (int j = 0; j < 15; j++)
            test << "(abcdefghijklmnopqrstuvwxyz)";
        test << endl;
    }
    test.close();
}

void main()
{
    //genTest();
    //solve(fin_test, fout_test);
    //solve(fin_small, fout_small);
    solve(fin_big, fout_big);
}