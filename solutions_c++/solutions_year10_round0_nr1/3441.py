//Decision Tree - Round 1B

#include <iostream> 
#include <cmath> 
#include <vector> 
#include <string> 
#include <map> 
#include <iomanip>

using namespace std;

//n-nomber, p-power
int power(int n, int p)
{
    int r = 1;
    
    for(int i = 0; i < p; i++)
    {
        r *= n;   
    }
    return r;
}

int main()
{
    int T, k, n;
    cin>>T;
    for(int i = 0; i < T; i++)
    {
        cin>>n>>k;
        if((k % power(2,n)) == power(2,n)-1)
            cout<<"Case #"<<i+1<<": ON"<<endl;
        else
            cout<<"Case #"<<i+1<<": OFF"<<endl;
    }
}
