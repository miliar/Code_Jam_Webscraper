# include <fstream>
# include <string>
# include <algorithm>
using namespace std;
string s;
string *words;
int ter;
int *q1, *q2;
int l, d, n;
int main()
{
    ifstream fin ("input.txt");
    ofstream fout ("output.txt");
    fin >> l >> d >> n;
    words = new string[d];
    for (int i = 0; i < d; i++)
        fin >> words[i];
    for (int i = 0; i < n; i++)
    {
        q1 = new int[l];
        q2 = new int[l];
        int temp = 0;
        fin >> s;
        for (int j = 0; j < l; j++)
        {
            if (s[temp] == '(')
            {
                        temp++;
                        q1[j] = temp;
                        while (s[temp] != ')')
                              temp++;
                        q2[j] = temp - 1;
            }
            else
            {
                q1[j] = temp;
                q2[j] = temp;
            }
            temp++;
        }
        ter = 0;
        for (int j = 0; j < d; j++)
        {
            bool ok = true;
            for (int e = 0; e < l; e++)
            {
                bool sym = false;
                for (int r = q1[e]; r <= q2[e]; r++)
                    if (words[j][e] == s[r])
                    {
                       sym = true;
                       break;
                    }
                if (!sym)
                {
                         ok = false;
                         break;
                }
            }
            if (ok)
               ter++;
        }
        fout << "Case #" << i + 1 << ": " << ter << endl;
    }
    return 0;
}
