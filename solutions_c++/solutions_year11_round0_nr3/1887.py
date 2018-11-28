#include <fstream>
#include <algorithm>
using namespace std;

int main()
{
    ifstream fin("input.in");
    ofstream fout("output.in");
    int test;
    fin>>test;
    for(int i=1;i<=test;i++)
    {
        int n;
        fin>>n;
        long *arr=new long[n];
        long long sum=0;
        for(int j=0;j<n;j++)
        {
            fin>>arr[j];
            sum=sum^arr[j];
        }
        if(sum!=0)
        {
            fout<<"Case #"<<i<<": NO"<<endl;
            continue;
        }
        sort(arr,arr+n);
        sum=0;
        for(int j=1;j<n;j++)
        {
            sum+=arr[j];
        }
        fout<<"Case #"<<i<<": "<<sum<<endl;


    }
    return 0;
}
