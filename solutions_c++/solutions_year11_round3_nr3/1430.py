#include <iostream>
#include <stdio.h>

using namespace std;

long long int fre[10005];
int N;
long long int L, H;
void printResult(int);
int main()
{
    freopen("small.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int numCase;

    cin >> numCase;

    for (int i = 1; i <= numCase; ++i)
    {
        cin >> N >> L >> H;
        for (int x = 0; x < N; ++x)
        {
            cin >> fre[x];
        }

        printResult(i);
    }

    return 0;
}

void printResult(int numCase)
{
    cout << "Case #" << numCase << ": ";
    bool flag = 0;
    //check harmony
    for (long long int i = L; i <= H; ++i)
    {
        flag = 0;
        for (int j = 0; j < N; ++j)
        {
            if (i % fre[j] != 0 && fre[j] % i != 0){
                flag = 1;
                break;
            }
        }
        if (flag == 0) {
            cout << i << endl;
            break;
        }
    }

    if (flag == 1){
        cout << "NO" << endl;
    }
}
