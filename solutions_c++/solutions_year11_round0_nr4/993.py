#include <iostream>
#include <iomanip>

using namespace std;

static const int maxN = 1000;
int testNum, testIndex;
int n;
int a[maxN];
double cost;
double perm[maxN+1];
double cycle[maxN+1];
int mark[maxN+1];
int countC[maxN+1];

void init()
{
    cost = 0;
    memset( mark, 0, sizeof( mark ) );
    memset( countC, 0, sizeof( countC ) );
}

void readInput()
{ 
    cin >> n;
    //cout << "Test #" << testIndex << "n = " << n << "\n";
    for (int i = 1; i <= n; ++i)
    {
        cin >> a[i];
        //cout << a[i] << " ";
    }
    //cout << "\n";
}

void compute()
{
    for (int i = 0; i < n; ++i)
    {
        int k = a[i];
        int l = 0;
        while (!mark[k]) 
        {
            mark[k] = 1;
            ++l;
            k = a[k];   
        }
        ++countC[l];
    }
    
    for (int i = 0; i <= maxN; ++i)
        cost += cycle[i] * countC[i];
}

void output()
{
    cout << "Case #" << testIndex << ": " << fixed << setprecision(6) << cost << "\n";
}

void computePerm()
{
    perm[0] = 0;
    perm[1] = 0;
    cycle[0] = 0;
    cycle[1] = 0;
    for (int i = 2; i <= maxN; ++i)
    {
        double sum = 0;
        for (int j = 1; j < i; ++j)
        {                    
            sum += (cycle[j] + perm[i-j]) / i;
        }
        cycle[i] = (sum + 1) * i / (i-1);
        perm[i] = sum + cycle[i] / i;
    }
    /*
    for (int i = 0; i <= maxN; ++i)
    {
        cout << cycle[i] << " ";
    }
    cout << "\n";
    for (int i = 0; i <= maxN; ++i)
    {
        cout << perm[i] << " ";
    }
    cout << "\n";    
    */
}

int main()
{
    computePerm();
    cin >> testNum;
    for (testIndex = 1; testIndex <= testNum; ++testIndex)
    {
        init();
        readInput();
        compute();
        output();              
    }
}
