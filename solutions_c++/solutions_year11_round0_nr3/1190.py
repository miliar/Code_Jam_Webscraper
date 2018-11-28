#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    int T,Ttotal, N;
    cin>>T;
    Ttotal=T;
    while(T--)
    {
        cin>>N;
        int totalxor = 0, min = 10000000, sum = 0, i;
        int array[N];
        for(i=0;i<N;++i)
        {
            cin>>array[i];
            totalxor ^= array[i];
            if(array[i]<min) min = array[i];
            sum += array[i];
        }
        if(totalxor)
            cout<<"Case #"<<Ttotal-T<<": NO"<<endl;
        else
            cout<<"Case #"<<Ttotal-T<<": "<<sum-min<<endl;
    }
    return 0;
}
