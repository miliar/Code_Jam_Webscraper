#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    int T = 0;
    cin >> T;

    for (int Case = 1; Case<=T; Case++)
    {
        int N = 0;
        cin >> N;

        unsigned int sum = 0;
        unsigned int num = 0;
        unsigned int bigsum = 0;
        unsigned int min = 0xFFFFFFF;
        for (int i = 0; i<N; i++)
        {
            cin >> num;
            bigsum += num;
            sum ^= num;
            min = (min < num) ? min : num;
        }

        cout << "Case #" << Case << ": ";
        if (sum != 0)
        {
            cout << "NO" << endl;
        }
        else
        {
            cout << bigsum - min << endl;
        }

    }

    return 0;
}
