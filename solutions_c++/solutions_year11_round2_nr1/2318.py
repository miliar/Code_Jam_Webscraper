#include <iostream>
using namespace std;

char board[101][101];
int match[101];
int win[101];
double WP[101];
double OWP[101];
double OOWP[101];
double RPI[101];

int main()
{
    int n, ln;
    double total;
    cin >> n;
    for (int j =0; j < n ; j++)
    {
        cin >> ln;
        for (int k = 0; k <= ln; k++)
        {
            match[k] = win[k] =0;
            WP[k] = OWP[k] = OOWP[k] = RPI[k] = 0.0;
        }
        for (int k = 1; k <= ln; k++)
          for (int m =1; m <= ln ; m++)
            cin >> board[k][m];

        for (int k = 1; k <=ln ; k++)
        {
          for (int m =1; m <= ln ; m++)
          {
            if (board[k][m] == '0' || board[k][m] == '1')
              match[k] ++;
            if (board[k][m] == '1')
              win[k] ++;
          }
          WP[k] = (win[k]*1.0)/match[k];
        }          
              
        for (int k = 1; k <=ln ; k++)
        {
            total = 0.0;
            for (int m = 1; m <= ln ; m++)
            {
                if (board[k][m] == '1')
                  total += (WP[m]*match[m])/(match[m]-1);
                if (board[k][m] == '0')
                  total += (WP[m]*match[m]-1)/(match[m]-1);
            }
            OWP[k] = (total*1.0)/match[k];
        }
        
        for (int k = 1; k <=ln; k++)
        {
            total = 0.0;
            for (int m = 1; m <= ln ; m++)
            {
                if (board[k][m] == '1'||board[k][m]=='0')
                  total += OWP[m];
            }
            OOWP[k] = (total*1.0)/match[k];
        }
        cout << "Case #" << j+1 <<":"<< endl;
        for (int k = 1; k <=ln ; k++)
        {
            cout << 0.25 * WP[k] + 0.50 * OWP[k] + 0.25 *OOWP[k] << endl;   
        }
    }
    
}
