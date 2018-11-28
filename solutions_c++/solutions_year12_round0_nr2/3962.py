#include <iostream>

using namespace std;

int main(int argc, char *argv[])
{
    int num = 0;
    cin >> num;
    for (int count = 1; count <= num; ++count)
    {
        int N, S, p;
        cin >> N >> S >> p;
        int res = 0;
        for (int i = 0; i<N; ++i)
        {
            int score;
            cin >> score;
            int d = score / 3;
            int r = score % 3;
            if (d >= p)
                ++res;
            else if (d == p-1)
            {
                if (r == 0 && S > 0 && p-2 >= 0) { ++res; --S; }
                else if (r > 0) ++res;
            }
            else if (d == p-2)
            {
                if (r == 2 && S > 0) { ++res; --S; }
            }
        }
        cout << "Case #" << count << ": " << res << endl;
    }
    return 0;
}
