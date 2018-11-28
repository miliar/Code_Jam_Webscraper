#include <fstream>
#include <vector>

using namespace std;

int main()
{
    fstream fin("input.txt");
    fstream fout("output.txt", ios_base::out);
    int tests, n, k, b, t;
    vector<int> x, v;
    fin >> tests;
    vector<bool> can(50);
    for (int test = 1; test <= tests; test++)
    {
        fin >> n >> k >> b >> t;
        for (int i = 0; i < n; i++)
            can[i] = false;
        x.clear();
        v.clear();
        int tmp;
        for (int i = 0; i < n; i++)
        {
            fin >> tmp;
            x.push_back(tmp);
        }
        for (int i = 0; i < n; i++)
        {
            fin >> tmp;
            v.push_back(tmp);
        }
        if (k == 0)
        {
            fout << "Case #" << test << ": 0" << endl;
            continue;
        }
        for (int i = 0; i < n; i++)
        {
            int mini = i;
            for (int j = i + 1; j < n; j++)
            {
                if (x[j] < x[mini])
                    mini = j;
            }
            int tmpx = x[i];
            int tmpv = v[i];
            x[i] = x[mini];
            v[i] = v[mini];
            x[mini] = tmpx;
            v[mini] = tmpv;
        }
        for (int i = 0; i < n; i++)
            can[i] = b <= t * v[i] + x[i];
        int cnt = 0;
        int i;
        for (i = n - 1; i >= 0; i--)
        {
            if (can[i])
                cnt++;
            if (cnt == k)
                break;
        }
        if (cnt == k)
        {
            int answer = 0;
            int notcan = 0;
            for (int j = i; j < n; j++)
            {
                if (!can[j])
                {
                    answer += j - i - notcan;
                    notcan++;
                }
                    
            }
            fout << "Case #" << test << ": " << answer << endl;
        }
        else
        {
            fout << "Case #" << test << ": IMPOSSIBLE" << endl;
        }
    }
    fin.close();
    fout.close();
    return 0;
}