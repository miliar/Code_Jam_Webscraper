#include<iostream>
#include<vector>
#include<algorithm>

using namespace std;

int main()
{
    int T, num, i;
    cin >> T;
    vector <int> A;
    vector <int> V;
    for(num = 1; num <= T; ++num)
    {
        long long t;
        int L, N, C;
        cin >> L >> t >> N >> C;
        A.resize(C);
        for(i=0;i<C;++i)
            cin >> A[i];
        V.resize(0);
        long long alldist = 0;
        int delta = 0;
        for(i=0;i<N;++i)
        {
            delta = A[i % C];
            if (2 * alldist >= t)
            {
                V.push_back(delta);
            }
            else if(2 * (alldist + delta) <= t)
            {

            }
            else
            {
                V.push_back( alldist + delta - t / 2);
            }
            alldist += delta;
        }
        alldist *= 2;
        sort(V.rbegin(), V.rend());
        i = 0;
        while (i < V.size() && L > 0)
        {
            alldist -= V[i];
            --L;
            ++i;
        }
        cout << "Case #" << num << ": " << alldist << endl;
    }
}
