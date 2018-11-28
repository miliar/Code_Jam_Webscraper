#include <iostream>
#include <algorithm>

using namespace std;

unsigned long long N;
unsigned long long m;
unsigned long long X;
unsigned long long Y;
unsigned long long Z;
unsigned long long n;

unsigned long long A[500000];
unsigned long long seq[500000];

long long numGreater[500000];

unsigned long long recurse(int place)
{
    if(numGreater[place] != -1)
        return numGreater[place];
    
    unsigned long long temp = 1;
    
    for(int j = place-1; j >= 0; --j)
    {
        if(seq[j] < seq[place])
        {
            temp = (temp + recurse(j))%1000000007;
        }
    }
    
    numGreater[place] = temp;
    
    return temp;
}

int main()
{
    cin >> N;
    
    for(int i = 1; i <= N; ++i)
    {
        cin >> n >> m >> X >> Y >> Z;
        
        for(int j = 0; j < m; ++j)
        {
            cin >> A[j];
        }
        
        for(int j = 0; j < n; ++j)
        {
            seq[j] = A[j%m];
            A[j%m] = (X*A[j%m] + Y*(j+1))%Z;
        }
        
        //for(int j = 0; j < 
        
        for(int j = 0; j < n; ++j)
            numGreater[j] = -1;
        
        unsigned long long ans = 0;
        
        for(int j = 0; j < n; ++j)
        {
            ans = (ans + recurse(j))%1000000007;
        }
        
        cout << "Case #" << i << ": " << ans << endl;
    } 
}

