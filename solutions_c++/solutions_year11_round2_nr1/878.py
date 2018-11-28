#include <iostream>
#include <cstdio>
using namespace std;

typedef long long LL;

int N;
char input[128][128];

double WP[128], OWP[128], OOWP[128];
int saveW[128], saveL[128];

void solve()
{
    for (int i = 0; i < N; i++)
    {
        int win = 0, lost = 0;
        for (int j = 0; j < N; j++)
        {
            if (input[i][j] == '1') { win++; continue; }
            if (input[i][j] == '0') { lost++; continue; }
        }
        
        saveW[i] = win; saveL[i] = lost;
        WP[i] = (double)win / ((double)win + lost);
    }

    for (int i = 0; i < N; i++)
    {
        int op = 0; double sum = 0;
        for (int j = 0; j < N; j++)
            if (input[i][j] != '.') 
            {
                op++;
                int win = saveW[j], lost = saveL[j];
                if (input[i][j] == '1') lost--; else win--;
                
                sum += (double)win / ((double)win + lost);
            }
            
        OWP[i] = sum / (double)op; 
    }
    
    for (int i = 0; i < N; i++)
    {
        double sum = 0; int op = 0;
        for (int j = 0; j < N; j++)
            if (input[i][j] != '.') { op++; sum += OWP[j]; }
        
        OOWP[i] = sum / (double)op;
    }

    for (int i = 0; i < N; i++)
    {
        double rpi = 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i];
        
        printf("%.8lf\n", rpi);
    }
}

int main()
{
    int T; cin >> T;
    
    for (int t = 1; t <= T; t++)
    {        
        cin >> N;
        for (int i = 0; i < N; i++)
            cin >> input[i];    
                        
        cout << "Case #" << t << ":" << endl;
        solve();
    }      
    
    return 0;
}
