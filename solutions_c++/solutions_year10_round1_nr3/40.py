#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

const int MAX = 1000000;

int T, A1, A2, B1, B2;
int a[MAX+1];
int b[2*MAX];

int findmax(int x, int y)
{
    return ((x > y) ? x : y);
}

int findmin(int x, int y)
{
    return ((x < y) ? x : y);
}

int main()
{
    ifstream input("C-large.in");
    ofstream output("C-large.out");
    
    a[1] = 1;
    int k = 1;
    for (int n = 2; n <= MAX; n++)
    {
        while (k < n-1 && a[k+1] < n) k++;
        a[n] = n+k;
    }
    b[1] = 1;
    for (int n = 2; n <= MAX; n++)
        for (int m = a[n-1]+1; m <= a[n]; m++) 
            b[m] = n;
    
    input >> T;
    for (int casenum = 0; casenum < T; casenum++)
    {
        input >> A1 >> A2 >> B1 >> B2;
        long long ans = 0;
        for (int x = A1; x <= A2; x++)
        {
            int t = findmin(B2, a[x])- findmax(B1, b[x]) + 1;
            if (t < 0) t = 0;
            ans += (long long)t;
        }
        long long total = ((long long)(A2-A1+1)) * ((long long)(B2-B1+1));
        
        output << "Case #" << casenum+1 << ": " << total-ans << endl;
    }
    
    input.close();
    output.close();
    return 0;
}
