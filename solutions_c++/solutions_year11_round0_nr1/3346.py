#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int T, N;
    
    cin >> T;
    
    for(int t = 0; t < T; t++)
    {
        cin >> N;
        
        char *R = new char[N];
        int *P = new int[N];
        
        vector<int> PO, PB;
        
        for(int n = 0; n < N; n++)
        {
            cin >> R[n];
            cin >> P[n];
            
            if(R[n] == 'O')
                PO.push_back(P[n]);
            else
                PB.push_back(P[n]);
        }
        
        int y = 0;
        int O = 1;
        int B = 1;
        
        int step, secs, next, dir;
        
        for(int n = 0; n < N; n++)
        {
            if(R[n] == 'O')
            {
                step = P[n] - O;
                O+= step;
                
                secs = abs(step) + 1;
                
                PO.erase(PO.begin());
                
                if(!PB.empty())
                {
                    next = PB.front();
                    dir = next < B ? -1 : 1;
                    B+= min(secs, abs(next - B)) * dir;
                }
            }
            else
            {
                step = P[n] - B;
                B+= step;
                
                secs = abs(step) + 1;
                
                PB.erase(PB.begin());
                
                if(!PO.empty())
                {
                    next = PO.front();
                    dir = next < O ? -1 : 1;
                    O+= min(secs, abs(next - O)) * dir;
                }
            }
            
            y+= secs;
        }
        
        cout << "Case #" << (t + 1) << ": " << y << endl;
    }
    
    return 0;
}