#include <iostream>
#include <vector>
using namespace std;

int main()
{
    int i, j;
    long long int A[501][501];
    long long int combo[501][501];
    long long int ans[501];
    int k;
    int T, t, n;

    for(i=0; i<=500; i++)
        for(j=0; j<=500; j++)
            combo[i][j] = 0;
    for(i=0; i<=500; i++)
    {
        combo[i][0] = 1;
        combo[i][i] = 1;
    }
    for(i=2; i<=500; i++)
        for(j=1; j<i; j++)
            combo[i][j] = (combo[i-1][j-1]+combo[i-1][j])%100003;

    for(i=0; i<=500; i++)
        for(j=0; j<=500; j++)
            A[i][j] = 0;
    for(j=2; j<=500; j++)
        A[1][j] = 1;

    for(i=2; i<=500; i++)
    {
        for(j=i+1; j<=500; j++)
        {
            for(k=0; k<i; k++)
                A[i][j] = (A[i][j]+(combo[j-i-1][k]*A[i-1-k][i])%100003)%100003;
        }
    }
    for(j=0; j<=500; j++)
    {
        ans[j] = 0;
        for(i=0; i<=500; i++)
            ans[j] = (ans[j]+A[i][j])%100003;
    }

    cin>>T;
    for(t=1; t<=T; t++)
    {
        cin>>n;
        cout<<"Case #"<<t<<": "<<ans[n]<<endl;
    }

    return 0;
}

