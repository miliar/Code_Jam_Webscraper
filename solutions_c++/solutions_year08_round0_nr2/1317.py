/* vim: set sw=4 sts=4 et foldmethod=syntax : */

#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int main()
{
    int N;
    cin >> N;

    for (int n = 0 ; n < N ; ++n)
    {
        int T, NA, NB;
        cin >> T >> NA >> NB;

        vector<pair<int, int> > A;
        vector<pair<int, int> > B;

        while (NA--)
        {
            int h, m;
            scanf("%d:%d", &h, &m);
            A.push_back(make_pair(h*60 + m, 1));
            scanf("%d:%d", &h, &m);
            B.push_back(make_pair(h*60 + m + T, -1));
        }

        while (NB--)
        {
            int h, m;
            scanf("%d:%d", &h, &m);
            B.push_back(make_pair(h*60 + m, 1));
            scanf("%d:%d", &h, &m);
            A.push_back(make_pair(h*60 + m + T, -1));
        }


        sort(A.begin(), A.end());
        sort(B.begin(), B.end());

        int trains = 0;
        int max = 0;

        for (int i = 0 ; i < A.size() ; ++i)
        {
            trains += A[i].second;
            if (trains > max)
                max = trains;
        }

        cout << "Case #" << n + 1 << ": " << max;

        trains = 0;
        max = 0;

        for (int i = 0 ; i < B.size() ; ++i)
        {
            trains += B[i].second;
            if (trains > max)
                max = trains;
        }
        cout << " " << max << "\n";
    }

    return 0;
}
