#include <iostream>

using namespace std;

static const int maxV = 10000000;
static const int maxC =  1000;
int sumV;
int minV;
int realsum;
int n;
int a[maxC];
int testNum, testIndex;


void readInput()
{
    cout << "Case #" << (testIndex+1) << ": ";
    //cout << "\n";    
    cin >> n;
    ///cout << n << " ";
    for (int i = 0; i < n;++i)
    {        
        cin >> a[i];    
    //    cout << a[i] << " ";
    }        
    //cout << "\n";
}

void init()
{
    realsum = 0;
    sumV = 0;
    minV = maxV;
}

void compute()
{
    for (int i = 0; i < n; ++i)
    {
       sumV ^= a[i];
       realsum += a[i];
       if (minV > a[i]) minV = a[i];
    }      
}

void output()
{
    if (sumV) cout << "NO\n";
    else cout << (realsum - minV) << "\n";
}

int main()
{
    cin >> testNum;
    for (testIndex = 0; testIndex < testNum; ++testIndex)
    {
        init();    
        readInput();
        compute();
        output();
    }    
    
}
