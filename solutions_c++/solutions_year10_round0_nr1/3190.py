#include <iostream>

using namespace std;

int main()
{
    int casos;
    unsigned long long potencias[31];
    potencias[0]=1;
    for (int i=1; i<=30; i++)
        potencias[i]=potencias[i-1]*2;
    cin>>casos;
    for (int ccasos=1; ccasos<=casos; ccasos++)
    {
        unsigned long long n,k;
        cin>>n>>k;
        if ((k+1)%potencias[n]==0)
            cout << "Case #"<<ccasos<<": ON"<<endl;
        else
            cout << "Case #"<<ccasos<<": OFF"<<endl;
    }
    return 0;
}
