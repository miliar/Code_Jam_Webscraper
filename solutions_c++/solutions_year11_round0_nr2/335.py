#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <iostream>
#include <sstream>
#include <cstddef>
#include <algorithm>
#include <utility>
#include <iterator>
#include <numeric>
#include <list>
#include <complex>
#include <cstdio>
#include <climits>
#include <fcntl.h>
#include <unistd.h>

using namespace std;

typedef vector<int> vi;
typedef vector<string> vs;
typedef long long ll;
typedef complex<double> pnt;
typedef pair<int, int> pii;

#define RA(x) (x).begin(), (x).end()
#define FE(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define SZ(x) ((int) (x).size())

template<class T>
void splitstr(const string &s, vector<T> &out)
{
    istringstream in(s);
    out.clear();
    copy(istream_iterator<T>(in), istream_iterator<T>(), back_inserter(out));
}

template<class T> T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }

static void redirect(int argc, const char **argv)
{
    if (argc > 1)
    {
        int fd = open(argv[1], O_RDONLY);
        if (fd == -1) { perror(argv[1]); exit(1); }
        if (-1 == dup2(fd, 0)) { perror(argv[1]); exit(1); }
        if (-1 == close(fd)) { perror(argv[1]); exit(1); }
    }

    if (argc > 2)
    {
        int fd = open(argv[2], O_WRONLY | O_CREAT, 0666);
        if (fd == -1) { perror(argv[2]); exit(1); }
        if (-1 == dup2(fd, 1)) { perror(argv[2]); exit(1); }
        if (-1 == close(fd)) { perror(argv[2]); exit(1); }
    }
}

int main(int argc, const char **argv)
{
    redirect(argc, argv);

    int cases;
    cin >> cases;
    for (int cas = 0; cas < cases; cas++)
    {
        int C, D, N;
        string invoked;
        vector<int> ans;
        int in_ans[26] = {};
        int combine[26][26];
        vector<int> oppose[26];
        cin >> C;

        memset(combine, -1, sizeof(combine));
        for (int i = 0; i < C; i++)
        {
            string s;
            cin >> s;
            int a = s[0] - 'A';
            int b = s[1] - 'A';
            combine[a][b] = combine[b][a] = s[2] - 'A';
        }
        cin >> D;
        for (int i = 0; i < D; i++)
        {
            string s;
            cin >> s;
            int a = s[0] - 'A';
            int b = s[1] - 'A';
            oppose[a].push_back(b);
            oppose[b].push_back(a);
        }
        cin >> N >> invoked;
        for (int i = 0; i < N; i++)
        {
            int cur = invoked[i] - 'A';
            bool done = false;
            if (!ans.empty())
            {
                int c = combine[ans.back()][cur];
                if (c != -1)
                {
                    in_ans[ans.back()]--;
                    ans.back() = c;
                    in_ans[ans.back()]++;
                    done = true;
                }
            }
            if (!done)
            {
                for (size_t j = 0; j < oppose[cur].size(); j++)
                {
                    int o = oppose[cur][j];
                    if (in_ans[o] != 0)
                    {
                        ans.clear();
                        fill(in_ans, in_ans + 26, 0);
                        done = true;
                        break;
                    }
                }
            }
            if (!done)
            {
                ans.push_back(cur);
                in_ans[cur]++;
            }
        }
        printf("Case #%d: [", cas + 1);
        for (size_t i = 0; i < ans.size(); i++)
        {
            if (i) printf(", ");
            printf("%c", ans[i] + 'A');
        }
        printf("]\n");
    }
    return 0;
}
