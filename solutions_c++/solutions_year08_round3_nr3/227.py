#include<stdio.h>
#include<iostream>
#include<vector>

using namespace std;

int main()
{
    int ncase,ccase;
    vector<long long> A,B,C;
    long long n,m,X,Y,Z;
    long long x,y,z;
    
    cin >> ncase;
    for(ccase = 1;ccase <= ncase;ccase++)
    {
        cin >> n >> m >> X >> Y >> Z;
        
        A.clear();
        for(x = 0;x < m;x++)
        {
            cin >> z;
            A.push_back(z);
        }
        
        B.clear();
        C.clear();
        for(x = 0;x < n;x++)
        {
            C.push_back(0);
            B.push_back(A[x % m]);
            A[x % m] = (((X % Z) * (A[x % m] % Z)) % Z + ((Y % Z) * ((x + 1) % Z)) % Z) % Z;
        }
        
        for(x = B.size() - 1;x >= 0;x--)
        {
            for(y = x + 1;y < B.size();y++)
            {
                if(B[y] > B[x])
                {
                    C[x] += 1 + C[y];
                    C[x] = C[x] % 1000000007;
                }
            }
        }
        
        z = 0;
        for(x = 0;x < B.size();x++)
        {
                z += C[x] % 1000000007;
                z = z % 1000000007;
        }
        z += n;
        z = z % 1000000007;
        
        cout << "Case #" << ccase << ": " << z << endl;
    }

    while(getchar()!=EOF);
    return 0;
}
