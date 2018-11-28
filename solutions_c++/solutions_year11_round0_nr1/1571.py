#include <fstream>
#include <cmath>

using namespace std;

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    size_t t = 0;
    fin >> t;
    for (size_t cont = 1; cont <= t; ++cont) {
        size_t n = 0;
        char color;
        int index;
        size_t step[2];
        int prev[2];
        size_t result = 0;
        step[0] = step[1] = 0;
        prev[0] = prev[1] = 1;
        fin >> n;

        for (size_t i = 0; i != n; ++i) {
            fin >> color >> index;

            size_t step_index = 0;
            if (color == 'O') step_index = 0;
            else step_index = 1;

            int k = abs(index - prev[step_index]);
            if (k > step[step_index]) {
                result += k - step[step_index] + 1;
                step[!step_index] += k - step[step_index] + 1;
            }
            else {
                result += 1;
                step[!step_index] += 1;
            }
            step[step_index] = 0;
            prev[step_index] = index;

        }

        fout << "Case #" << cont << ": " << result << endl;
    }

    fin.close();
    fout.close();
    return 0;
}
