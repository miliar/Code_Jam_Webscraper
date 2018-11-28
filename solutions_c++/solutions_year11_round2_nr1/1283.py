#include <iostream>
#include <string>

using namespace std;

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    string s[100];
    int t, n, i, j, c=1;
    cin >> t;
    while(t--)
    {
        int x[100] = {0}, sum[100] = {0};
        double WP[100]={0}, OWP[100]={0}, OOWP[100]={0};
        cin >> n;
        for(i=0; i<n; i++)
            cin >> s[i];
        for(i=0; i<n; i++)
        {
            for(j=0; j<n; j++)
                if(s[i][j] != '.')
                    sum[i] ++, x[i] += (s[i][j] == '1');
            WP[i] = (double)x[i] / sum[i];
        }
        for(i=0; i<n; i++)
        {
            for(j=0; j<n; j++)
            {
                if(s[i][j] != '.' && s[j][i] == '1')
                    OWP[i] += (double)(x[j] - 1) / (sum[j] - 1);
                else if(s[i][j] != '.')
                    OWP[i] += (double)(x[j]) / (sum[j] - 1);
            }
            OWP[i] /= sum[i];
        }
        for(i=0; i<n; i++)
        {
            for(j=0; j<n; j++)
            {
                if(s[i][j] != '.')
                    OOWP[i] += OWP[j];
            }
            OOWP[i] /= sum[i];
        }
        printf("Case #%d:\n", c++);
        for(i=0; i<n; i++)
        {
            printf("%.10lf\n", 0.25 * WP[i] + 0.50 * OWP[i] + 0.25 * OOWP[i]);
        }
    }
}
