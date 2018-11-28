#include <iostream>
#include <vector>

using namespace std;

int main(int argc, char *argv[])
{
    int T,N;
    long int K,val;
    int i;
    cin>>T;
    for(i=0;i<T;i++)
    {
                    cin>>N>>K;
                    val = 1;
                    while(N>0)
                    {
                              val=val*2;
                              N--;
                    }
                    cout<<"Case #"<<i+1<<": ";
                    if(K % val == val-1)
                    {
                         cout<<"ON\n";
                    }
                    else
                    {
                        cout<<"OFF\n";
                    }
    }
    
}
