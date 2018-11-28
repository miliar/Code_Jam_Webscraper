# include <iostream>

using namespace std;

int main ()
{
    int test;
    cin>>test;
    int i=1;
    while (test--)
    {
        int N,K;
        cin>>N;  
        cin>>K;
        int value = 1 << N;
        if ((K+1)%value == 0)
        {
           cout<<"Case #"<<i<<": ON"<<endl;
        }
        else
        {
           cout<<"Case #"<<i<<": OFF"<<endl;    
        }
        i++;
    }
    return 0;     
}      
