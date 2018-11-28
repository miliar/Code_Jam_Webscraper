#include <fstream>
#include <string>
using namespace std;

ifstream fin("in.txt");
ofstream  fout("out.txt");

int a[5000][15];    // DxL
int b[5000];

int main()
{
    int L, D, N;
    fin >> L >> D >> N;
    string s;
    for (int i=0; i<D; i++)
    {
        fin >> s;
        for (int j=0; j<L; j++)
            a[i][j] = s[j];
    }
    for (int tc=0; tc<N; tc++)
    {
        for (int i=0; i<D; i++)
            b[i] = 0;
        fin >> s;
        int pos = 0, cnt = 0;
        bool ok = true;
        while (pos<s.size())
        {
            if (cnt>=L)
            {
                ok = false;
                break;
            }
            if (s[pos]=='(')
            {
                pos++;
                while (pos<s.size() && s[pos]!=')')
                {
                    for (int i=0; i<D; i++)
                        if (b[i]==cnt && a[i][cnt]==s[pos])
                            b[i]++;
                    pos++;                  
                }
            }
            else
                for (int i=0; i<D; i++)
                    if (b[i]==cnt && a[i][cnt]==s[pos])
                        b[i]++;
            cnt++;
            pos++;
        }
        int res = 0;
        if (ok)
        {
            for (int i=0; i<D; i++)
                if (b[i]==L)
                    res++;
        }
        fout << "Case #" << (tc+1) << ": " << res << endl;
    }
    return 0;
}