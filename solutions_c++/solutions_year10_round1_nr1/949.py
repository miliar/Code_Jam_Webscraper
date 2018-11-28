#include <iostream>
using namespace std;

int main()
{
    int T, t;
    int N, K;
    char pattern[51][51];
    int i, j, k;
    bool red, blue;
    int temp;
    int diag;

    cin>>T;
    for(t=1; t<=T; t++)
    {
        cin>>N>>K;
        for(i=1; i<=N; i++)
            for(j=1; j<=N; j++)
                cin>>pattern[i][j];
        for(i=1; i<=N; i++)
        {
            for(j=1; j<=N; j++)
            {
                for(k=N+1-j; k>=1; k--)
                    if(pattern[i][k]!='.')
                    {
                        if(N+1-j!=k)
                        {
                            pattern[i][N+1-j] = pattern[i][k];
                            pattern[i][k] = '.';
                        }
                        break;
                    }
            }
        }
        red = false;
        blue = false;
        for(i=1; i<=N; i++)
        {
            temp = 0;
            for(j=1; j<=N; j++)
            {
                if(pattern[i][j]=='R')
                    temp++;
                else
                {
                    if(temp>=K)
                        red = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                red = true;
        }
        for(j=1; j<=N; j++)
        {
            temp = 0;
            for(i=1; i<=N; i++)
            {
                if(pattern[i][j]=='R')
                    temp++;
                else
                {
                    if(temp>=K)
                        red = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                red = true;
        }
        for(diag=1; diag<=N; diag++)
        {
            temp = 0;
            for(i=1; i<=diag; i++)
            {
                if(pattern[i][diag+1-i]=='R')
                    temp++;
                else
                {
                    if(temp>=K)
                        red = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                red = true;
        }
        for(diag=1; diag<=N; diag++)
        {
            temp = 0;
            for(i=1; i<=diag; i++)
            {
                if(pattern[N+1-i][diag+1-i]=='R')
                    temp++;
                else
                {
                    if(temp>=K)
                        red = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                red = true;
        }
        for(diag=1; diag<=N; diag++)
        {
            temp = 0;
            for(i=1; i<=diag; i++)
            {
                if(pattern[i][N+1-(diag+1-i)]=='R')
                    temp++;
                else
                {
                    if(temp>=K)
                        red = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                red = true;
        }
        for(diag=1; diag<=N; diag++)
        {
            temp = 0;
            for(i=1; i<=diag; i++)
            {
                if(pattern[N+1-i][N+1-(diag+1-i)]=='R')
                    temp++;
                else
                {
                    if(temp>=K)
                        red = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                red = true;
        }
        for(i=1; i<=N; i++)
        {
            temp = 0;
            for(j=1; j<=N; j++)
            {
                if(pattern[i][j]=='B')
                    temp++;
                else
                {
                    if(temp>=K)
                        blue = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                blue = true;
        }
        for(j=1; j<=N; j++)
        {
            temp = 0;
            for(i=1; i<=N; i++)
            {
                if(pattern[i][j]=='B')
                    temp++;
                else
                {
                    if(temp>=K)
                        blue = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                blue = true;
        }
        for(diag=1; diag<=N; diag++)
        {
            temp = 0;
            for(i=1; i<=diag; i++)
            {
                if(pattern[i][diag+1-i]=='B')
                    temp++;
                else
                {
                    if(temp>=K)
                        blue = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                blue = true;
        }
        for(diag=1; diag<=N; diag++)
        {
            temp = 0;
            for(i=1; i<=diag; i++)
            {
                if(pattern[N+1-i][diag+1-i]=='B')
                    temp++;
                else
                {
                    if(temp>=K)
                        blue = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                blue = true;
        }
        for(diag=1; diag<=N; diag++)
        {
            temp = 0;
            for(i=1; i<=diag; i++)
            {
                if(pattern[i][N+1-(diag+1-i)]=='B')
                    temp++;
                else
                {
                    if(temp>=K)
                        blue = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                blue = true;
        }
        for(diag=1; diag<=N; diag++)
        {
            temp = 0;
            for(i=1; i<=diag; i++)
            {
                if(pattern[N+1-i][N+1-(diag+1-i)]=='B')
                    temp++;
                else
                {
                    if(temp>=K)
                        blue = true;
                    temp = 0;
                }
            }
            if(temp>=K)
                blue = true;
        }
        cout<<"Case #"<<t<<": ";
        if(red&&blue)
            cout<<"Both"<<endl;
        else if(!red&&!blue)
            cout<<"Neither"<<endl;
        else if(red&&!blue)
            cout<<"Red"<<endl;
        else
            cout<<"Blue"<<endl;
    }

    return 0;
}

