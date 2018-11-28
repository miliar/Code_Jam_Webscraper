#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <cstdio>
#include <algorithm>

using namespace std;

ifstream fin("probC.in");
ofstream fout("answer.out");

bool is_same(int a, int b)
{
    stringstream ss;
    string sa, sb;

    ss << a; ss >> sa; ss.clear();
    ss << b; ss >> sb; ss.clear();
    for (size_t i = 0; i < sa.size(); ++i) {
        rotate(sb.begin(), sb.end() - 1, sb.end());
        if (sa == sb)
            return true;
    }

    return false;
}

int main()
{
    int n;
    fin >> n;
    for (int _ = 0; _ < n; ++_) {
        int A, B;
        fin >> A >> B;

        int ans = 0;
        for (int i = A; i <= B; ++i)
            for (int j = i + 1; j <= B; ++j) {
                if (is_same(i, j)) {
                    ++ans;
                }
            }
        fout << "Case #" << _+1 << ": " << ans << endl;
    }
    return 0;
}
