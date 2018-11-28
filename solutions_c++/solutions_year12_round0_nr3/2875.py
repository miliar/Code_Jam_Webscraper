//Christopher Mueller
//Made for Google Code Jam 2012

#include <fstream>
#include <string>
#include <sstream>
#include <set>
#include <utility>
#include <iostream>
#include <tr1/unordered_set>

struct Hasher
{
    std::size_t operator () (const std::pair <int, int>& p) const
    {
        return p.first * 119 + p.second;
    }
};

using namespace std;
using namespace tr1;

void solve(string& str)
{
    unordered_set <pair <int, int>, Hasher> pairs(999983);

    stringstream ss(str);
    int A, B;
    ss >> A >> B;

    for(int i = A; i <= B; ++i)
    {
        stringstream ss;
        ss << i;
        string num = ss.str();

        for(unsigned j = 1; j < num.size(); ++j)
        {
            string recycled(num.size(), ' ');
            unsigned k = 0;
            for(; k < j; ++k)
            {
                recycled[k] = num[num.size() - j + k];
            }
            for(; k < num.size(); ++k)
            {
                recycled[k] = num[k - j];
            }

            int n, m;
            stringstream ss(num);
            ss >> n;
            stringstream ss2(recycled);
            ss2 >> m;

            if(n < A || n > B || m < A || m > B || n == m || recycled[0] == '0') continue;
            if(n > m)
            {
                int temp = n;
                n = m;
                m = temp;
            }

            pairs.insert(pair <int, int>(n, m));
        }
    }

    unsigned count = pairs.size();
    stringstream out;
    out << count;
    str = out.str();
}

int main()
{
    string str;

    ifstream infile("C-small-attempt0.in");
    int T;
    infile >> T;
    getline(infile, str); //remove the newline after T

    ofstream outfile("output.txt");
    for(int i = 0; i < T; ++i)
    {
        outfile << "Case #" << i + 1 << ": ";
        getline(infile, str);

        solve(str);

        outfile << str << endl;
    }

    return 0;
}
