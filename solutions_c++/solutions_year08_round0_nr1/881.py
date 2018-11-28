# include <string>
# include <fstream>
# include <vector>
# include <memory>
# include <sstream>
# include <algorithm>

using namespace std;

const int MAXN = 1024;
char buff [1024];

int cnt [MAXN][MAXN];

string engine [MAXN];
string query [MAXN];

int main ()
{

    ifstream fin ("input.txt");
    ofstream fout ("output.txt");

    int tests = 0;

    fin.getline(buff, MAXN);
    {
        stringstream in(buff);
        in >> tests;
    }

    while (tests --)
    {

        memset (cnt, 0, sizeof (cnt));
        int n, m ; 
        fin.getline(buff, MAXN);
        {
            stringstream in(buff);
            in >> n;
        }

        for (int i = 0; i < n; ++ i)
        {
            fin.getline(buff, MAXN);
            engine [i]= buff;
        }
        
        fin.getline(buff, MAXN);
        {
            stringstream in(buff);
            in >> m;
        }

        for (int i = 0; i < m; ++ i)
        {
            fin.getline(buff, MAXN);
            query [i]= buff;
        }

        if (m)
        for (int i = 0; i < n; ++ i)
        {
            cnt [m - 1][i] = (int)(engine [i] == query [m - 1]);
        }

        if (m)
        for (int i = m - 2; i >= 0; -- i)
        {
            for (int j = 0; j < n; ++ j)
            {
                cnt [i][j] = 1000000;

                if (engine [j] != query [i])
                {
                    cnt [i][j] = cnt [i + 1][j];
                }

                for (int q = 0; q < n; ++ q)
                    if (q != j)
                        if (engine [q] != query [i] && cnt [i + 1][q] + 1 < cnt [i][j])
                        {
                            cnt [i][j] = cnt [i + 1][q] + 1;
                        }
            }
        }

        int res = 1000000;
        
        for (int i = 0; i < n; ++ i)
            res = min (res, cnt [0][i]);

        static int caseNum = 0;
        ++ caseNum ;

        fout << "Case #" << caseNum << ": " << res << endl;
    }

    return 0;
}