#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <queue>
#include <algorithm>
#include <vector>
#include <stack>
using namespace std;


void solve(int k)
{
    int n; cin >> n;
    vector<string> ar;
    for(int i=0;i<n;i++)
    {
        string s; cin >> s;
        ar.push_back(s);
    }

    vector<double> wp;
    vector<vector<double> > owp;
    for(int i=0;i<n;i++)
    {
        int win = 0;
        int loss = 0;

        for(int j=0;j<n;j++)
        {
            if(ar[i][j] == '1')
                win += 1;
            else if(ar[i][j] == '0')
                loss += 1;
        }

        wp.push_back((double) (win) / (double) (win +loss));


            vector<double> v;
        for(int x=0;x<n;x++)
        {
            int win = 0;
            int loss = 0;
            for(int j=0;j<n;j++)
            {
                if(j == i)
                    continue;
                if(ar[x][j] == '1')
                    win += 1;
                else if(ar[x][j] == '0')
                    loss += 1;
            }

            if((win + loss) > 0)
            v.push_back((double) (win) / (double) (win +loss));
            else
            v.push_back(0.0);
        }

        owp.push_back(v);
    }

    vector<double> owp_avg;
    for(int i=0;i<n;i++)
    {
        int count = 0;
        double avg = 0.0;
        for(int j=0;j<n;j++)
        {
            if(ar[i][j] != '.')
            {
                count++;
                avg += owp[i][j];
            }
        }

        if(count > 0)
            avg /= (double) count;
        else
            avg = 0;

        owp_avg.push_back(avg);
    }


    vector<double> owp_avg_next;
    for(int i=0;i<n;i++)
    {

        int count = 0;
        double avg = 0.0;
        for(int j=0;j<n;j++)
        {
            if(ar[i][j] != '.')
            {
                count++;
                avg += (double)owp_avg[j];
            }
        }

        if(count > 0)
            avg /= (double) count;
        else
            avg = 0;

        owp_avg_next.push_back(avg);
    }

    printf("Case #%d:\n", k);
    for(int i=0;i<n;i++)
        printf("%.6f\n", (0.25*wp[i] + 0.5*owp_avg[i] + 0.25*owp_avg_next[i]));
}

int main()
{
    int n; cin >> n;
    for(int i=0;i<n;i++)
    {
        solve(i+1);
    }
    return 0;
}

