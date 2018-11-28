# include <fstream>
# include <string>
# include <vector>
# include <math.h>
# include <algorithm>
# include <string.h>
using namespace std;
int main()
{
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int t;
    fin >> t;
    for (int j = 0; j < t; j++)
    {
        string s, q;
        fin >> s;
        bool ok = true;
        int r = s.length() - 1;
        while (s[r] == '0')
              r--;
        for (int i = r; i >= 0; i--)
            if (s[i] == '0')
               ok = false;
        if (ok)
        {
            for (int i = 0; i < s.length(); i++)
                if (s[i] <= '9' && s[i] >= '1')
                   q += s[i];
            for (int i = 0; i < q.length() - 1; i++)
                if (q[i + 1] > q[i])
                   ok = false;
        }
        if (!ok)
        {
            char *ch = new char[s.length()];
            for (int i = 0; i < s.length(); i++)
                ch[i] = s[i];
            next_permutation(ch, ch + s.length());
            fout << "Case #" << j + 1 << ": ";
            for (int i = 0; i < s.length(); i++)
                fout << ch[i];
        }
        else
        {
            char *ch = new char[s.length() + 1];
                for (int i = 0; i < s.length(); i++)
                    ch[i] = s[i];
            ch[s.length()] = '0';
            sort(ch, ch + s.length() + 1);
            int we = 0;
            while (ch[we] == '0')
                  we++;
            swap(ch[0], ch[we]);
            fout << "Case #" << j + 1 << ": ";
            for (int i = 0; i < s.length() + 1; i++)
                fout << ch[i];
        }
        fout << endl;
    }
    return 0;
}
