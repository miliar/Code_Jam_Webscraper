#include<iostream>
using namespace std;
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w", stdout);
    int t,i,j,k;
    int match_table[110][110];
    char c;
    cin>>t;
    int n;
    int winning[110] , total[110];
    double wp[110], owp[110], oowp[110], sum, answer[110];
    int count;
    for (i = 1; i<=t; i++)
    {
        cin>>n;
        for (j = 0; j < n; j++)
        {
            total[j] = 0;
            winning[j] = 0;
            for (k = 0; k < n; k++)
            {
                cin>>c;
                if (c == '1')
                {
                   match_table[j][k] = 1;
                   total[j] ++;
                   winning[j] ++;
                }
                else if (c == '0')
                {
                   match_table[j][k] = -1;
                   total[j] ++;
                }
                else match_table[j][k] = 0;
            }
        }
            for (j = 0; j<n; j++)
            {
                wp[j] = (double)winning[j] / (double)total[j];
            }
            
            for (j = 0; j<n; j++)
            {
                count = 0;
                sum = 0.0;
                for (k = 0; k<n; k++)
                {
                    if (match_table[j][k] == 0)
                       continue;
                    count ++;
                    if (match_table[k][j] == 1)
                        sum += (double)(winning[k]-1) / (double)(total[k] - 1);
                    else
                        sum += (double)(winning[k]) / (double)(total[k] - 1);
                }
                if (count != 0)
                   owp[j] = sum / count;
                else
                   owp[j] = 0;
            }
            
            for (j = 0; j<n; j++)
            {
                count = 0;
                sum = 0.0;
                for (k = 0; k<n; k++)
                {
                    if (match_table[j][k] == 0)
                       continue;
                    count ++;
                    sum += owp[k];
                }
                if (count != 0)
                   oowp[j] = sum / count;
                else
                   oowp[j] = 0;
            }
            cout<<"Case #"<<i<<":"<<endl;
            for (j = 0; j<n; j++)
            {
                answer[j] = 0.25*wp[j] + 0.5 * owp[j] + 0.25*oowp[j];
                cout<<answer[j]<<endl;
            }
        }
    return 0;
}
