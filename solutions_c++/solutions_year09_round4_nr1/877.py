#include <fstream>
#include <set>
#include <string>
#include <vector>
#include <sstream>
#include <iomanip>
#include <algorithm>

using namespace std;

fstream fin_small("small.in", ios_base::in);
fstream fout_small("small.out", ios_base::out);
fstream fin_big("large.in", ios_base::in);
fstream fout_big("large.out", ios_base::out);
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

template <>
string read<string>(fstream& fin)
{
    string s;
    getline(fin, s);
    return s;
}

void solve(fstream& fin, fstream& fout)
{
    int tests = read<int>(fin);
    for (int test = 1; test <= tests; test++)
    {
        int n = read<int>(fin);
        vector<int> positions;
        for (int i = 0; i < n; i++)
        {
            string row  = read<string>(fin);
            int index = 0;
            for (int j = n - 1; j >= 0; j--)
            {
                if (row[j] == '1')
                {
                    index = j;
                    break;
                }
            }
            positions.push_back(index);
        }
        int answer = 0;
        for (int i = 0; i < n; i++)
        {
            for (int k = 0; k < n; k++)
            {
                if (positions[k] <= i)
                {
                    answer += k;
                    positions.erase(positions.begin() + k);
                    break;
                }
            }
        }
        fout << "Case #" << test << ": " << answer << endl;
    }
    fout.close();
}

void main()
{
    //solve(fin_test, fout_test);
    //solve(fin_small, fout_small);
    solve(fin_big, fout_big);
}