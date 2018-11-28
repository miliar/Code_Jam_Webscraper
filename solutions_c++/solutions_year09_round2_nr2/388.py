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

bool bigger(const string& first, const string& second)
{
    if (first.size() > second.size()) return true;
    if (first.size() < second.size()) return false;
    int pos = 0;
    while ((pos < first.size()) && (first[pos] == second[pos]))
        pos++;
    return (pos < first.size()) && (first[pos] > second[pos]);
}

void solve(fstream& fin, fstream& fout)
{
    int tests = read<int>(fin);
    for (int test = 1; test <= tests; test++)
    {
        fout << "Case #" << test << ": ";
        string number = read<string>(fin);
        bool found = false;
        for (int i = 2; i <= number.size(); i++)
        {
            int first = (int)number.size() - i;
            string tmp = number;
            int min = -1;
            for (int j = first; j < number.size(); j++)
                if ((tmp[j] > tmp[first]) && ((min == -1) || (tmp[j] < tmp[min])))
                    min = j;
            if (min != -1)
            {
                swap(tmp[first], tmp[min]);
                sort(tmp.begin() + first + 1, tmp.end());
                if (tmp > number)
                {
                    found = true;
                    fout << tmp << endl;
                    break;
                }
            }
        }
        if (!found)
        {
            string tmp = number;
            int min = -1;
            for (int i = 0; i < tmp.size(); i++)
                if ((tmp[i] > '0') && ((min == -1) || (tmp[i] < tmp[min])))
                    min = i;
            tmp = tmp[min] + tmp;
            tmp[min + 1] = '0';
            sort(tmp.begin() + 1, tmp.end());
            fout << tmp << endl;
        }
    }
    fout.close();
}

void main()
{
    //genTest();
    //solve(fin_test, fout_test);
    //solve(fin_small, fout_small);
    solve(fin_big, fout_big);
}