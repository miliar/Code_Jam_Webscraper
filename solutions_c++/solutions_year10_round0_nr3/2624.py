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
        int r, k, n;
        fin >> r >> k >> n;
        vector<int> a(n);
        for (int i = 0; i < n; i++)
            fin >> a[i];
        queue<int> q;
        for (int i = 0; i < n; i++)
            q.push(a[i]);
        long long rez = 0;
        for (int i = 0; i < r; i++)
        {
            int temp = 0, cur = 0;
            while (temp + q.front() <= k && cur < n)
            {
                  cur++;
                  temp += q.front();
                  q.push(q.front());
                  q.pop();
            }
            rez += (long long)temp;
        }
        fout << "Case #" << we + 1 << ": " << rez << endl;
    }
    return 0;
}
