#include <iostream>
#include <algorithm>

using namespace std;

int main()
{
    int T;
    cin >> T;
    
    int N, L, H;
    
    int *freqs;
    
    int freq;
    bool mult;
    
    for(int t = 1; t <= T; t++)
    {
        cin >> N;
        cin >> L;
        cin >> H;
        
        freqs = new int[N];
        
        for(int n = 0; n < N; n++)
        {
            cin >> freqs[n];
        }
        
        sort(freqs, freqs + N);
        
        freq = -1;
        
        for(int i = L; i <= H; i++)
        {
            mult = true;
        
            for(int n = 0; n < N && mult; n++)
            {
                if(freqs[n] < i)
                    mult = i % freqs[n] == 0;
                else
                    mult = freqs[n] % i == 0;
            }
            
            if(mult)
            {
                freq = i;
                break;
            }
        }
        
        cout << "Case #" << t << ": ";
        
        if(freq == -1)
            cout << "NO";
        else
            cout << freq;
            
        cout << endl;
    }

    return 0;
}
