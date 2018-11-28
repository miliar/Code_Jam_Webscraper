#include<algorithm>
#include<iostream>
#include<iomanip>
#include<string>
#include<vector>
#include<cmath>
using namespace std;

int n;
bool match[101][101];
vector <int> opp[101];
double amount[101];
double WP[101] , OWP[101] , OOWP[101];

int main()
{
    freopen("in.txt" , "r" , stdin);
    freopen("out.txt" , "w" , stdout);
    ios :: sync_with_stdio(false);
    cout << fixed << setprecision(16);
    int TestCase;
    cin >> TestCase;
    for(int CaseID = 1 ; CaseID <= TestCase ; CaseID ++)
    {
        cin >> n;
        memset(amount , 0 , sizeof(amount));
        memset(WP , 0 , sizeof(WP));
        memset(OWP , 0 , sizeof(OWP));
        memset(OOWP , 0 , sizeof(OOWP));
        memset(match , 0 , sizeof(match));
        for(int i = 1 ; i <= n ; i++)
        {
            opp[i].clear();
            string s;
            cin >> s;
            s = " " + s; 
            for(int j = 1 ; j <= n ; j++)
                if(s[j] == '1')
                    match[i][j] = 1 , WP[i] += 1.0 , amount[i] += 1.0 , opp[i].push_back(j);
                else if(s[j] == '0')
                    amount[i] += 1.0 , opp[i].push_back(j); 
        }
        for(int i = 1 ; i <= n ; i++)
            WP[i] /= amount[i];
        for(int i = 1 ; i <= n ; i++)
            for(int J = 0 ; J < opp[i].size() ; J++)
            {
                int j = opp[i][J];
                double cnt = 0.0;
                for(int k = 1 ; k <= n ; k++)
                    if(k != i && match[j][k] == 1)
                        cnt += 1.0;
                OWP[i] += cnt / (amount[j] - 1) / amount[i];
            }
        for(int i = 1 ; i <= n ; i++)
            for(int j = 0 ; j < opp[i].size() ; j++)
                OOWP[i] += OWP[opp[i][j]] / amount[i];
        cout << "Case #" << CaseID << ":" << endl;
        for(int i = 1 ; i <= n ; i++)
        {
            double result = WP[i] * 0.25 + OWP[i] * 0.5 + OOWP[i] * 0.25;
            cout << result << endl;
        }
    }
    return 0;
}
