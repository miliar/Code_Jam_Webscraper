
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int N;

    cin >> N;

    for( int CASE=1; CASE <= N; CASE++ )
    {
        int n;
        cin >> n;

        vector<long long int> v1(n, 0), v2(n, 0);
        for( int i = 0; i < n; i++ )
        {
            int x;
            cin >> x;
            v1[i] = x;
        }
        for( int i = 0; i < n; i++ )
        {
            int x;
            cin >> x;
            v2[i] = x;
        }

        sort(v1.begin(), v1.end());
        sort(v2.begin(), v2.end());
        long long int prod = 0;
        for( int i = 0; i < n; i++ )
        {
            prod += v1[i]*v2[n-i-1];
        }

        cout << "Case #" << CASE << ": " << prod << endl;
    }

    return 0;
}


