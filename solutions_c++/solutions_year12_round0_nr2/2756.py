#include <iostream>
#include <fstream>

using namespace std;

bool check_w_o(int col,int inputs[], int p)
{
    int rem = inputs[col]%3, quo = inputs[col]/3;

    switch(rem)
    {
        case 0: if((quo) >= p)
                    return true;
                else
                    return false;
                break;
        case 1: if((quo+1) >= p)
                    return true;
                else
                    return false;
                break;
        case 2: if((quo-1) >= 0)
                {
                    if((quo+1) >= p)
                        return true;
                    else
                        return false;
                }
                else
                    return false;
                break;
    }
    return false;
}

bool check_w(int col,int inputs[],int p)
{
    int rem = inputs[col]%3, quo = inputs[col]/3;

    switch(rem)
    {
        case 0: if((quo-1) >= 0)
                {
                    if((quo+1) >= p)
                        return true;
                    else
                        return false;
                }
                else
                    return false;
                break;
        case 1: if((quo-2) >= 0)
                {
                    if((quo+1) >= p)
                        return true;
                    else
                        return false;
                }
                else
                    return false;
                break;
        case 2: if((quo+2) >= p)
                    return true;
                else
                    return false;
                break;
    }
    return false;
}

int find_max(int N,int S,int p,int inputs[])
{
    int dp[S+1][N+1];

    for(int i=0; i<=S; i++)
        dp[i][0] = 0;

    for(int i=1; i<=N; i++)
    {
        if(check_w_o(i-1, inputs, p))
            dp[0][i] = 1 + dp[0][i-1];
        else
            dp[0][i] = dp[0][i-1];
    }

    for(int i=1; i<=S; i++)
    {
        for(int j=1; j<=N; j++)
        {
            if(check_w_o(j-1, inputs, p))
                dp[i][j] = 1 + dp[i][j-1];
            else if(check_w(j-1, inputs, p))
                dp[i][j] = 1 + dp[i-1][j-1];
            else dp[i][j] = dp[i][j-1];
        }
    }
    return dp[S][N];
}

int main()
{
    int T, N, S, p, inputs[100];
    ifstream file_in("B-small-attempt0.in");
    ofstream file_out("output.txt");

    file_in>>T;
    for(int i=1; i<=T; i++)
    {
        file_in>>N>>S>>p;

        for(int j=0; j<N; j++)
        {
            file_in>>inputs[j];
        }

        file_out<<"Case #"<<i<<": "<<find_max(N, S, p, inputs);
        if(i != T)
            file_out<<endl;
    }
    return 0;
}
