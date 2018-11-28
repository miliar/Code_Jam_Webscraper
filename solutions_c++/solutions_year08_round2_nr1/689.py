#include <iostream>
#include <algorithm>

using namespace std;

long long arrx[100000];
long long arry[100000];


int main()
{
    int N, n;
    long long A, B, C, D, M, x, y, ret;
    double x1, y1;
    
    cin>>N;
    for (int i = 0; i < N; i++)
    {
        cin>>n>>A>>B>>C>>D>>x>>y>>M;
        arrx[0] = x;
        arry[0] = y;
        ret = 0;
        
        for (int j = 1; j < n; j++)
        {
            arrx[j] = (((arrx[j-1] * A) % M + B) % M);
            arry[j] = (((arry[j-1] * C) % M + D) % M);
        }
    
        for (int j = 0; j < n; j++)
        {
            //cout<<arrx[j]<<" "<<arry[j]<<endl;
            for (int k = j + 1; k < n; k++)
            {
                for (int l = k + 1; l < n; l++)
                {
                    if ((((arrx[j] + arrx[k] + arrx[l]) % 3) == 0) && (((arry[j] + arry[k] + arry[l]) % 3) == 0))       
                       ret++;
                   
                }
            }
        }
        cout<<"Case #"<<i+1<<": "<<ret<<endl;
                    
    }
        
    return 0;
}
