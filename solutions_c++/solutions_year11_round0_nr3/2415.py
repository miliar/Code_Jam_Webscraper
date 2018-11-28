#include<iostream>
#include <string>
#include <vector>
#include <bitset>

#include <math.h>

#define dout if(0) cout
#define MAX 1001


using namespace std;

void Compute(int*, int);

int main()
{

    int T;
    cin >>T;
    dout << T << endl;
    for(int t=1; t<=T; ++t)
    {
        int N; cin >>N;
        dout << "-----------------------" << endl;
        dout << N << endl;
        int *A= new int[N];

        for(int i=0; i<N; ++i)
        {
            cin >> A[i];
            dout << A[i] << " ";
        }
        dout << endl;

        cout << "Case #" << t << ": ";
        Compute(A, N) ;
        cout << endl;
    }
}

int Add(int x, int y)
{
    return (x^y);
}


void Compute(int *A, int N)
{
    int max_sum = -1;

    bitset<MAX> bits(1);
    for(unsigned long long i=1; i<=N; ++i)
    {
        int sum0 =0, sum1 =0;
        long as0 =0, as1 =0;

        for(int j=0; j<N; ++j)
        {
            if(bits[j]){
                sum1 = Add(sum1, A[j]);
                as1 += A[j];
            } else {
                sum0 = Add(sum0, A[j]);
                as0 += A[j];
            }
        }
        dout << bits << " " << sum0 << " " << as0 << " | "
             << sum1 << " " << as1 << endl;
        if(sum1 == sum0)
        {
            long max_as = as0 > as1 ? as0 : as1;
            max_sum = max_sum < max_as ? max_as : max_sum;
        }
        bits <<= 1;
    }

    if(max_sum >=0) cout << max_sum;
    else            cout << "NO";
}
