#include <iostream>

using namespace std;

int main()
{
    const int MAXN = 100;
    int X[MAXN] = { 0 };
    int Y[MAXN] = { 0 };
    
    int N = 0;
    cin >> N;
    for (int c = 1; c <= N; c++)
    {
        int n, A, B, C, D, x0, y0, M;
        cin >> n >> A >> B >> C >> D >> x0 >> y0 >> M;
        int x = x0, y = y0;
        for (int i = 0; i < n; i++)
        {
            X[i] = x;
            Y[i] = y;
            x = (int)(((long long)A * x + B) % M);
            y = (int)(((long long)C * y + D) % M);
        }
        
        long long count = 0;
        for (int i = 0; i < n; i++)
        {
            for (int j = i + 1; j < n; j++)
            {
                for (int k = j + 1; k < n; k++)
                {
                    if ((X[i] + X[j] + X[k]) % 3)
                        continue;
                    if ((Y[i] + Y[j] + Y[k]) % 3)
                        continue;
                    count++;
                }
            }
        }
        
        cout << "Case #" << c << ": " << count << endl;
    }
    
    return 0;
}
