#include <iostream>
#include <cstring>
#include <map>
#include <iomanip>
using namespace std;

int table[5000009];
int sum[1 << 20];
int seq[32];

int N;
void print(int s)
{
    for(int i = 0; i < N; i++)
        if(s & (1 << i))
            cout << seq[i] << ' ';
    cout << '\n';
}
int main()
{
    int T; 
    cin >> T;
    while(T--)
    {
        cin >> N;

        static int tn = 0;
        cout << "Case #" << ++tn << ":\n";

memset(table, 0, sizeof(table));
        for(int i = 0; i < N; i++)
        {
            cin >> seq[i];
            sum[1 << i] = seq[i];
        }

        bool check = false;
        for(int i = 1; i < (1 << N); i++)
        {
            sum[i] = sum[i & -i] + sum[i - (i & -i)];
           
            if(table[sum[i]])
            {
                print(i);
                print(table[sum[i]]);
                check = true;
                break;
            }
            table[sum[i]] = i;
        }
        if(!check)
        cout << "Impossible\n";
    }

    return 0;
}
