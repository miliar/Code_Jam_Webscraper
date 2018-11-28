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
    ios_base::sync_with_stdio(false);
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    int t;
    fin >> t;
    for (int i = 0; i < t; i++)
    {
        int n;
        fin >> n;
        vector<int> a(n);
        for (int j = 0; j < n; j++)
            fin >> a[j];
        int asum = 0;
        int axor = 0;
        sort(a.begin(), a.end());
        
        for (int j = 0; j < n; j++)
        {
            axor ^= a[j];
            asum += a[j];
        }
        fout << "Case #" << i + 1 << ": ";
        if (axor == 0)
           fout << asum - a[0];
        else
            fout << "NO";
        fout << endl;
    }
    //system("pause");
    return 0;
}
