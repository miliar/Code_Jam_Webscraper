#include <cstdio>
#include <queue>
#include <iostream>
#define DEBUG false
using namespace std;

int T; //test cases
int N, S, p, t[101]; //limits
int dp[101][101]; //worker
int viz[101][101]; //worker

struct point
{
    int m;
    int n;
};

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    //reading number of testcases
    cin>>T;

    for (int i = 1; i <= T; i++)
    {
        //readng limits
        cin>>N>>S>>p;

        //reading grades
        for (int j = 1; j <= N; j++)
        {
            cin>>t[j];
        }

        //initializing matrix
        for (int cic = 0; cic < 101; cic++)
        {
            for (int coc = 0; coc < 101; coc++)
            {
                dp[cic][coc] = 0;
                viz[cic][coc] = 0;
            }
        }

        queue<point> Q;

        point start;
        start.m = 0;
        start.n = 0;
        point xxx;

        Q.push(start);

        while(!Q.empty())
        {
            point current = Q.front();
            Q.pop();
            if(DEBUG)
            {
                cout<<"Extracting: "<<current.m<<" "<<current.n<<endl;
            }
            if ((current.m < N) && (current.n <= S))
            {
                int base = t[current.m + 1]/3;
                int diff = t[current.m + 1] - (3 * base);
                if (DEBUG)
                {
                    cout<<"number: "<<t[current.m + 1]<<endl<<"base: "<<base<<endl<<"diff: "<<diff<<endl;
                }
                switch(diff)
                {
                case 0:
                    if (base >= p)
                    {
                        if (dp[current.m + 1][current.n] < (dp[current.m][current.n] + 1))
                        {
                            dp[current.m + 1][current.n] = dp[current.m][current.n] + 1;
                        }
                    }
                    else
                    {
                        if (dp[current.m + 1][current.n] < dp[current.m][current.n])
                        {
                            dp[current.m + 1][current.n] = dp[current.m][current.n];
                        }
                    }
                    if(viz[current.m + 1][current.n] == 0)
                    {
                        xxx.m = current.m + 1;
                        xxx.n = current.n;
                        Q.push(xxx);
                        if (DEBUG)
                        {
                            cout<<"Adding: "<<xxx.m<<" "<<xxx.n<<endl;
                        }
                        viz[current.m + 1][current.n] = 1;
                    }
                    if (((base + 1) <= 10) && ((base - 1) >= 0))
                    {
                        if ((base + 1) >= p)
                        {
                            if (dp[current.m + 1][current.n + 1] < (dp[current.m][current.n] + 1))
                            {
                                dp[current.m + 1][current.n + 1] = dp[current.m][current.n] + 1;
                            }
                        }
                        else
                        {
                            if (dp[current.m + 1][current.n + 1] < dp[current.m][current.n])
                            {
                                dp[current.m + 1][current.n + 1] = dp[current.m][current.n];
                            }
                        }
                    }
                    if(viz[current.m + 1][current.n + 1] == 0)
                    {
                        xxx.m = current.m + 1;
                        xxx.n = current.n + 1;
                        Q.push(xxx);
                        if (DEBUG)
                        {
                            cout<<"Adding: "<<xxx.m<<" "<<xxx.n<<endl;
                        }
                        viz[current.m + 1][current.n + 1] = 1;
                    }
                    break;
                case 1:
                    if ((base + 1) >= p)
                    {
                        if (dp[current.m + 1][current.n] < (dp[current.m][current.n] + 1))
                        {
                            dp[current.m + 1][current.n] = dp[current.m][current.n] + 1;
                        }
                    }
                    else
                    {
                        if (dp[current.m + 1][current.n] < dp[current.m][current.n])
                        {
                            dp[current.m + 1][current.n] = dp[current.m][current.n];
                        }
                    }
                    if(viz[current.m + 1][current.n] == 0)
                    {
                        xxx.m = current.m + 1;
                        xxx.n = current.n;
                        Q.push(xxx);
                        if (DEBUG)
                        {
                            cout<<"Adding: "<<xxx.m<<" "<<xxx.n<<endl;
                        }
                        viz[current.m + 1][current.n] = 1;
                    }
                    if (((base + 1) <= 10) && ((base - 1) >= 0))
                    {
                        if ((base + 1) >= p)
                        {
                            if (dp[current.m + 1][current.n + 1] < (dp[current.m][current.n] + 1))
                            {
                                dp[current.m + 1][current.n + 1] = dp[current.m][current.n] + 1;
                            }
                        }
                        else
                        {
                            if (dp[current.m + 1][current.n + 1] < dp[current.m][current.n])
                            {
                                dp[current.m + 1][current.n + 1] = dp[current.m][current.n];
                            }
                        }
                    }
                    if(viz[current.m + 1][current.n + 1] == 0)
                    {
                        xxx.m = current.m + 1;
                        xxx.n = current.n + 1;
                        Q.push(xxx);
                        if (DEBUG)
                        {
                            cout<<"Adding: "<<xxx.m<<" "<<xxx.n<<endl;
                        }
                        viz[current.m + 1][current.n + 1] = 1;
                    }
                    break;
                case 2:
                    if ((base + 2) <= 10)
                    {
                        if ((base + 2) >= p)
                        {
                            if (dp[current.m + 1][current.n + 1] < (dp[current.m][current.n] + 1))
                            {
                                dp[current.m + 1][current.n + 1] = dp[current.m][current.n] + 1;
                            }
                        }
                        else
                        {
                            if (dp[current.m + 1][current.n + 1] < dp[current.m][current.n])
                            {
                                dp[current.m + 1][current.n + 1] = dp[current.m][current.n];
                            }
                        }
                        if(viz[current.m + 1][current.n + 1] == 0)
                        {
                            xxx.m = current.m + 1;
                            xxx.n = current.n + 1;
                            Q.push(xxx);
                            if (DEBUG)
                            {
                                cout<<"Adding: "<<xxx.m<<" "<<xxx.n<<endl;
                            }
                            viz[current.m + 1][current.n + 1] = 1;
                        }
                    }
                    if ((base + 1) >= p)
                    {
                        if (dp[current.m + 1][current.n] < (dp[current.m][current.n] + 1))
                        {
                            dp[current.m + 1][current.n] = dp[current.m][current.n] + 1;
                        }
                    }
                    else
                    {
                        if (dp[current.m + 1][current.n] < dp[current.m][current.n])
                        {
                            dp[current.m + 1][current.n] = dp[current.m][current.n];
                        }
                    }
                    if(viz[current.m + 1][current.n] == 0)
                    {
                        xxx.m = current.m + 1;
                        xxx.n = current.n;
                        Q.push(xxx);
                        if (DEBUG)
                        {
                            cout<<"Adding: "<<xxx.m<<" "<<xxx.n<<endl;
                        }
                        viz[current.m + 1][current.n] = 1;
                    }
                    break;
                }
            }
        }

        /*for(int xx = 1; xx <= N; xx++)
        {
            for(int yy = 0; yy <= S; yy++)
            {
                cout<<dp[xx][yy]<<" ";
            }
            cout<<endl;
        }*/
        cout<<"Case #"<<i<<": "<<dp[N][S]<<endl;
    }
    return 0;
}

