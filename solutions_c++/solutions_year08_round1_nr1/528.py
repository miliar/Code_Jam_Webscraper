#include <cstdlib>
#include <iostream>
#include <string>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>


using namespace std;

void Clear()
{
}

void Run()
{
    int N;
    cin >> N;

    vector<long long> v1;
    vector<long long> v2;

    for (int i=0; i<N; i++)
    {
        int n;
        cin >> n;

        v1.push_back(n);
    }

    sort(v1.begin(), v1.end());
    //copy(v1.begin(), v1.end(), ostream_iterator<int>(cout, " "));
    //cout << endl;

    for (int i=0; i<N; i++)
    {
        int n;
        cin >> n;

        v2.push_back(n);
    }

    sort(v2.rbegin(), v2.rend());
    //copy(v2.begin(), v2.end(), ostream_iterator<int>(cout, " "));
    //cout << endl;

    long long product = 0;

    for (int i=0; i<N; i++)
    {
        product += v1[i] * v2[i];
    }

    cout << product << endl;;
}

int main(int argc, char *argv[])
{
    int T;
    cin >> T;

    for (int i=0; i<T; i++)
    {
        cout << "Case #" << i + 1 << ": ";
        Run();
    }

    return 0;
}
