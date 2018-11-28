#include <iostream>
#include <algorithm>

using namespace std;

long long arr[1000];
long long lim[1000];
long long A[100];
long long c = 1000000007;



int main()
{
    long long N, n, m, X, Y, Z;
    long long ret;
    
    cin>>N;
    
    for(int i = 0; i < N; i++)
    {
        cin>>n>>m>>X>>Y>>Z;
        
        for (int j = 0; j < m; j++)
          cin>>A[j];
        
        for (int j = 0; j < n; j++) 
        {
          lim[j] = A[j % m];
          A[j % m] = (A[j % m] * X + Y * (j + 1)) % Z;
          arr[j] = 1;
          //cout<<lim[j]<<endl;
        }
        
        
        ret = 0;
        
        for (int j = 1; j < n; j++)
        {
            for (int l = 0; l < j; l++)
            {
                if (lim[l] < lim[j]) 
                {
                   arr[j] = (arr[j] + arr[l]) % c;
                }
            }
            //cout<<arr[j];
        }
        
        for (int j = 0; j < n; j++)
        {
            ret = (ret + arr[j]) % c;
            //cout<<arr[j];
        }
        
        cout<<"Case #"<<i+1<<": "<<ret<<endl;        
    }
    return 0;
}
    
