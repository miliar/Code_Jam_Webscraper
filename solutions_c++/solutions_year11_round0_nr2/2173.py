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
    for (int tt = 0; tt < t; tt++)
    {
        char comb[500][500];
        memset(comb, -1, sizeof(comb));
        int c;
        fin >> c;
        for (int i = 0; i < c; i++)
        {
            string s;
            fin >> s;
            comb[s[0]][s[1]] = comb[s[1]][s[0]] = s[2];
        }
        bool opposite[500][500];
        memset(opposite, false, sizeof(opposite));
        int d;
        fin >> d;
        for (int i = 0; i < d; i++)
        {
            string s;
            fin >> s;
            opposite[s[0]][s[1]] = opposite[s[1]][s[0]] = true;
        }
        int n;
        fin >> n;
        string s;
        fin >> s;
        deque<char> cur;
        for (int i = 0; i < n; i++)
        {
            cur.push_back(s[i]);
            if (cur.size() == 1)
               continue;
            int l = cur.size();
            char ch = comb[cur[l - 1]][cur[l - 2]];
            if (ch != -1)
            {
                  cur.pop_back();
                  cur.pop_back();
                  cur.push_back(ch);         
            }
            for (int j = 0; j < (int)cur.size() - 1; j++)
                if (opposite[cur[j]][cur.back()])
                {
                                                 cur.clear();
                                                 break;
                }
        }
        fout << "Case #" << tt + 1 << ": [";
        for (int i = 0; i < (int)cur.size() - 1; i++)
            fout << cur[i] << ", ";
        if (!cur.empty())
           fout << cur.back();
        fout << "]" << endl;
    }
    //system("pause");
    return 0;
}
