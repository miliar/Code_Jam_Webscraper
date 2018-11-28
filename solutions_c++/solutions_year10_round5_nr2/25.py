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
        ll L;
        int N;
        cin >> L >> N;
        vector<ll> B(N);
        for (int i = 0; i < N; i++)
            cin >> B[i];
        sort(RA(B));

        int M = B.back();
        int phase = L % M;
        vector<int> dist(M, -1);
        deque<pii> q;
        q.push_back(pii(0, 0));
        dist[0] = 0;
        while (!q.empty())
        {
            int cur = q.front().first;
            int cur_dist = q.front().second;
            q.pop_front();
            if (cur_dist != dist[cur])
                continue;
            if (cur == phase) break;
            for (int i = 0; i < N - 1; i++)
            {
                int next = cur + B[i];
                int next_dist = cur_dist + 1;
                if (next >= M)
                {
                    next -= M;
                    next_dist--;
                }
                if (dist[next] == -1 || next_dist < dist[next])
                {
                    dist[next] = next_dist;
                    if (next_dist == cur_dist)
                        q.push_front(pii(next, next_dist));
                    else
                        q.push_back(pii(next, next_dist));
                }
            }
        }

        printf("Case #%d: ", cas + 1);
        if (dist[phase] == -1)
            printf("IMPOSSIBLE\n");
        else
            printf("%lld\n", (L - phase) / M + dist[phase]);
    }
    return 0;
}
