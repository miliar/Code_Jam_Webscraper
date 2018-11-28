#include <fstream>
#include <queue>

using namespace std;

int main()
{
    ifstream f("c.in");
    ofstream f2("c.out");
    int T;
    f>>T;
    for(int tt=1; tt<=T; ++tt)
    {
        long long r,k;
        long long n;
        f>>r>>k>>n;
        queue<long long> q;
        for(int i=0; i<n; ++i) { long long x; f>>x; q.push(x); }

        f2<<"Case #"<<tt<<": ";
        long long res = 0;

        for(int i=1; i<=r; ++i)
        {
            long long crtnopers = 0;
            long long towhere = q.size();
            long long where = 1;
            while(where<=towhere && crtnopers+q.front()<=k)
            {
                crtnopers += q.front();
                res += q.front();
                ++where;
                long long x = q.front();
                q.pop();
                q.push(x);
            }
        }
        f2<<res<<"\n";
    }
    return 0;
}
