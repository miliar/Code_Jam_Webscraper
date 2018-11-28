#include <cstdlib>
#include <iostream>

using namespace std;

int main()
{
    int n;
    long int k,pown,T,i=0;
    cin>>T;
    while(i<T)
    {
    cin>>n;
    cin>>k;
    pown=1<<n;
    k=k%pown;
    if(k==(pown-1))
    cout<<"Case #"<<i+1<<": ON";
    else
    cout<<"Case #"<<i+1<<": OFF";
    cout<<"\n";        
    i++;
    }      

    return 1;
}
