#include<fstream>
#include<algorithm>
#include<vector>
#include<math.h>

using namespace std;

ifstream cin("a.in");
ofstream cout("a.out");

int main()
{
    unsigned T,I,n,i,xorSum,min,Sum;
    cin>>T;
    vector<unsigned> a;
    for(I=1;I<=T;I++)
    {
        cin>>n;
        a.resize(n);
        xorSum=Sum=0;
        min=-1;
        for(i=0;i<n;i++)
        {
            cin>>a[i];
            xorSum^=a[i];
            Sum+=a[i];
            if(a[i]<min)min=a[i];
        }
        cout<<"Case #"<<I<<": ";
        if(xorSum!=0){cout<<"NO"<<endl;continue;}
        cout<<Sum-min<<endl;
    }
    return 0;
}
