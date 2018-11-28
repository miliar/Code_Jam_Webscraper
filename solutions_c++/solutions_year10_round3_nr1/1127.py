#include <iostream>
#include <vector>
#include <map>
using namespace std;



int main()
{
    int TESTCOUNT;
    cin >> TESTCOUNT;
    #define MAXPATH 10000
    char dummy[MAXPATH];
    for(int testcount = 1; testcount<=TESTCOUNT; testcount++)
    {
        int result = 0;
        int N;
        cin >> N;
        int A[2000],B[2000];
        for(int i = 0; i<N; i++)
        {
            cin >> A[i] >> B[i];
        }
        for(int i = 0; i<N; i++)
        {
            for(int j = i+1; j<N; j++)
            {
                if (i!=j)
                {
                    if (((A[i]-A[j] )*(B[i]-B[j]) ) <=0 )
                        result ++;
                }
            }
        }
        cout << "Case #" << testcount << ": " << result << endl;
    }
    return 0;
}
