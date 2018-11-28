#include <iostream>
#include <fstream>
#include <vector>
using namespace std;
vector<string> v_1;
vector<string> v_2;
int main()
{
    ifstream cin("a.txt");
    ofstream cout("b.txt");
    long long t, n, min, i, j, z, r, sum;
    cin>>t;
    for (i=0;i<t;++i)
    {
        cin>>n;
        cin>>z;
        min=z;
        r=z;
        sum=z;
        for (j=1;j<n;++j)
        {
            cin>>z;
            sum+=z;
            if (z<min)
            {
                min=z;
            }
            r=(r^z);
        }
        cout<<"Case #"<<(i+1)<<": ";
        if (r!=0)
        {
            cout<<"NO"<<endl;
        }
        else
        {
            cout<<(sum-min)<<endl;
        }
    }
    return 0;
}
