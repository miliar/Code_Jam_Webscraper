# include <fstream>
# include <string>
# include <vector>
# include <math.h>
# include <algorithm>
# include <string.h>
# include <stack>
# include <queue>
# include <sstream>
# include <set>
# include <map>
using namespace std;
int main()
{
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int t;
    fin >> t;
    for (int we = 0; we < t; we++)
    {
        int n, k;
        fin >> n >> k;
        int st = (1 << n);
        if (k % st == st - 1)
           fout << "Case #" << we + 1 << ": " << "ON" << endl;
        else
            fout << "Case #" << we + 1 << ": " << "OFF" << endl;
    }
    return 0;
}
