#include<iostream>
#include<fstream>
using namespace std;

long long n , k;

bool check()
{
     long long f = (1<<n) - 1;
     return (f == (k & f));
}

int main()
{
    ifstream cin("A.in");
    ofstream cout("A.out");
    int T;
    cin>>T;
    for(int c = 1 ; c <= T ; c++)
    {
            cin>>n>>k;
            if(check())
                       cout<<"Case #"<<c<<": ON"<<endl;
            else
                cout<<"Case #"<<c<<": OFF"<<endl;
    }
    return 0;
}
