#include <cstdlib>
#include <iostream>
#include <queue>

using namespace std;

// declaración de prototipo
string intToBinary(string);

int main()
{
    freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
    
    int T, R, k, N;
    double q, value, value_tot;
    cin >> T;
    
    for (int t = 0; t < T; t++)
    {
        cin >> R >> k >> N;
        queue<double> Q;
        value = 0.0;
        for (int n = 0; n < N; n++)
        {
            cin >> q;
            Q.push(q);
            value += q;
        }
        
        if (value < k)
           value_tot = R*value;
        else
        {
            value_tot = 0.0;
            for (int r = 0; r < R; r++)
            {
                value = 0.0;
                while ((value + Q.front()) <= k)
                {
                      value += Q.front();
                      Q.push(Q.front());
                      Q.pop();
                }
                value_tot += value;     
            }
        }
        cout << "Case #" << t+1 << ": " << (int)value_tot << endl;
    }
    
    return 0;
    
}
